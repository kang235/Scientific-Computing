// subset.c
#include <stdlib.h>
#include <stdbool.h>
typedef struct Set Set;
Set *Set_new(int size);
void Set_add(Set *set, int element);
bool Set_has_element(Set *set, int element);
void Set_delete(Set *set);
void subset(int n, int m, int nss, int (*ss)[m]) {
   srand(2016);
   for (int iss = 0; iss < nss; iss++) {
      Set *chosen = Set_new(m);
      int denom = RAND_MAX/n;
      int j = 0;
      while (j < m){
         int k = rand()/denom;
         while (k >= n) k = rand()/denom;
         if (!Set_has_element(chosen, k)){
            Set_add(chosen, k);
            ss[iss][j] = k;
            j++;}}
      Set_delete(chosen);}}
