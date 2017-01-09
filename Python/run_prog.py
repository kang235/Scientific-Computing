#!/usr/bin/env python 

import sys
import os
from runm import run_
from subprocess import Popen, PIPE
import numpy as np

retcode = run_('gcc -std=c99 ssprog.c subset.c set.c')
if retcode != 0:  exit("Failed to compile c code!")

n = 3000
m = 300
nss = 20

proc = Popen('./a.out', stdin = PIPE, stdout = PIPE, stderr = PIPE)
odata, edata = proc.communicate(np.array([n, m, nss], 'int32').tobytes())
ss = np.frombuffer(odata, 'int32')

for iss in range(nss):
    count = 0
    for j in range(m):
        index = iss*m + j
        if n/3 <= ss[index] and ss[index] < 2*n/3:
            count += 1
    print('%d ' % count, end = "")
print('\b\n')

os.remove('a.out')
