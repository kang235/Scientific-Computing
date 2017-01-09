/* astack.c */
#include <stdio.h>
#include <stdlib.h>
typedef struct Stack {
    void *obj[20];
    int n;
} Stack;
Stack *Stack_new(void) {
    Stack *stack = (Stack *)malloc(sizeof(Stack));
    stack->n = 0;
    return stack;}
void Stack_push(Stack *stack, void *obj) {
    if (stack->n == 20) {
        fprintf(stderr, "Stack capacity exceeded.\n");
        exit;}
    stack->obj[stack->n] = obj;
    stack->n++;}
void *Stack_pop(Stack *stack) {
    if (stack->n == 0) {
        fprintf(stderr, "Cannot pop empty stack.\n");
        exit;}
    stack->n--;
    return stack->obj[stack->n];}
void Stack_delete(Stack *stack) {
    free(stack);}
