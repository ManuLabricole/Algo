import json
import os

path = os.getcwd()
# print(currentDir)
print(os.path.join(path, "Algo/card.json"))


def importFile(data: json) -> dict:
    # Opening JSON file
    f = open(os.path.join(path, "Algo/card.json"))
    data = json.load(f)
    f.close()
    return data


print(data)
len(data)
