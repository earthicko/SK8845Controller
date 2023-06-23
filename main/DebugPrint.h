#ifndef DEBUGPRINT_H
#define DEBUGPRINT_H

#include "SerialPrintf.h"
#include <Arduino.h>

// #define _DEBUG
// #define CONFIG_NIMBLE_CPP_LOG_LEVEL 5

#ifdef _DEBUG
#define DEBUG_PRINT(str) Serial.print(str)
#define DEBUG_PRINTF(...) SerialPrintf(__VA_ARGS__)
#define DEBUG_PRINTLN(str) Serial.println(str)
#else
#define DEBUG_PRINT(x)
#define DEBUG_PRINTF(x, ...)
#define DEBUG_PRINTLN(x)
#endif

#endif
