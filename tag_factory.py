import json
import os
import sys
import subprocess

tags = sys.argv[1][1:-1].replace("'", "").replace('#', "").split(", ")
name = sys.argv[2]
score = int(sys.argv[3])
if __name__ == "__main__":
    with open("data/tags.json", "r+") as f:
        data = json.load(f)
        for tag in tags:
            if tag in data:
                data[tag].append([name, score])
            else:
                data[tag] = [[name, score]]
                
        f.seek(0)
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.truncate()