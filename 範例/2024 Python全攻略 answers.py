import re
import os

with open("research.txt", encoding="utf8") as f:
    text = f.read()
    x = re.findall(r"\([A-Za-z0-9\s]+, \d{4,}\)", text)
    print(x)

result = []


def search(st):
    r = re.findall(r'\d{3}-\d{3}-\d{4}', st)
    if r:
        for number in r:
            result.append(number)


for folder, subfolders, files in os.walk("Employee"):
    for f in files:
        with open(os.path.join(folder, f), encoding="utf8") as my_file:
            text = my_file.read()
            search(text)

print(result)
