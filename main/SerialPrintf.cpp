#include <Arduino.h>
#include <stdarg.h>
#include <stdio.h>

void SerialPrintf(const char *s, ...)
{
	va_list args;
	va_start(args, s);
	int n = vsnprintf(NULL, 0, s, args); // 문자열 길이를 먼저 구함
	char *str = new char[n + 1];         // 메모리 할당
	vsprintf(str, s, args);              // 실제 내용을 복사
	va_end(args);
	Serial.print(str);
	delete[] str; // 메모리 해제
}
