import asyncio
import sys
from signal import SIGINT
import json
import logging
import logging.config
import asyncio_glib

from dasbus.connection import SystemMessageBus
from hid_devices import HIDDeviceRegistry

if __name__ == "__main__":
    server_config = json.load(open("logger_config.json", "r"))
    logging.config.dictConfig(server_config)
    root_logger = logging.getLogger()
    root_logger.info(
        f"Log level set to {logging.getLevelName(root_logger.getEffectiveLevel())}")

    asyncio.set_event_loop_policy(asyncio_glib.GLibEventLoopPolicy())
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(SIGINT, sys.exit)
    bus = SystemMessageBus()
    hid_devices = HIDDeviceRegistry(loop)
    loop.run_forever()
