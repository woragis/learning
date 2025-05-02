#include <stdio.h>
#include <stdbool.h>

void inc_dec(int number);
void bit(int number);
void print_binary(unsigned int num);

int main()
{
    int a = 10;
    inc_dec(a);
    bit(a);
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

void bit(int number)
{
    unsigned int a = 60;
    unsigned int b = 13;
    printf("===================BITWISE===================\n");
    printf("=-=-=-=-=-=Numbers: a=%d .... b=%d=-=-=-=-=-=\n", a, b);
    // printf("Binaries: a=%d ... b=%d\n", a, b);
    printf("a: ");
    print_binary(a);
    printf("b: ");
    print_binary(b);
    printf("=-=-=-=-=-=-=-=& Operator (AND)-=-=-=-=-=-=-=\n");
    printf("c: ");
    print_binary(a & b);
    printf("Numbers: c=%d\n", a & b);
    printf("=-=-=-=-=-=-=-=| Operator (OR)=-=-=-=-=-=-=-=\n");
    printf("c: ");
    print_binary(a | b);
    printf("Numbers: c=%d\n", a | b);
    printf("=-=-=-=-=-=-=-=^ Operator (XOR)-=-=-=-=-=-=-=\n");
    printf("c: ");
    print_binary(a ^ b);
    printf("Numbers: c=%d\n", a ^ b);
    printf("=-=-=-=-=<< Operator (SHIFT To Right)-=-=-=-=\n");
    printf("a: ");
    print_binary(a << 2);
    printf("Numbers: 'a << 2' = %d\n", a << 2);
    printf("=-=-=-=-=<< Operator (SHIFT To Left)=-=-=-=-=\n");
    printf("a: ");
    print_binary(a >> 2);
    printf("Numbers: 'a >> 2' = %d\n", a >> 2);
    printf("=============================================\n");
}

void print_binary(unsigned int num)
{
    for (int i = 31; i >= 0; i--)
    {
        unsigned int bit = (num >> i) & 1;
        printf("%u", bit);

        // Optional: Add a space every 4 bits
        if (i % 4 == 0)
        {
            printf(" ");
        }
    }
    printf("\n");
}