#!/usr/bin/env python
# runP2P.py
from os import curdir, sep
from run_ import run_
run_(curdir+sep+'msortP2P.py 3')
sorted = open('sorted.txt')
print(sorted.read(), end='')
sorted.close()
for log2p in range(6):
    p = str(2**log2p)
    run_('mpiexec -n %d python '%2**log2p+curdir+sep+'msortP2P.py 25')

