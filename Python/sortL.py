#!/usr/bin/env python #sortL.py

#The problem is inspired by a fast N-body method that reduces the
#problem to a lattice.) Given a nonnegative integer argument n, create a text file listing all
#integer triples (i, j, k), 0 ≤ i ≤ j ≤ k ≤ n, ordering them based on the distance squared
#i^2 + j^2 + k^2 from the origin. For triples at the same distance, order them lexicographically.
#Implemented with list
import sys
n = int(sys.argv[1])
r = []

for i in range(n+1):
  for j in range(n+1):
    for k in range(n+1):
	  if i <= j and j <= k:
		l = [i*i+j*j+k*k, i, j, k]
		r.append(l)
r.sort()
ofile = open('d2ijkL.txt', 'w')
for e in r:
  ofile.write(str(e[0])+ ' ' + str(e[1]) + ' ' + str(e[2]) + ' ' + str(e[3])+ '\n')
ofile.close()

