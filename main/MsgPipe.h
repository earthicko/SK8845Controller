#ifndef MSGPIPE_H
#define MSGPIPE_H

#include "DebugPrint.h"
#include <Arduino.h>
#include <stdint.h>
#include <string.h>

#define MSGPIPE_DEFAULT_SIZE 0x100

typedef struct hidmsg_s
{
	uint8_t ep;
	uint8_t len;
	uint8_t buf[8];
} hidmsg_t;

template <typename MSG>
class MsgPipe
{
  private:
	SemaphoreHandle_t _lock;
	MSG *_msg;
	int _tail;
	int _len;
	int _cap;

  public:
	MsgPipe(int cap = MSGPIPE_DEFAULT_SIZE)
	{
		_lock = xSemaphoreCreateMutex();
		_msg = new MSG[cap + 1];
		_tail = 0;
		_len = 0;
		_cap = cap;
	}
	~MsgPipe()
	{
		delete[] _msg;
	}
	int push(const MSG *input)
	{
		if (xSemaphoreTake(_lock, portMAX_DELAY) != pdTRUE)
		{
			DEBUG_PRINTF("Cannot obtain pipe lock.\n");
			return (1);
		}
		if (_len >= _cap)
		{
			DEBUG_PRINTF("Msg Pipe is full.\n");
			xSemaphoreGive(_lock);
			return (1);
		}
		_msg[(_tail + _len) % (_cap + 1)] = *input;
		_len = _len + 1;
		xSemaphoreGive(_lock);
		return (0);
	}
	int pop(MSG *returnBuf)
	{
		if (xSemaphoreTake(_lock, portMAX_DELAY) != pdTRUE)
		{
			DEBUG_PRINTF("Cannot obtain pipe lock.\n");
			return (1);
		}
		if (_len <= 0)
		{
			xSemaphoreGive(_lock);
			return (1);
		}
		*returnBuf = _msg[_tail];
		_tail = (_tail + 1) % (_cap + 1);
		_len = _len - 1;
		xSemaphoreGive(_lock);
		return (0);
	}
};

#endif
