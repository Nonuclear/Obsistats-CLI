import json
import subprocess
import os
if not os.path.exists("data"):
    os.mkdir("data")
    subprocess.run(["python", "onboarding.py"])
with open('data/personal.json') as f:
    personal = json.load(f)
def listing(pile):
    for thing in pile:
        print(thing, pile[thing])
with open('data/locations.json') as f:
    dir = json.load(f)["vaults"][0]
    print(dir)
subprocess.run(["python", "streak.py"])
print()
listing(personal)
subprocess.run(["python", "crawler.py", dir])
print()
while True:
    print("> ", end="")
    prompt = input()
    if prompt == "exit":
        break
    elif prompt == "help":
        print("upd: add a new entry")
        print("list: list your stats")
        print("wipe: delete files info")
        print("exit: exit")
        print("help: show this message")
        continue
    elif prompt == "upd":
        subprocess.run(["python", "crawler.py", dir])
    elif prompt == "wipe":
        subprocess.run(["python", "wipe_data.py"])
    elif prompt == "list":
        listing(personal)
    else:
        print("invalid command, try \'help\'")