#!/usr/bin/env python  # test3.py
import subprocess, os, sys
from polynomial import *

fid = open("polynomial.dat", "r")
content = fid.read()
fid.close()
print("The desired output is:")
print(content)
print("\nYour output is:")

fid = open("temp", "w")
old_stdout = sys.stdout
sys.stdout = fid
p = Polynomial([-2, 1, 0])
print("degree of " + str(p) + " is " + str(p.deg()))
T = [None]*12
T[0] = Polynomial([1])
print(T[0])
T[1] = Polynomial([0, 1])
print(T[1])
two_x = Polynomial([0, 2])
for k in range(2, 12):
    T[k] = two_x * T[k-1] - T[k-2]
    print(T[k])
T3oT2 = T[3](T[2])
print(T3oT2)
c0_5 = Polynomial([0.5])
print(T3oT2(c0_5))
print(Polynomial()*p)
fid.close()
fid = open("temp", "r")
mycontent = fid.read()
fid.close()
sys.stdout = old_stdout
print(mycontent)
if content.split() == mycontent.split():
    print("\ntest3 is passed")
else:
    print("\ntest3 is failed")
os.remove("temp")






