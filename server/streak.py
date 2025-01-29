import json
import os
from datetime import date, datetime, timedelta

today = date.today()
mytime = datetime.now().hour

def streakVisual(num):
    print("Your streak: ")
    if num < 4:
        i = 0
    else:
        i = num - 4
    for n in range(i,num):
        print(n + 1)
        if i < num-1:
            print(" | ")

with open("data/personal.json", "r+") as data:
    data = json.load(data)

with open("data/streaks.json", "r+") as f:
    datemap = json.load(f)
    if datemap == {}:
        datemap[f"{today}"] = True
       
    else:
        datemap_keys = list(datemap.keys())
        last_key = datemap_keys[-1]
        print(last_key)
        gap = (today - datetime.strptime(last_key, "%Y-%m-%d").date()).days
        if gap < 1:
            for i in range(gap):
                datemap[datemap.keys()[-1]] + timedelta(days=1)
    f.seek(0)
    json.dump(datemap, f)
    f.truncate()

    if(mytime < 5):
        print("Good night, "+ data["Name"]+" , isn't it?")
    elif(mytime < 12):
        print("Good morning, "+ data["Name"]+"!")
    elif(mytime < 17):
        print("What a beautiful day to learn something new, "+ data["Name"])
    elif(mytime < 23):
        print("Good afternoon, "+ data["Name"]+"!")
    else:
        print("Late study session, huh?")
    streakVisual(int(data["Streak"]))