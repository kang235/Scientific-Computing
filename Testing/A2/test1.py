#!/usr/bin/env python  # test1.py
import subprocess, os, sys, shutil

if "Sandbox" in os.listdir("."):
    shutil.rmtree("Sandbox")
join = os.path.join
os.mkdir("Sandbox")
os.chdir("Sandbox")
subprocess.call(join(os.pardir,"rmdir.py"))
os.chdir(os.pardir)

if "Sandbox" in os.listdir("."):
    print("'Sandbox' is not removed.")
    print("test1 is passed.")
    shutil.rmtree("Sandbox")
else:
    print("'Sandbox' is removed.")
    print("\ntest2 is failed")


