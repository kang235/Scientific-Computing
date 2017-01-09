#!/usr/bin/env python  # sort.py

#The problem is inspired by a fast N-body method that reduces the
#problem to a lattice.) Given a nonnegative integer argument n, create a text file listing all
#integer triples (i, j, k), 0 ≤ i ≤ j ≤ k ≤ n, ordering them based on the distance squared
#i^2 + j^2 + k^2 from the origin. For triples at the same distance, order them lexicographically.

import sys, time
import numpy as np
from mpi4py import MPI
if len(sys.argv) == 1: print('Usage: sort.py <n>'); sys.exit()
begin = time.time()

cw = MPI.COMM_WORLD
size = cw.Get_size()
assert size == 4
rank = cw.Get_rank()

M = int(sys.argv[1])
# partition the list among 4 arrays
# how long is each list?
Ntot = (M+1)*(M+2)*(M+3)//6  # must be 6X...
N = [Ntot//4]*4
for r in range(Ntot % 4):
    N[r] += 1

# construct 4 lists
d2 = np.empty((N[rank], 4), 'int32')
n = 0
for k in range(M+1):
    for j in range(0, k+1):
        for i in range(0, j+1):
            nr, r = n//4, n % 4
            if r == rank: d2[nr] = (i*i+j*j+k*k, i, j, k)
            n += 1
# do 4 insertion sorts
for n in range(1, N[rank]):
    p = n
    while p > 0 and tuple(d2[p-1]) > tuple(d2[p]):
        d2[p-1], d2[p] = d2[p], d2[p-1].copy()
        p -= 1

def merge(a, na, b, nb):
    c = np.empty((na + nb, 4), 'int32')
    ia = ib = 0
    for i in range(na + nb):
        if ib == nb or ia < na and tuple(b[ib]) > tuple(a[ia]):
            c[i] = a[ia]
            ia += 1
        else:
            c[i] = b[ib]
            ib += 1
    return c

data = cw.gather(d2, root=0)

if rank == 0:
    m0 = merge(data[0], N[0], data[1], N[1]);
    m1 = merge(data[2], N[2], data[3], N[3])
    arr = merge(m0, len(m0), m1, len(m1))
    for n in range(Ntot):
        print('%d %d %d %d' % tuple(arr[n]))

end = time.time()
sys.stderr.write('proc %d, time = %.3f\n' % (rank, end - begin))
