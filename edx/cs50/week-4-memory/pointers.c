#include <stdio.h>

int main(int argc, char* argv)
{
    int* myPointer;
    int myAge = 20;
    myPointer = &myAge;
    printf("Value stored in my Pointer: %i\n", *myPointer);
    printf("Basically this was the value of my variable 'age': '%i'\n", myAge);
    printf("\n");

    printf("Address of my variable: %p\n", &myAge);
    printf("Pointer value: %p\n", myPointer);
    printf("(basically the address of the variable)\n");
    printf("\n");

    printf("Pointer address: %p\n", &myPointer);
    printf("\n");

    printf("Pointer value: %p\n", myPointer);
    printf("Pointer dereferenced value: %i\n", *myPointer);
    printf("Pointer address: %p\n", &myPointer);

    return 0;
}
