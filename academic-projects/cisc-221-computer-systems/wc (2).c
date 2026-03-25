/*
 * CISC 221 — Assignment 1: wc (word count)
 * Author: Arham Hassan, 20426387
 * Purpose:
 *   Mimic the Linux 'wc' for ASCII text, will print the following:
 *     lines  words  chars
 *
 * What the code has in it:
 *   - Delimiters that separate words: space ' ', tab '\t', newline '\n' only.
 *   - Punctuation counts as part of a word unless it is stand-alone
 *     (e.g., "h . h" → 3 words; "h, h" → 2 words).
 *   - ASCII only: 1 byte == 1 character → the 'chars' count equals POSIX wc's
 *     "bytes" column on these inputs.
 *   - Lines are counted by the number of newline characters read ('\n').
 *
 * I/O model:
 *   - Read from stdin until EOF (Ctrl-D on a blank line in the terminal).
 *   - Write a single line: "<lines> <words> <chars>\n".
 *
 * Build (on CASLab Linux):
 *   gcc -std=c17 -Wall -Wextra -O2 -o wc wc.c
 *
 * Example:
 *   printf("h . h\n") | ./wc     → 1 3 6
 *   ./wc < ABC.txt ; wc < ABC.txt  (should match for ASCII)
 */


 
#include <stdio.h>   // to be able to getchar, printf

/* Return 1 iff c is a word delimiter according to what the assignment asked. */
static int is_delim(int c) {
    return (c == ' ') || (c == '\t') || (c == '\n');
}

int main(void) {
    /* CHoosing a big counter to avoid overflow on large inputs. */
    unsigned long long lines = 0, words = 0, chars = 0;

    /* Two word scanners one for when we're in a word and one for when we're not:
       in_word == 0 : currently on a delimiter or at start
       in_word == 1 : currently inside a (non-delimiter) word
     */
    int in_word = 0;

    /* This will read bytes as int so EOF (-1) is distinguishable from valid bytes. */
    int c;

    while ((c = getchar()) != EOF) {
        /* Every byte counts as a character (ASCII assumption). */
        chars++;

        /* We set a new line to mark the end of the previous line. */
        if (c == '\n') {
            lines++;
        }

        if (is_delim(c)) {
            /* We are on a delimiter; next non-delimiter may start a word. */
            in_word = 0;
        } else if (!in_word) {
            /* Transition delimiter -> non-delimiter: start of a new word. */
            words++;
            in_word = 1;
        }
        /* Else: if we're still going on with the same word; then do nothing. */
    }

    /* Print in the same order as Unix wc: lines words bytes (bytes==chars). */
    printf("%llu %llu %llu\n", lines, words, chars);
    return 0;
}
