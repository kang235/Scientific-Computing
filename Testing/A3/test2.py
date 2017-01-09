#!/usr/bin/env python
# test2.py
import numpy as np
from cholM import cholR

n = 14
A = 1./np.add.outer(np.arange(n), np.arange(1., n+1))
try:
    G = cholR(A[:n,:n])
    print("No error message when the matrix is not positive definite")
    print("test2 is failed")
except Exception as inst:
    print(inst)
    print("test2 is passed")


