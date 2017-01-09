#!/usr/bin/env python  # test6.py
from subprocess import call
import shlex

call("python sortL.py 5", shell = True)
fid = open("d2ijkL.txt", 'r')
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
    print("test6 is passed")
else:
    print("test6 is failed")
