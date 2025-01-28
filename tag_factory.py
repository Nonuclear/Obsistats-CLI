import json
import os
import sys
import subprocess

tags = sys.argv[1][1:-1].replace("'", "").replace('#', "").split(",")
if __name__ == "__main__":

    # for tag in tags:
    print(tags)