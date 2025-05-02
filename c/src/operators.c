#include <stdio.h>
#include <stdbool.h>

void inc_dec(int number);

int main()
{
    int a = 10;
    inc_dec(a);
    return 0;
}

void inc_dec(int number)
{
    printf("===========Increment=and=Decrement===========\n");
    printf("A: %d\n", number);
    printf("A incrementing before the line is run: %d\n", ++number);
    printf("A decrementing before the line is run: %d\n", --number);
    printf("A incrementing after the line is run: %d\n", number++);
    printf("A decrementing after the line is run: %d\n", number--);
    printf("=============================================\n");
}
