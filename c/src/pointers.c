#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(int argc, char *argv[])
{
    for (int i = 0; i < argc; i++)
    {
        char *variable = (char *)argv[i];
        char **pointer = &argv[i];
        printf("Variable: %s\n", variable);
        printf("Pointer: %p\n", pointer);
        printf("Pointer address: %p\n", *pointer);
        // printf("Argument %d: %s\n", i, (char *)argv[i]);
        // printf("Argument %d pointer: %p\n", i, *(char *)argv[i]);
    }
    return 0;
}
