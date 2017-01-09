#!/usr/bin/env python  # test2.py
from test1 import run_
result = """result is 5
result is 1
result is 100
result is 8
"""
print("The desired output is:")
print(result)
print("Your output is:")
run_("gcc -std=c11 calc.c astack.c -o calc")
run_("./calc", input=
"""8 4 2 1 - - -
   8 4 - 2 - 1 -
   +100 -99 - +99 -
   8
""")
