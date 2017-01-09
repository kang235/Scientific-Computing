#!/bin/bash
for i in $*
do 
	cp -i $i $i.bak
done
