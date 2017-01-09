#!/usr/bin/env python
# test1.py

from run_ import run_

content="""
nprocs =  5, nparts =  5, time = 0.046
0 0 0 0
1 0 0 1
2 0 1 1
3 1 1 1
4 0 0 2
5 0 1 2
6 1 1 2
8 0 2 2
9 0 0 3
9 1 2 2
10 0 1 3
11 1 1 3
12 2 2 2
13 0 2 3
14 1 2 3
17 2 2 3
18 0 3 3
19 1 3 3
22 2 3 3
27 3 3 3
nprocs =  1, nparts =  1, time = 4.919
nprocs =  2, nparts =  2, time = 1.449
nprocs =  4, nparts =  4, time = 0.719
nprocs =  8, nparts =  8, time = 1.041
nprocs = 16, nparts = 16, time = 0.696
nprocs = 32, nparts = 32, time = 0.257
"""
print("Example output is:")
print(content)
print("Your output is:")
run_("python runP2P.py")
