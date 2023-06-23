#include "BLEComboParser.h"
#include "DebugPrint.h"
#include "MsgPipe.h"
#include "Wire.h"
#include "remapKeyboard.h"

const TickType_t delay_tick = 10;

constexpr uint32_t HEARTBEAT_PERIOD{1000};
constexpr uint8_t CORE_TASK_BLE{0};
constexpr uint8_t I2C_DEV_ADDR{0x55};
constexpr uint8_t I2C_BUF_SIZE{32};

static TaskHandle_t task_handle_ble;

MsgPipe<hidmsg_t> hid_msg_pipe;
BLEComboParser ble("IBM UltraNav", "IBM / rokart", 100);

void onRequest(void)
{
	static uint32_t i;

	Wire.print(i++);
	Wire.print(" Packets.");
	Serial.println("onRequest");
}

void onReceive(int len)
{
	if (len > I2C_BUF_SIZE)
	{
		while (Wire.available())
			Wire.read();
		return;
	}

	DEBUG_PRINTF("onReceive[%d]: ", len);
	uint8_t buf[I2C_BUF_SIZE];
	for (uint8_t i = 0; Wire.available(); i++)
	{
		buf[i] = Wire.read();
		DEBUG_PRINTF("%d, ", (int8_t)(buf[i]));
	}
	DEBUG_PRINTF("\n");

	hidmsg_t msg;
	msg.ep = len == 8 ? 1 : 2;
	msg.len = len;
	memcpy(msg.buf, buf, msg.len);

	DEBUG_PRINTF("ep %d len %d buf {", msg.ep, msg.len);
	for (uint8_t i = 0; i < msg.len; i++)
		DEBUG_PRINTF("%d, ", (int8_t)(msg.buf[i]));
	DEBUG_PRINTF("}\n");

	if (msg.ep == 1)
	{
		uint8_t modifierRemapped = 0;
		for (int i = 0; i < 8; i++)
		{
			if (msg.buf[0] & keycodeMapModifier[i][0])
				modifierRemapped |= keycodeMapModifier[i][1];
		}
		msg.buf[0] = modifierRemapped;
		for (int i = 2; i < 8; i++)
			msg.buf[i] = keycodeMap[msg.buf[i]];
	}

	hid_msg_pipe.push(&msg);
}

void BLETask(void *parameter)
{
	static bool connection;
	static const parser_t parsers[] = {
		(const parser_t)(NULL),
		(const parser_t)(&BLEComboParser::parseHIDDataKeyboard),
		(const parser_t)(&BLEComboParser::parseHIDDataMouse),
	};

	DEBUG_PRINTF("BLETask start.\n");
	ble.begin();
	while (true)
	{
		if (ble.isConnected())
		{
			if (connection == false)
			{
				DEBUG_PRINTF("BLE Connected\n");
				connection = true;
			}
		}
		else
		{
			if (connection == true)
			{
				DEBUG_PRINTF("BLE Disconnected\n");
				connection = false;
			}
		}
		hidmsg_t msg;
		if (hid_msg_pipe.pop(&msg))
		{
			vTaskDelay(delay_tick);
			continue;
		}
		if (!ble.isConnected())
		{
			vTaskDelay(delay_tick);
			continue;
		}
		(ble.*parsers[msg.ep])((int8_t *)msg.buf);
	}
}

void setup(void)
{
#ifdef _DEBUG
	Serial.begin(115200);
#endif
	DEBUG_PRINTF("Start\n");

	Wire.onReceive(onReceive);
	Wire.onRequest(onRequest);
	Wire.begin(I2C_DEV_ADDR);

	xTaskCreatePinnedToCore(BLETask,          // Function to implement the task
							"BLETask",        // Name of the task
							8192,             // Stack size in words
							NULL,             // Task input parameter
							2,                // Priority of the task
							&task_handle_ble, // Task handle.
							CORE_TASK_BLE);   // Core where the task should run
}

void loop(void)
{
}
