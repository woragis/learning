#include <stdio.h>

void copyStr(char *from, char *to);
int strLength(char *ptr);

int main()
{
    char my_name[] = "Jezreel de Andrade";
    char name_2[50];
    copyStr(my_name, name_2);
    printf("My name: %s\n", my_name);
    printf("Other name: %s\n", name_2);
    strLength("My ");

    return 0;
}

void copyStr(char *from, char *to)
{
    // While *from != '\0'
    while (*from)
        *to++ = *from++;
    // The ++ is added on statement end
    // like this:
    // *to = *from
    // then:
    // *to++; *from++;

    *to = '\0';
}

int strLength(char *ptr)
{
    char *start = ptr;
    printf("Ptr %p\n", ptr);
    printf("Start %p\n", ptr);
    while (*start)
    {
        printf("start: %p\t", start);
        printf("ptr: %p\n", ptr);
        start++;
    }

    printf("End %p\n", &start);
    printf("Calculus: '%p' - '%p' = '%p'\n", &ptr, &start, &start - &ptr);

    return *start - *ptr;
}