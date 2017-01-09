#!/usr/bin/env python
# run_subset.py
code = r'''
#include <stdio.h>
#include <dlfcn.h>
#include <stdlib.h>
int main(void){
  int n = 3000;
  int m = 300;
  int nss = 20; // number of random subsets
  int ss[nss][m];
  void *so = dlopen("./set.so", RTLD_LAZY);
  if (so == NULL) {
    printf("%s\n", dlerror());
    exit(1);
  }
  typedef void subset_t(int, int, int, int (*)[m]);
  subset_t *subset = (subset_t *)dlsym(so, "subset");
  subset(n, m, nss, ss);
  dlclose(so);
  for (int iss = 0; iss < nss; iss++) {
    int count = 0;
      for (int j = 0; j < m; j++)
        if (n/3 <= ss[iss][j] && ss[iss][j] < 2*n/3) count++;
  printf("%d ", count);}
  printf("\b\n");
  return 0;
}
'''[1:]
import os
from runm import run_
ofile = open('main.c', 'w')
ofile.write(code)
ofile.close()
retcodeO = run_('gcc -std=c99 -fPIC subset.c set.c -c')
retcodeSO = run_('gcc -std=c99 -shared subset.o set.o -o set.so')
retcodeOUT = run_('gcc -std=c99 main.c -ldl')
os.remove('main.c')
if retcodeOUT == 0 and retcodeO == 0 and retcodeSO == 0:
    run_(os.curdir+os.sep+'a.out')
