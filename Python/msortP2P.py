#!/usr/bin/env python
import sys, time
import numpy as np
from mpi4py import MPI

if len(sys.argv) == 1: print('Usage: sort.py <n>'); sys.exit()
M = int(sys.argv[1])
begin = time.time()
cw = MPI.COMM_WORLD
p = cw.Get_size()
#assert p > 1
rank = cw.Get_rank()
sent = 0
Ntot = (M+1)*(M+2)*(M+3)//6  # length of list
# partition the list among p sublists and sort each of them
ls = [None]*p
# construct sublist
N = [Ntot//p]*p
if rank < Ntot % p: N[rank] += 1
#print('rank %d, N %d' % (rank, N[rank]))
lsr = ls[rank] = np.empty((N[rank], 4), 'int32')
n = 0
for k in range(M+1):
    for j in range(0, k+1):
        for i in range(0, j+1):
            if n % p == rank: lsr[n//p] = (i*i+j*j+k*k, i, j, k)
            n += 1
# do an insertion sort
for n in range(1, N[rank]):
    m = n
    while m > 0 and tuple(lsr[m-1]) > tuple(lsr[m]):
        lsr[m-1], lsr[m] = lsr[m], lsr[m-1].copy()
        m -= 1
def merge(a, b):
    Na, Nb = len(a), len(b)
    c = np.empty((Na + Nb, 4), 'int32')
    na = nb = 0
    for n in range(Na + Nb):
        if nb == Nb or na < Na and tuple(b[nb]) > tuple(a[na]):
            c[n] = a[na]
            na += 1
        else:
            c[n] = b[nb]
            nb += 1
    return c
h = (p-1)//2+1
prevh = p
while sent == 0:
    if rank >= h:
        #print('%d is sending data to %d' % (rank, rank - h))
        cw.send(lsr, dest = rank - h, tag = 0) #send
        sent = 1
    if rank + h < prevh:
        #print('%d is receiving data from %d' % (rank, rank + h))
        srcdata = cw.recv(source = rank + h, tag = 0) #receive
        lsr = merge(lsr, srcdata)
        #print(lsr)
    if h == 1: break
    prevh = h
    h = (h-1)//2+1
end = time.time()
if rank == 0:
    print('nprocs = %2d, nparts = %2d, time = %.3f' % (p, p, end - begin))
    sorted = open('sorted.txt', 'w')
    for n in range(Ntot):
        #print('%d %d %d %d\n' % tuple(lsr[n]), end='')
        sorted.write('%d %d %d %d\n' % tuple(lsr[n]))
    sorted.close()

