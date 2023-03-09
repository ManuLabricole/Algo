import json
import os
import random
path = os.getcwd()


def mixGame(inputList: list) -> list:

    random.shuffle(inputList)


def importFile(source: str) -> dict:

    sourceDir = "Algo/"+source
    f = open(os.path.join(path, sourceDir))
    data = json.load(f)
    f.close()

    return data


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
    # Initialization of suit list
    lenghtFamily = 13
    diamondsList = [0 for i in range(lenghtFamily)]
    spadesList = [0 for i in range(lenghtFamily)]
    heartsList = [0 for i in range(lenghtFamily)]
    clubsList = [0 for i in range(lenghtFamily)]

    print(len(diamondsList))
    cardGame = importFile("card.json")
    mixGame(cardGame)

    return cardGame


game = algoTri()
print(game)
