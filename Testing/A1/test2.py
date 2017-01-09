#!/usr/bin/env python  # test2.py
from subprocess import call
import shlex
from os import remove
import glob

for file in glob.glob("*.bak"):
    remove(file)

filenameall = ""
filenamebak = ["" for i in range(5)];
for i in range(5):
    filename = "temp" + str(i)
    filenameall = filenameall + filename + " "
    filenamebak[i] = filename + ".bak"
    fid = open(filename, 'w')
    fid.close()
call("./backup.sh " + filenameall, shell = True)
filenamebak2 = glob.glob("*.bak")
filenamebak.sort()
filenamebak2.sort()
print("The desired output is:")
print(filenamebak)
print("\nYour output is:")
print(filenamebak2)
if filenamebak == filenamebak2:
     print("\ntest2 is passed")
else:
     print("\ntest2 is failed")

for file in glob.glob("temp*"):
    remove(file)
