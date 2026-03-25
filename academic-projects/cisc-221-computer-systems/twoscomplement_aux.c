// Arham Hassan | 20426387 | 23cr8@queensu.ca | CISC 221 Assignment 2
// What we're Implementing: int subtract2sc_issafe(int x, int y)
// Returns 1 if x - y can be represented in signed two's-complement int,
// returns 0 if it could overflow. We're trying to avoid an overflowing.
//
// Some Notes:
// - We will NOT assume a specific int width. Instead, we record it using sizeof(int)*CHAR_BIT.


#include <limits.h>   // INT_MIN, INT_MAX, CHAR_BIT
#include <stddef.h>   // optional

int subtract2sc_issafe(int x, int y) {
    // We record width but don't need it for the checks below.
    const int INT_WIDTH = (int)(sizeof(int) * CHAR_BIT);
    (void)INT_WIDTH;

    if (y > 0) {
        // x - y < INT_MIN  <=>  x < INT_MIN + y
        // INT_MIN + y cannot overflow because y > 0 moves value toward zero.
        return x >= INT_MIN + y;
    } else if (y < 0) {
        // x - y > INT_MAX  <=>  x > INT_MAX + y
        // INT_MAX + y cannot overflow because y < 0 moves value toward zero.
        return x <= INT_MAX + y;
    } else {
        // y == 0: always safe
        return 1;
    }
}


