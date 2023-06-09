import os
import asyncio
import logging
from watchgod import awatch, AllWatcher

from sk8845_message_filter import SK8845MessageFilter


class HIDDevice:
    def __init__(self, device: dict, loop: asyncio.AbstractEventLoop):
        self.logger = logging.getLogger(__class__.__name__)
        self.loop = loop
        self.filter = SK8845MessageFilter()
        self.device_id: str = device["instance"]
        self.logger.debug(f"read from {'/dev/' + device['hidraw']}")
        self.hidraw_file = os.open(
            '/dev/' + device["hidraw"], os.O_RDWR | os.O_NONBLOCK)
        loop.add_reader(self.hidraw_file, self.hidraw_event)
        self.logger.debug(f"HID Device {self.device_id} created")

    def hidraw_event(self):
        if self.hidraw_file is None:
            return
        try:
            msg = os.read(self.hidraw_file, 16)
        except Exception:
            self.loop.remove_reader(self.hidraw_file)
            os.close(self.hidraw_file)
            self.hidraw_file = None
            self.logger.error(
                f"HID device {self.device_id} exception on read. closing")
            return
        tm = self.filter.filter_message_to_host(msg)
        self.logger.debug(f"hid raw event filtered {tm}")

    def __eq__(self, other):
        return self.device_id == other.device_id

    def __del__(self):
        self.logger.debug(f"HID Device {self.device_id} removed")


class DeviceDirWatcher(AllWatcher):
    def should_watch_dir(self, entry):
        return entry.path.count('/') == 3


class HIDDeviceRegistry:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.logger = logging.getLogger(__class__.__name__)
        self.loop = loop
        self.capturing_devices = {}
        asyncio.run_coroutine_threadsafe(
            self.__watch_device_changes(), loop=self.loop)
        self.__scan_devices()

    async def __watch_device_changes(self):
        async for changes in awatch('/dev/input', watcher_cls=DeviceDirWatcher):
            self.__scan_devices()

    def __scan_devices(self):
        for device in os.listdir('/sys/bus/hid/devices'):
            try:
                with open('/sys/bus/hid/devices/' + device + '/uevent', 'r') as uevent:
                    hidraw = os.listdir(
                        '/sys/bus/hid/devices/' + device + '/hidraw')[0]
                    self.logger.debug(f"create hiddevice {device} {hidraw}")
                    self.capturing_devices[device] = HIDDevice(
                        {"instance": device, "hidraw": hidraw}, self.loop)
            except Exception as exc:
                self.logger.error(
                    f"Error while loading HID device: {device}, Error: {exc}, Skipping.")
