#ifndef DEBUGPRINT_H
#define DEBUGPRINT_H

#include <stdio.h>

// #define _DEBUG

#ifdef _DEBUG
#define DEBUG_PRINTF(...) printf(__VA_ARGS__)
#else
#define DEBUG_PRINTF(x, ...)
#endif

#endif
