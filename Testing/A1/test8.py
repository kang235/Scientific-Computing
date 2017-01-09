#!/usr/bin/env python  # test8.py
from subprocess import call
import shlex

call("python sortD.py 5", shell = True)
fid = open("d2ijkD.txt", 'r')
content = fid.read()
fid.close()
fid = open("d2ijk_n5.txt", 'r')
contenttrue = fid.read()
fid.close()
print("The desired output is:")
print(contenttrue)
print("Your output is:")
print(content)

if contenttrue == content:
    print("test8 is passed")
else:
    print("test8 is failed")
