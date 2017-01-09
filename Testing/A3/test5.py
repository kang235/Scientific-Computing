#!/usr/bin/env python
# test5.py
from subprocess import call
from os import sep, remove

call("gcc -std=c11 sort.c -o sort.exe", shell = True)

fid = open("p3result1.txt", "r")
content = fid.read()
fid.close()
print("The desired output is:")
print(content)

fid = open("temp", "w")
for n in [0, 1, 3]:
    call("." + sep + "sort.exe %d" % n, stdout = fid, shell = True)
remove("sort.exe")
fid.close()
fid = open("temp", "r")
mycontent = fid.read()
fid.close()
print("Your output is:")
print(mycontent)

if content == mycontent:
    print("test5 is passed.")
else:
    print("test5 is failed.")
remove("temp")