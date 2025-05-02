#include <stdio.h>
#include <stdbool.h>

int main()
{
    printf("Size of 'char': %d\n", sizeof(char));
    printf("Size of 'bool': %d\n", sizeof(bool));
    printf("Size of 'int': %d\n", sizeof(int));
    printf("Size of 'long': %d\n", sizeof(long));
    printf("Size of 'long long': %d\n", sizeof(long long));
    printf("Size of 'double': %d\n", sizeof(double));
    printf("Size of 'long double': %d\n", sizeof(long double));
    printf("Size of 'NULL': %d\n", sizeof(NULL));

    return 0;
}