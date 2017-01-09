#!/usr/bin/env python

#removes those directories from the current
#working directory that contain nothing except (possibly) empty directories—recursively
import os

cwd = os.getcwd()
l = os.walk(cwd, False)
for i in l:
	dirs = os.listdir(i[0])
	if(len(dirs) == 0 and i[0] != cwd):
		os.rmdir(i[0])
		print('removing %s' % os.path.relpath(i[0], cwd))
