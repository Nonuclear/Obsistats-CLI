import sys

if len(sys.argv) < 2:
    print("Please specify a file to tokenize")
    exit()
argument = sys.argv[1]

def tokenize(file):
    with open(file, "r") as f:
        line = f.readline()
        tags = []
        temp = ""
        record = 0
        mode = False
        for char in line:
            record += 1
            if char == "#":
                mode = True
            if char == " " and mode:
                tags.append(temp)
                temp = ""
                mode = False
            if char == "\n":
                tags.append(temp)
                return tags
            if record == len(line):
                temp += char
                tags.append(temp)
                return tags
            if mode:
                temp += char
if __name__ == "__main__":
    print(tokenize(argument))