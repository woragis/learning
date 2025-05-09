#include <stdio.h>
#include <stdlib.h>

int main()
{
    int my_age = 999;
    const int *pmy_age = &my_age;
    printf("My age: %d\n", my_age);
    printf("Age pointer: %u\n", pmy_age);
    printf("Age address: %u\n", &my_age);
    my_age = 800;
    printf("My age: %d\n", my_age);
    printf("Age pointer: %u\n", pmy_age);
    printf("Age address: %u\n", &my_age);
}