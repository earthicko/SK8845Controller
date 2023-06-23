#include "BLEComboParser.h"
#include "DebugPrint.h"
#include <stdlib.h>

BLEComboParser::BLEComboParser(std::string deviceName, std::string deviceManufacturer, uint8_t batteryLevel)
    : BLECombo(deviceName, deviceManufacturer, batteryLevel)
{
}

void BLEComboParser::parseHIDDataKeyboard(const int8_t* buf)
{
    this->sendReport((keyreport_t*)buf);
}

static bool should_update_scroll(void)
{
    static int counter;

    counter++;
    if (counter != BLECOMBOPARSER_SCROLL_UPDATE_FREQ)
        return (false);
    counter = 0;
    return (true);
}

void BLEComboParser::handleMouse1(const int8_t* buf)
{
    static bool prev_middle_stat;
    static bool did_trigger_wheel_movement;
    static int scroll_d[2];

    int8_t m[5];
    memset(m, 0, sizeof(m));
    if (buf[1] & MOUSE_MIDDLE) {
        // middle button stays being pressed
        if (should_update_scroll()) {
            // update scroll movement
            m[0] = buf[1] & ~((int8_t)MOUSE_MIDDLE); // button state
            m[3] = scroll_d[0] * BLECOMBOPARSER_SCROLL_MULTIPLIER / BLECOMBOPARSER_SCROLL_DIVIDER / BLECOMBOPARSER_SCROLL_UPDATE_FREQ; // vertical wheel = dy
            m[4] = scroll_d[1] * BLECOMBOPARSER_SCROLL_MULTIPLIER / BLECOMBOPARSER_SCROLL_DIVIDER / BLECOMBOPARSER_SCROLL_UPDATE_FREQ; // horizontal wheel = dx
            did_trigger_wheel_movement = true;
            scroll_d[0] = 0;
            scroll_d[1] = 1;
        } else {
            // ignore scroll movement
            m[0] = buf[1] & ~((int8_t)MOUSE_MIDDLE); // button state
            scroll_d[0] += -buf[3];
            scroll_d[1] += buf[2];
        }
    } else if (!(buf[1] & MOUSE_MIDDLE) && (prev_middle_stat)) {
        // middle button just being released
        if (did_trigger_wheel_movement) {
            // middle button was pressed to scroll
            m[0] = buf[1]; // button state
            m[1] = ((int)(buf[2])) * BLECOMBOPARSER_MOVE_MULTIPLIER / BLECOMBOPARSER_MOVE_DIVIDER; // dx
            m[2] = ((int)(buf[3])) * BLECOMBOPARSER_MOVE_MULTIPLIER / BLECOMBOPARSER_MOVE_DIVIDER; // dy
            did_trigger_wheel_movement = false;
        } else {
            // middle button was pressed to act as wheel click
            mouseClick(MOUSE_MIDDLE);
            prev_middle_stat = false;
            return;
        }
    } else {
        // middle button stays being released
        m[0] = buf[1]; // button state
        m[1] = ((int)(buf[2])) * BLECOMBOPARSER_MOVE_MULTIPLIER / BLECOMBOPARSER_MOVE_DIVIDER; // dx
        m[2] = ((int)(buf[3])) * BLECOMBOPARSER_MOVE_MULTIPLIER / BLECOMBOPARSER_MOVE_DIVIDER; // dy
    }
    prev_middle_stat = buf[1] & MOUSE_MIDDLE;

    DEBUG_PRINTF("m = {");
    for (int i = 0; i < 5; i++)
        DEBUG_PRINTF("%d, ", m[i]);
    DEBUG_PRINTF("}\n");

    mouseNotify(sizeof(m), (uint8_t*)m);
}

void BLEComboParser::handleMouse2(const int8_t* buf)
{
    HANDLE_KEY(buf[1] == 2, KEY_ARDUINO_F15);
}

void BLEComboParser::handleMouse3(const int8_t* buf)
{
    uint32_t pattern = *((uint32_t*)buf);
    DEBUG_PRINTF("buf as uint32_t = %x\n", pattern);
    HANDLE_KEY(pattern & BYTES_MAGNIFIER, KEY_ARDUINO_F13);
    HANDLE_KEY(pattern & BYTES_SCREEN_OFF, KEY_ARDUINO_F14);
    HANDLE_KEY(pattern & BYTES_WIRELESS, KEY_ARDUINO_F16);
    HANDLE_KEY(pattern & BYTES_SCREEN_OUTPUT, KEY_ARDUINO_F17);
    HANDLE_KEY(pattern & BYTES_HIBERNATE, KEY_ARDUINO_F18);
    HANDLE_KEY(pattern & BYTES_BRIGHTNESS_UP, KEY_ARDUINO_F20);
    HANDLE_KEY(pattern & BYTES_BRIGHTNESS_DOWN, KEY_ARDUINO_F21);
    HANDLE_KEY(pattern & BYTES_ACCESS_IBM, KEY_ARDUINO_F22);
    HANDLE_KEY(pattern & BYTES_VOLUME_UP, KEY_MEDIA_VOLUME_UP);
    HANDLE_KEY(pattern & BYTES_VOLUME_DOWN, KEY_MEDIA_VOLUME_DOWN);
    HANDLE_KEY(pattern & BYTES_VOLUME_MUTE, KEY_MEDIA_MUTE);
}

void BLEComboParser::parseHIDDataMouse(const int8_t* buf)
{
    switch (buf[0]) {
    case 1:
        handleMouse1(buf);
        break;
    case 2:
        handleMouse2(buf);
        break;
    case 3:
        handleMouse3(buf);
        break;
    default:
        break;
    }
}
