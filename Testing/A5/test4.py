#!/usr/bin/env python 
# test4.py

from subprocess import call

content = """proc 1, time = 0.003
proc 2, time = 0.000
proc 3, time = 0.000
0 0 0 0
1 0 0 1
2 0 1 1
3 1 1 1
4 0 0 2
5 0 1 2
6 1 1 2
8 0 2 2
9 1 2 2
12 2 2 2
proc 0, time = 0.001
proc 3, time = 0.000
proc 2, time = 0.001
proc 1, time = 0.001
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
proc 0, time = 0.018
proc 1, time = 0.001
proc 3, time = 0.000
proc 2, time = 0.000
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
16 0 0 4
17 0 1 4
17 2 2 3
18 0 3 3
18 1 1 4
19 1 3 3
20 0 2 4
21 1 2 4
22 2 3 3
24 2 2 4
25 0 3 4
26 1 3 4
27 3 3 3
29 2 3 4
32 0 4 4
33 1 4 4
34 3 3 4
36 2 4 4
41 3 4 4
48 4 4 4
proc 0, time = 0.001
"""
print("Example output is:")
print(content)
print("Your output is:")
for i in range(2,5):
    call("mpiexec -n 4 python sortMPI.py i", shell=True)

