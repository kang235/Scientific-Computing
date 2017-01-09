#!/usr/bin/env python
# test1.py
import numpy as np
from cholM import cholR

n = 13
A = 1./np.add.outer(np.arange(n), np.arange(1., n+1))
G = cholR(A)
res = np.amax(abs(G @ G.T - A[:n,:n]))
print("Residual for n = %d is" % n, res)
if res<10**(-15):
    print("test1 is passed.")
else:
    print("test1 is failed. Residual is too large")