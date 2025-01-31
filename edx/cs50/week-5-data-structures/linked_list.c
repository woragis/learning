// #include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    char* phrase;
    struct node *next;
}
node;

#define LIST_SIZE 2

int unload(node *list);
void visualizer(node *list);

int main(void)
{
    node *list = NULL;

    // Add items to list
    for (int i = 0; i < LIST_SIZE; i++)
    {
        char* phrase = get_string("Enter a new phrase: ");

        // TODO: add phrase to new node in list
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return 1;
        }

        n->phrase = phrase;
        // n->next = NULL;
        n->next = list;
        list = n;

        // Visualize list after adding a node
        visualizer(list);
    }

    if (unload(list) == 0)
    {
        printf("Error freeing the list.\n");
        return 1;
    }

    printf("Freed the list.\n");
    return 0;
}

int unload(node *list)
{
    // TODO: Free all allocated nodes
    node *ptr = list;

    while (ptr != NULL)
    {
        ptr = list->next;
        free(list);
        list = ptr;
    }

    return 1;
}

void visualize(node *list)
{
    node *n = malloc(sizeof(node));
    n->phrase="Hi!";
    n->next='\0';
    list = n;

    node *n = malloc(sizeof(node));
    n->phrase="Hey!";
    n->next=list;
    list = n;

    node *ptr = list->next;
    free(list);

    list = ptr;
    ptr = list->next;
    free(list);

    list = ptr;
    ptr = list->next;

    return 0;
}
