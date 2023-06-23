#ifndef BLECOMBOPARSER_H
#define BLECOMBOPARSER_H

#include <BLECombo.h>

#define BLECOMBOPARSER_MOVE_MULTIPLIER 3
#define BLECOMBOPARSER_MOVE_DIVIDER 2
#define BLECOMBOPARSER_SCROLL_MULTIPLIER 1
#define BLECOMBOPARSER_SCROLL_DIVIDER 2
#define BLECOMBOPARSER_SCROLL_UPDATE_FREQ 5

#define BYTES_MAGNIFIER 0x1000000
#define BYTES_SCREEN_OFF 0x10000
#define BYTES_WIRELESS 0x20000
#define BYTES_SCREEN_OUTPUT 0x40000
#define BYTES_HIBERNATE 0x80000
#define BYTES_BRIGHTNESS_UP 0x100000
#define BYTES_BRIGHTNESS_DOWN 0x200000
#define BYTES_ACCESS_IBM 0x400000
#define BYTES_VOLUME_UP 0x100
#define BYTES_VOLUME_DOWN 0x200
#define BYTES_VOLUME_MUTE 0x400

#define KEY_F13 0x68
#define KEY_F14 0x69
#define KEY_F15 0x6A
#define KEY_F16 0x6B
#define KEY_F17 0x6C
#define KEY_F18 0x6D
#define KEY_F19 0x6E
#define KEY_F20 0x6F
#define KEY_F21 0x70
#define KEY_F22 0x71

#define ARDUINO_KEYCODE_OFFSET 136

#define KEY_ARDUINO_F13 (KEY_F13 + ARDUINO_KEYCODE_OFFSET)
#define KEY_ARDUINO_F14 (KEY_F14 + ARDUINO_KEYCODE_OFFSET)
#define KEY_ARDUINO_F15 (KEY_F15 + ARDUINO_KEYCODE_OFFSET)
#define KEY_ARDUINO_F16 (KEY_F16 + ARDUINO_KEYCODE_OFFSET)
#define KEY_ARDUINO_F17 (KEY_F17 + ARDUINO_KEYCODE_OFFSET)
#define KEY_ARDUINO_F18 (KEY_F18 + ARDUINO_KEYCODE_OFFSET)
#define KEY_ARDUINO_F19 (KEY_F19 + ARDUINO_KEYCODE_OFFSET)
#define KEY_ARDUINO_F20 (KEY_F20 + ARDUINO_KEYCODE_OFFSET)
#define KEY_ARDUINO_F21 (KEY_F21 + ARDUINO_KEYCODE_OFFSET)
#define KEY_ARDUINO_F22 (KEY_F22 + ARDUINO_KEYCODE_OFFSET)

#define HANDLE_KEY(condition, keycode)                                         \
	if (condition)                                                             \
	{                                                                          \
		keyPress(keycode);                                                     \
	}                                                                          \
	else                                                                       \
	{                                                                          \
		keyRelease(keycode);                                                   \
	}

class BLEComboParser : public BLECombo
{
  public:
	BLEComboParser(std::string deviceName = "ESP32 Combo",
				   std::string deviceManufacturer = "Espressif",
				   uint8_t batteryLevel = 90);
	void parseHIDDataKeyboard(const int8_t *buf);
	void parseHIDDataMouse(const int8_t *buf);

  private:
	void handleMouse1(const int8_t *buf);
	void handleMouse2(const int8_t *buf);
	void handleMouse3(const int8_t *buf);
};

typedef void (BLEComboParser::*parser_t)(const int8_t *);

#endif
