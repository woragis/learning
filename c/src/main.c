#include <stdio.h>

int compare_string(char *string1, char *string2);
void show_help();
void swap(int *a, int *b);

int main(int argc, char *argv[])
{
    int a = 20;
    int b = 80;
    swap(&a, &b);

    printf("Hello, World!\n");
    printf("Count of arguments: %d\n", argc);
    for (int i = 0; i < argc; i++)
    {
        printf("Argument %d: %s\n", i, argv[i]);
        if (compare_string("help", argv[i]) == 0)
        {
            printf("This person needs help!\n");
            show_help();
        }
    }
    return 0;
}

int compare_string(char *string1, char *string2)
{
    int i = 0;
    char char1 = string1[i];
    char char2 = string2[i];
    while (char1 != '\0' && char2 != '\0')
    {
        if (char1 != char2)
        {
            return 1;
        }
        i++;
        char1 = string1[i];
        char2 = string2[i];
    }
    return 0;
}

void show_help()
{
    printf("===============================\n");
    printf("-----How to use the program----\n");
    printf("\n");
    printf("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
    printf("----How to build the program---\n");
    printf("-------  make src/main  -------\n");
    printf("\n");
    printf("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
    printf("---How to Execute the program--\n");
    printf("--------  ./src/main  ---------\n");
    printf("===============================\n");
    printf("\n");

    return;
}

void help()
{
    printf("[0 or ttt] - Tic Tac Toe\n");
    printf("[1 or sdk] - Sudoku\n");
    printf("[2 or h] - Help\n");
}

void swap(int *a, int *b)
{
    // Common swap
    // printf("Previous result:\n");
    // printf("A: %d  B: %d\n", *a, *b);
    // int temp = *a;
    // *a = *b;
    // *b = temp;
    // printf("After result:\n");
    // printf("A: %d  B: %d\n", *a, *b);
    printf("Previous result:\n");
    printf("A: %d  B: %d\n", *a, *b);
    *a = *a ^ *b;
    *b = *b ^ *a;
    *a = *a ^ *b;
    printf("After result:\n");
    printf("A: %d  B: %d\n", *a, *b);
}
