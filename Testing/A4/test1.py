#!/usr/bin/env python  # test1.py
import numpy as np
def main():
    result = """true
true
true
true
true
true
true
Time for C is 0.005509
true
true
true
true
true
true
true
Time for C is 0.004149
Time for vectorized Python is 0.005240917205810547
"""
    print("The desired output is:")
    print(result)
    print("Your output is:")
    run_("gcc -std=gnu11 -fopenmp testqr.c qr.c -o testqr -lm")
    run_("./testqr")
    k = np.arange(100.)
    x = np.pi*np.arange(98.)/98.
    a = np.cos(np.outer(k, x))
    import time
    begin = time.time()
    q = a.copy()
    r = np.zeros((98, 98))
    mgs(q, r)
    end = time.time()
    print("Time for vectorized Python is", end - begin)
    # the following code violates the stricture on side effects in Python
def mgs(q, r):
    r[0,0] = np.sqrt(np.dot(q[:,0], q[:,0]))
    if r[0,0] == 0.: return "linearly dependent"
    q[:,0] /= r[0,0]
    message = None
    if q.shape[1] > 1:
        r[1:,0] = 0.
        r[0,1:] = np.dot(q[:,0], q[:,1:])
        q[:,1:] -= np.outer(q[:,0], r[0,1:])
        msg = mgs(q[:,1:], r[1:,1:])
    return message
from subprocess import Popen, PIPE
import shlex
def run_(cmd, input=None):
    p = Popen(shlex.split(cmd), stdin=PIPE, stderr=PIPE,
              universal_newlines=True)
    err = p.communicate(input=input)[1]
    if err: print(err)
    if p.returncode < 0:
        print("return code =", - p.returncode)
        if not err: print('Enter "'+cmd+'" to see error message.')
        exit(1)
    elif p.returncode > 0:
        print("return code =", p.returncode)
if __name__ == "__main__":
    main()
