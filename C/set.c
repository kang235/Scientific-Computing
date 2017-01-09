// set.c
#include <stdlib.h>
#include <stdbool.h>
typedef struct Node{
   int value;
   struct Node *next;} Node;
typedef struct set{
   int size;
   Node **first;} Set;  // array of Node *
Set *Set_new(int size){
   Set *set = (Set *)malloc(sizeof(Set));
   set->size = size;
   set->first = (Node **)calloc(size, sizeof(Node *));
   return set;}
void Set_delete(Set *set){
   for (int i = 0; i < set->size; i++){
      Node *node = set->first[i];
      while (node != NULL){
         Node *nextnode = node->next;
         free(node);
         node = nextnode;}}
   free(set->first);
   free(set);}
void Set_add(Set *set, int element){
   int index = element % set->size;  // hash function
   bool found = false;
   Node *node = set->first[index];
   while (!found && node != NULL)
      if (node->value == element)
         found = true;
      else
         node = node->next;
   if (!found){
      Node *node = (Node *)malloc(sizeof(Node));
      node->value = element;
      node->next = set->first[index];
      set->first[index] = node;}}
bool Set_has_element(Set *set, int element){
   int index = element % set->size;
   bool found = false;
   Node *node = set->first[index];
   while (!found && node != NULL)
      if (node->value == element)
         found = true;
      else
         node = node->next;
   return found;}
