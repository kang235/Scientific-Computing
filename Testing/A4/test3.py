#!/usr/bin/env python  # test3.py
from test1 import run_
result = """true
true
"""
print("The desired output is:")
print(result)
print("Your output is:")
run_("gcc -std=c99 teststk.c lstack.c -o teststk")
run_("./teststk")
