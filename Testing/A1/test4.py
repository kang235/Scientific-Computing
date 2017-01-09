#!/usr/bin/env python  # test4.py
from subprocess import call
import shlex
from os import remove

content = """
abc def g       h
  i 
  jklmn  op q

r


          
stuvwx

y z"""

fid = open("temp", 'w')
fid.write(content)
fid.close()
call("python wc.py temp > wcout", shell = True)

fid = open("wcout", 'r')
wcout = fid.read()
fid.close()
print("The desired output is:")
wctrue = "12 12 65\n"
print(wctrue)
print("Your output is:")
print(wcout)

if wcout == wctrue:
    print("test4 is passed")
else:
    print("test4 is failed")

remove("temp")
remove("wcout")
