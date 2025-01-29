import json
import os
import subprocess

def dir_walk(path, list=None):
    if list is None:
        list = []
    for i in os.listdir(path):
        print(i)
        if os.path.isdir(path+"/"+i):
            dir_walk(path+"/"+i, list)
        elif(i.endswith(".md")):
                list.append(i)
    return list

with open('data/logs.json', 'w') as f:
    json.dump({"Calendar": [], "Ignored": []}, f, indent=4)
    f.close()
with open('data/streaks.json', 'w') as f:
    json.dump({}, f, indent=4)
    f.close()
with open('data/tags.json', 'w') as f:
    json.dump({}, f)
    f.close()
    
print("hey, what's your name?")
name = input()
with open('data/personal.json', 'w') as f:
    json.dump({"Name": name, "Day": "1", "Streak": "1", "Score": "0"}, f)

print("Specify a filepath to your obsidian vault")
vault = input()
with open('data/locations.json', "w") as f:
    json.dump({"vaults": [vault]}, f)

if os.listdir(vault) != []:
    print("There's already some data in your vault, would you like to import it? - y/n")
    choice = input()
    # snapshot = {"Calendar": [], "Ignored": []}
    if choice == "y":
        with open("data/locations.json") as f:
            dir = json.load(f)["vaults"][0]
            print("adding files...")
            subprocess.run(["python", "crawler.py", dir])
        # with open("data/logs.json", "r+") as log:

            # day = ["Index: 0"]
            
                # obj = {"Name": i,"Flag": "Legacy", "Pull": "?"} 
                # day.append(obj)
                # print(i, "was added")
            # snapshot["Calendar"].append(day)
            # json.dump(snapshot, log, indent=4, ensure_ascii=False)

    if choice == "n":
        print("alright then...")
        with open("data/locations.json", "r+") as f:
            source = json.load(f)
        with open("data/logs.json", "r+") as log:
            print("ignoring these files:")
            for i in dir_walk(source["vaults"][0]):
                print("-", i)
                source["Ignored"].append(i)
            json.dump(source, log, indent=4, ensure_ascii=False)

print("Done! You can now use the statsCLI!")
