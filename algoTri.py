import json
import os
import random
path = os.getcwd()


def importFile(source: str) -> dict:

    sourceDir = "Algo/"+source
    f = open(os.path.join(path, sourceDir))
    data = json.load(f)
    f.close()

    return data


def mixGame(inputList: list) -> list:

    outputList = random.shuffle(inputList)

    return outputList


cardGame = importFile("card.json")
mixCardGame = mixGame(cardGame)
