import os
import sys
import subprocess
import json

with open("data/personal.json", "r+") as f:
    personal = json.load(f)
    f.close()
with open("data/logs.json", "r+") as f:
    logs = json.load(f)
    f.close()
def crawl(path, results=None):
    if results is None:
        results = []
    if os.path.isfile(path):
        if (path.endswith(".md") and not os.path.basename(path) in logs["Ignored"]): 
            logs["Ignored"].append(os.path.basename(path))
            tags = subprocess.run(
        ["python", "tokenizer.py", path],
        capture_output=True,
        text=True
            ).stdout.strip()
            subprocess.run(["python", "tag_factory.py", tags, os.path.basename(path).split(".")[0], str(personal["Score"])])
            with open(str(path), "a") as md:
                md.write('\n')
                md.write(str(personal["Score"]))
                md.close()
            personal["Score"] = str(int(personal["Score"]) + 1)
            with open("data/personal.json", "r+") as f:
                f.seek(0)
                json.dump(personal, f, indent=4)
                f.truncate()
            with open("data/logs.json", "r+") as f:
                f.seek(0)
                json.dump(logs, f, indent=4)
                f.truncate()
            print(os.path.basename(path)+" was added")
            return {"title": os.path.basename(path).split(".")[0], "tags": tags}
            
        
        return None
 
    if os.path.isdir(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            result = crawl(item_path)
            if result:
                results.append(result)
    
    return results
crawl(sys.argv[1])