import json
import os
import random
from typing import Type
path = os.getcwd()


def mixGame(inputList: list) -> list:

    random.shuffle(inputList)


def importFile(source: str) -> dict:

    sourceDir = source
    f = open(os.path.join(path, sourceDir))
    data = json.load(f)
    f.close()

    return data


def getCardValue(letter: str) -> int:

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
    nJoker = 3

    orderedDict = {
        "diamonds": [0 for i in range(lenghtFamily)],
        "spades": [0 for i in range(lenghtFamily)],
        "hearts": [0 for i in range(lenghtFamily)],
        "clubs": [0 for i in range(lenghtFamily)],
        "joker": [0 for i in range(nJoker)]
    }

    # print(orderedDict["joker"])
    cardGame = importFile("Algo/sort_algo/card.json")
    mixGame(cardGame)

    for card in cardGame:

        if card["suit"] == "joker":
            orderedDict["joker"].append(card)

        else:
            # print(f"{card['value']} and {card['suit']}")
            value = getCardValue(card["value"])
            if type(value) != int:
                raise Type("wrong type")
            orderedDict[card["suit"]][value-1] = card

    return orderedDict


game = algoTri()
print(game["diamonds"])
