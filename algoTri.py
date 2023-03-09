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
    print(inputList)
    outputList = random.shuffle(inputList)

    return outputList


def getValuePerLetter(letter: str) -> int:

    if type(letter) == int:
        return letter
    else:
        if letter == "J":
            return int(11)
        elif letter == "Q":
            return int(12)
        elif letter == "K":
            return int(13)
        elif letter == "A":
            return int(1)


def algoTri():

    return


cardGame = importFile("card.json")
mixCardGame = mixGame(cardGame)

print(mixCardGame)
