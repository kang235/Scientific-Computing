/* Postfix expression */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_CHAR 80

typedef struct Stack Stack;
Stack *Stack_new(void);
void Stack_push(Stack *stack, void *obj);
void *Stack_pop(Stack *stack);
void Stack_delete(Stack *stack);

int main(int argc, char *argv[]) {
	char str[MAX_CHAR];
	Stack *stack = Stack_new();
	while (fgets(str, MAX_CHAR, stdin) != NULL) { 
		if (str[0] != '\n') {
			for (char *p = strtok(str, " \n"); p != NULL; p = strtok(NULL, " \n")) {
				int *i = (void *) malloc (sizeof(int));
				if (strlen(p) == 1 && p[0] == '-') {
					int *a = Stack_pop(stack);
					int *b = Stack_pop(stack);
					*i = *b - *a;
					Stack_push(stack, i);
					free(a);
					free(b); 
				}	
				else {
					*i = atoi(p);
					//printf("%d\n", *i);
					Stack_push(stack, i);	
       				}
			}
			int *res = Stack_pop(stack);
			printf("result is %d\n", *res);
			free(res);	
		}
	}
	Stack_delete(stack);
	return 0;
}
