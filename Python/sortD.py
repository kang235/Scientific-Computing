#!/usr/bin/env python #sortD.py

#The problem is inspired by a fast N-body method that reduces the
#problem to a lattice.) Given a nonnegative integer argument n, create a text file listing all
#integer triples (i, j, k), 0 ≤ i ≤ j ≤ k ≤ n, ordering them based on the distance squared
#i^2 + j^2 + k^2 from the origin. For triples at the same distance, order them lexicographically.
#Implemented with dictionary.
import sys
n = int(sys.argv[1])
r = {}

for i in range(n+1):
  for j in range(n+1):
    for k in range(n+1):
	  if i <= j and j <= k:
	    index = i*i + j*j + k*k
	    if index in r:
	      r[index] += [(i, j, k)]
	    else:	  	
	      r[index] = [(i, j, k)]
ofile = open('d2ijkD.txt', 'w')
for e in r:
  for l in r[e]:
    ofile.write(str(e) + ' ')
    ofile.write(str(l[0]) + ' ')
    ofile.write(str(l[1]) + ' ')
    ofile.write(str(l[2]) + '\n')
ofile.close()

