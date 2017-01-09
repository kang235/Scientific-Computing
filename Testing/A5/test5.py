#!/usr/bin/env python 
# test4.py

from subprocess import call
content = """proc 0, time = 6.014
proc 1, time = 1.592
proc 2, time = 1.584
proc 3, time = 1.610
proc 0, time = 1.688
"""

print("Example output is:")
print(content)
print("Your output is:")
call("python sort.py 32 > /dev/null", shell=True)
call("mpiexec -n 4 python sortMPI.py 32 > /dev/null", shell=True)


