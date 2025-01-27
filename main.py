import json
import subprocess
import os
if not os.path.exists("data"):
    os.mkdir("data")
    subprocess.run(["python", "onboarding.py"])
with open('data/personal.json') as f:
    personal = json.load(f)
subprocess.run(["python", "streak.py"])
for thing in personal:
    print(thing+":\t"+personal[thing])
while True:
    print("> ", end="")
    prompt = input()
    if prompt == "exit":
        break
    if prompt == "help":
        print("add: add a new entry")
        print("log: your log")
        print("delete: delete an entry by ID")
        print("exit: exit")
        continue
    if prompt == "add":
        subprocess.run(["python", "crawler.py"])