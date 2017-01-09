#!/usr/bin/env python
# test3.py
import numpy as np
from cholM import chol

n = 13
A = 1./np.add.outer(np.arange(n), np.arange(1., n+1))
G = chol(A)
res = np.amax(abs(G @ G.T - A[:n,:n]))
print("Residual for n = %d is" % n, res)
if res<10**(-15):
    print("test3 is passed.")
else:
    print("test3 is failed. Residual is too large")