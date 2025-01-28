import os
import subprocess
def crawl(path, results=None):
    if results is None:
        results = []
    if os.path.isfile(path):
        if path.endswith(".md"):
            tags = subprocess.run(
        ["python", "tokenizer.py", path],
        capture_output=True,
        text=True
            ).stdout.strip()
            # if tags != None:
            subprocess.run(["python", "tag_factory.py", tags])
            return {"title": os.path.basename(path).split(".")[0], "tags": tags}
            
        
        return None
        
    if os.path.isdir(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            result = crawl(item_path)
            if result:
                results.append(result)
    
    return results
print(crawl("/home/belief/Documents/MathUSE"))