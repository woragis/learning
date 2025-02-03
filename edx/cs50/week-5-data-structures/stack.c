#include <stdio.h>
#include <stdlib.h>

typedef struct _stack
{
    int arr[10];
    int top;
}
stack;

int main(void)
{
    stack myStack;
    push(&myStack, 4);
    push(&myStack, 5);
    push(&myStack, 8);
    push(&myStack, 12);
    push(&myStack, 20);
    push(&myStack, 21);
    pop(&myStack);
}

void push(stack* s, int data) {}

void pop(stack* s) {}
