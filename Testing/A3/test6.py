#!/usr/bin/env python
# test6.py
from subprocess import call
from os import sep, remove

call("gcc -std=c11 sort.c -o sort.exe", shell = True)

fid = open("p3result2.txt", "r")
content = fid.read()
fid.close()
print("The desired output is:")
print(content)

fid = open("temp", "w")
n = 5
call("." + sep + "sort.exe %d" % n, stdout = fid, shell = True)
remove("sort.exe")
fid.close()
fid = open("temp", "r")
file = fid.read().split("\n")[:-1]
d2 = list(map(lambda line: line.split()[0], file))
N = len(d2)
printed = False  # line 0 not printed
mycontent = ""
for i in range(1, N):
    if d2[i] == d2[i-1]:
        if not printed:
            mycontent = mycontent + "\n"
            mycontent = mycontent + file[i-1] + "\n"
        mycontent = mycontent + file[i]+ "\n"
        printed = True  # line i printed
    else:
        printed = False  # line i not printed

print("Your output is:")
print(mycontent)

if content == mycontent:
    print("test6 is passed.")
else:
    print("test6 is failed.")
remove("temp")