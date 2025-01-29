import json
import os
import wsgiref

with open("data/personal.json", "r+") as f:
    new_data = json.load(f)
    new_data["Score"] = "0"
    f.seek(0)
    json.dump(new_data, f, indent=4)
    f.truncate()
with open("data/logs.json", "w") as f:
    json.dump({"Calendar": [], "Ignored": []}, f, indent=4)
with open("data/tags.json", "w") as f:
    json.dump({}, f)
