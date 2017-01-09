#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct Node {
        void * value;
        struct Node *next;
} Node;

typedef struct Stack {
        Node *top;
} Stack;

Stack *Stack_new(void) {
        Stack *stack = (Stack *) malloc (sizeof(Stack));
        stack->top = NULL;
        return stack;
}

void Stack_push(Stack *stack, void * a) {
        Node *node = (Node *) malloc (sizeof(Node));
        node->value = a;
        node->next = stack->top;
        stack->top = node;
}

void *Stack_pop(Stack *stack) {
        Node *node = stack->top;
        void *a = node->value;
        stack->top = node->next;
        free(node);
        return a;
}

bool Stack_isempty(Stack *stack) {
        return (stack->top == NULL);
}

void *Stack_top(Stack *stack) {
        return stack->top->value;
}

void Stack_delete(Stack *stack) {
        while (!Stack_isempty()) {
                Node *node = stack->top;
                stack->top = node->next;
                free(node);
        }
        free(stack);
}

