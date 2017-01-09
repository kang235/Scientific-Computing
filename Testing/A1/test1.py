#!/usr/bin/env python  # test1.py
from subprocess import call
import shlex
from os import remove

content = """
#
aaa
bbb
#ccc
d d d
eee #

ff #f#
"""
fid = open('temp', 'w')
fid.write(content)
fid.close()

print("The desired output is:")
spr = """extracting # lines from temp
#
#ccc
eee #
ff #f#
"""
print(spr)
print("\nYour output is:")
fid = open('l1', 'w')
fid.close()
call("./xtract.sh temp > l1", shell=True)
fid = open('C_temp', 'r')
content = fid.read()
fid.close()
fid = open('l1', 'r')
l = fid.read()
fid.close()
content = l + content
print(content)
if spr == content:
    print("test1 is passed.")
else:
    print("test1 is failed.")

remove('temp')
remove('C_temp')
