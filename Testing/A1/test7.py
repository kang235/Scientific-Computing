#!/usr/bin/env python  # test7.py
from subprocess import call
import shlex

call("python sortD.py 2", shell = True)
fid = open("d2ijkD.txt", 'r')
content = fid.read()
fid.close()
fid = open("d2ijk_n2.txt", 'r')
contenttrue = fid.read()
fid.close()
print("The desired output is:")
print(contenttrue)
print("Your output is:")
print(content)

if contenttrue == content:
    print("test7 is passed")
else:
    print("test7 is failed")
