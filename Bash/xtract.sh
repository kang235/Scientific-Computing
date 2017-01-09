#!/bin/bash
grep '#' $1 > "C_$1"
echo "extracting # lines from $1"
