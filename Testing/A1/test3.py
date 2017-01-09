#!/usr/bin/env python 
from subprocess import call
from os import remove
import glob
from sys import platform

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
fid = open("temp2.bak", 'w')
fid.close()
call("echo 'y' | ./backup.sh " + filenameall + "2> out", shell=True)
filenamebak2 = glob.glob("*.bak")
filenamebak2.sort()
filenamebak.sort()
if platform == "linux2":
	trueoutput = "cp: overwrite `temp2.bak'? " + "\n" + " ".join(filenamebak)
else:
	trueoutput = "overwrite temp2.bak? (y/n [n]) " + "\n" + " ".join(filenamebak)
print("The desired output is:")
print(trueoutput)
print("\nYour output is:")
fid = open("out", 'r')
content = fid.read() + "\n" + " ".join(filenamebak2)
fid.close()
print(content)

if trueoutput == content:
    print("\ntest3 is passed")
else:
    print("\ntest3 is failed")

for file in glob.glob("temp*"):
    remove(file)