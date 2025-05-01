#include <stdio.h>

int compare_string(char *string1, char *string2);

int main(int argc, char *argv[])
{
    printf("Hello, World!\n");
    printf("Count of arguments: %d\n", argc);
    for (int i = 0; i < argc; i++)
    {
        if (compare_string("help", argv[i]) == 0)
        {
            printf("This person needs help!\n");
        }
        printf("Argument %d: %s\n", i, argv[i]);
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