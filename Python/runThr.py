#!/usr/bin/env python
# runThr.py
from subprocess import run, PIPE
from os import sep, curdir, environ
import shlex
from run_ import run_
run_('gcc -std=c99 -fopenmp -lgomp msortThr.c')
environ["OMP_NUM_THREADS"]=str(5)
run_(curdir+sep+'a.out 3')
sorted = open('sorted.txt')
print(sorted.read(), end='')
sorted.close()
for log2p in range(6):
    environ["OMP_NUM_THREADS"]=str(2**log2p)
    run_(curdir+sep+'a.out 75')
