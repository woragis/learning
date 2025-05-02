/*
 * Purpouse: Show variables and its Data Types
 * Author: woragis
 */

#include <stdio.h>

int main()
{
    int integerVar = 100;
    float floatVar = 331.79;
    double doubleVar = 8.44e+11;
    char charVar = 'W';
    _Bool boolVar = 0;

    printf("Integer var: %i\n", integerVar);
    printf("Float var: %f\n", floatVar);
    printf("Double var: %e\n", doubleVar);
    printf("Double var: %g\n", doubleVar);
    printf("Char var: %c\n", charVar);
    printf("Bool var: %u\n", boolVar);
    return 0;
}