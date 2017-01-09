#!/usr/bin/env python  # test2.py
import subprocess, os, sys, shutil

if "Sandbox" in os.listdir("."):
    shutil.rmtree("Sandbox")

before = [set(['IL', 'IN', 'ky']),
          set(['Fountain', 'Tippecanoe']),
          set(['attica'])]
after = [set(['IN', 'ky']),
         set(['Fountain']),
         set(['attica'])]
strs = """removing IL
removing IN/Tippecanoe/Dayton
removing IN/Tippecanoe/Lafayette
removing IN/Tippecanoe
"""

print("The desired output is:")
print("before\n", before)
print(strs)
print("after\n", after)

mkfile = lambda f: open(f, "w").close()
join = os.path.join
os.mkdir("Sandbox")
os.chdir("Sandbox")
os.mkdir("IL")
os.mkdir("IN")
os.mkdir(join("IN","Tippecanoe"))
os.mkdir(join("IN","Tippecanoe", "Lafayette"))
os.mkdir(join("IN","Tippecanoe", "Dayton"))
os.mkdir(join("IN","Fountain"))
mkfile(join("IN","Fountain", "attica"))
mkfile("ky")
mybefore = []
mybefore.append(set(os.listdir(".")))
mybefore.append(set(os.listdir("IN")))
mybefore.append(set(os.listdir(join("IN","Fountain"))))
fid = open("temp","w")
subprocess.call(join(os.pardir,"rmdir.py"), stdout = fid)
fid.close()
fid = open("temp","r")
content = fid.read()
fid.close()
os.remove("temp")
myafter = []
myafter.append(set(os.listdir(".")))
myafter.append(set(os.listdir("IN")))
myafter.append(set(os.listdir(join("IN","Fountain"))))
os.chdir(os.pardir)
shutil.rmtree("Sandbox")

print("\nYour output is:")
print("before\n", mybefore)
print(content)
print("after\n", myafter)

if content == strs and before == mybefore and after == myafter:
    print("\ntest2 is passed")
else:
    print("\ntest2 is failed")


