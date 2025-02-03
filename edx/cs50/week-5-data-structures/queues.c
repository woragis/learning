#include <stdio.h>
#include <stdlib.h>

typedef struct _queue
{
    int arr[10];
    int first;
}
queue;

int main(void)
{
    // enqueue: add a new element to the end of the queue
    // dequeue: remove the oldest element from the front of the queue
    queue myQueue;
}

void enqueue(queue* q, int data) {}

int dequeue(queue* q) {
    return 1;
}
