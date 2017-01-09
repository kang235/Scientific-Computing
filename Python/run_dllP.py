#!/usr/bin/env python
from runm import run_
from ctypes import c_int
import numpy as np
from numpy.ctypeslib import load_library, ndpointer

retcodeo = run_('gcc -std=c99 -fPIC subset.c set.c -c')
retcodeso = run_('gcc -std=c99 -shared subset.o set.o -o set.so')
if retcodeo != 0 or retcodeso != 0:  exit("Failed to generate dynamic lib!")

n = 3000
m = 300
nss = 20
ss = np.zeros((nss, m), 'int32')

subset = np.ctypeslib.load_library('set.so','.').subset
subset.argtypes = [c_int, c_int, c_int, np.ctypeslib.ndpointer()]
subset.restype = None
subset(n, m, nss, ss)
for iss in range(nss):
    count = 0
    for j in range(m):
        if n/3 <= ss[iss][j] and ss[iss][j] < 2*n/3:
            count += 1
    print('%d ' % count, end = "")
print('\b\n')
