#!/usr/bin/env python # wc.py
import sys
ifile = open(sys.argv[1])
nline = 0
nword = 0
nchar = 0
for line in ifile:
	nchar += len(line)
	nword += len(line.split())	
	nline += 1
ifile.close()
print nline, nword, nchar
