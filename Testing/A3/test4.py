#!/usr/bin/env python
# test4.py
import numpy as np
from cholM import chol

n = 14
A = 1./np.add.outer(np.arange(n), np.arange(1., n+1))
try:
    G = chol(A[:n,:n])
    print("No error message when the matrix is not positive definite")
    print("test4 is failed")
except Exception as inst:
    print(inst)
    print("test4 is passed")


