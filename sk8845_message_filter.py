import logging

from keycodes import *

# IBM SK-8845 filter


class SK8845MessageFilter:
    def __init__(self):
        self.logger = logging.getLogger(__class__.__name__)
        self.byteorder = "little"
        self.signed = True
        self.keyboard_buf = bytes([0 for _ in range(10)])
        self.key_remap_modifier = {
            KEY_MOD_LCTRL: KEY_MOD_LCTRL,
            KEY_MOD_LSHIFT: KEY_MOD_LSHIFT,
            KEY_MOD_LALT: KEY_MOD_LMETA,
            KEY_MOD_LMETA: KEY_MOD_LALT,
            KEY_MOD_RCTRL: KEY_MOD_RCTRL,
            KEY_MOD_RSHIFT: KEY_MOD_RSHIFT,
            KEY_MOD_RALT: KEY_MOD_LALT,
            KEY_MOD_RMETA: KEY_MOD_RMETA
        }

    def remap_modifier(self, modbyte: bytes):
        modifier_remapped = 0
        for before, after in self.key_remap_modifier.items():
            if modbyte[0] & int.from_bytes(before, byteorder=self.byteorder, signed=self.signed):
                modifier_remapped = modifier_remapped | int.from_bytes(
                    after, byteorder=self.byteorder, signed=self.signed)
        modbyte = modifier_remapped.to_bytes(
            1, self.byteorder, signed=self.signed) + modbyte[1:8]
        return modbyte

    def key_press(self, keycode: bytes) -> bytes:
        for idx in range(4, 10):
            if self.keyboard_buf[idx:idx + 1] == keycode:
                return self.keyboard_buf
            if self.keyboard_buf[idx:idx + 1] == b'\x00':
                return self.keyboard_buf[0:idx] + keycode + self.keyboard_buf[idx + 1:10]
        return self.keyboard_buf

    def key_release(self, keycode: bytes) -> bytes:
        for idx in range(4, 10):
            if self.keyboard_buf[idx:idx + 1] == keycode:
                return self.keyboard_buf[0:idx] + b'\x00' + self.keyboard_buf[idx + 1:10]
        return self.keyboard_buf

    def handle_key(self, condition: bool, keycode: bytes):
        if condition:
            self.keyboard_buf = self.key_press(keycode)
        else:
            self.keyboard_buf = self.key_release(keycode)

    def filter_message_to_host(self, msg) -> bytes:
        self.logger.debug(f"filter msg {msg}")
        if len(msg) == 8:
            self.keyboard_buf = b'\xa1\x01' + \
                self.remap_modifier(msg[0:1]) + msg[1:8]
            return self.keyboard_buf
        elif len(msg) == 5 and msg[0] == 1:
            # mouse
            # 00 01 02 03 04 05 06 07 08
            # A1 03 Btns  X     Y     Wh
            return b'\xa1\x03' + self.get_buttons_flags(msg) + self.get_x(msg) + self.get_y(msg) + self.get_wheel(msg)
        elif msg[0] == 2:
            # HANDLE_KEY(buf[1] == 2, KEY_ARDUINO_F15);
            code = int.from_bytes(
                msg[1:2], byteorder=self.byteorder, signed=self.signed)
            self.handle_key(code == 2, KEY_F15)
            return self.keyboard_buf
        elif msg[0] == 3:
            msg_in_int = int.from_bytes(
                msg[1:4], byteorder="big", signed=False)
            self.handle_key(0 != (msg_in_int & BYTES_MAGNIFIER), KEY_F13)
            self.handle_key(0 != (msg_in_int & BYTES_SCREEN_OFF), KEY_F14)
            self.handle_key(0 != (msg_in_int & BYTES_WIRELESS), KEY_F16)
            self.handle_key(0 != (msg_in_int & BYTES_SCREEN_OUTPUT), KEY_F17)
            self.handle_key(0 != (msg_in_int & BYTES_HIBERNATE), KEY_F18)
            self.handle_key(0 != (msg_in_int & BYTES_BRIGHTNESS_UP), KEY_F20)
            self.handle_key(0 != (msg_in_int & BYTES_BRIGHTNESS_DOWN), KEY_F21)
            self.handle_key(0 != (msg_in_int & BYTES_ACCESS_IBM), KEY_F22)
            self.handle_key(0 != (msg_in_int & BYTES_VOLUME_UP), KEY_VOLUMEUP)
            self.handle_key(
                0 != (msg_in_int & BYTES_VOLUME_DOWN), KEY_VOLUMEDOWN)
            self.handle_key(0 != (msg_in_int & BYTES_VOLUME_MUTE), KEY_MUTE)
            return self.keyboard_buf
        self.logger.warning("unrecognized pattern")
        return None

    def get_buttons_flags(self, msg):
        return msg[1:2] + b'\x00'

    def get_x(self, msg):
        value = int.from_bytes(
            msg[2:3], byteorder=self.byteorder, signed=self.signed)
        result = value.to_bytes(2, self.byteorder, signed=self.signed)
        return result

    def get_y(self, msg):
        value = int.from_bytes(
            msg[3:4], byteorder=self.byteorder, signed=self.signed)
        result = value.to_bytes(2, self.byteorder, signed=self.signed)
        return result

    def get_wheel(self, msg):
        return msg[4:5]

    def filter_message_from_host(self, msg):
        return None
