typedef struct node
{
    char* phrase;
    struct node *next;
}
node;

int unload(node *list);
void u(node *list);

int main(int argc, char* argv)
{
    node *list = '\0';
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
