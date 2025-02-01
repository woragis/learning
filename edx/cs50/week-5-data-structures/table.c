// #include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int hash(char* phrase);

int main(void)
{

}

int hash(char* phrase)
{
    return phrase[0] - 'A';
}