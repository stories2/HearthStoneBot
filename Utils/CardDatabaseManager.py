import json
import LogManager
from Settings import DefineManager

cardData = None

def StaticCradDataLoader():
    global cardData

    cardData = None
    with open('Data/CardData.json') as dataFile:
        cardData = json.load(dataFile)

    LogManager.PrintLog("CardDatabaseManager", "StaticCardDataLoader", "card data loaded", DefineManager.LOG_LEVEL_INFO)

def SearchCardById(cardId):
    return