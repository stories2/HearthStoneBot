import json
import LogManager
from Settings import DefineManager

cardData = None

def StaticCradDataLoader():
    global cardData

    cardData = None
    with open('Data/CardData.json') as dataFile:
        cardData = json.load(dataFile)

    LogManager.PrintLog("CardDatabaseManager", "StaticCardDataLoader", "card data loaded keys: " + ', '.join(cardData.keys()), DefineManager.LOG_LEVEL_INFO)

def SearchCardById(cardId):
    global cardData

    if cardId != "" and cardId != None:
        LogManager.PrintLog("CardDatabaseManager", "SearchCardById", "search card id: " + cardId, DefineManager.LOG_LEVEL_DEBUG)

        for indexOfCardType in cardData.keys():
            for indexOfCardInfo in cardData[indexOfCardType]:
                if indexOfCardInfo["cardId"] == cardId:
                    LogManager.PrintLog("CardDatabaseManager", "SearchCardById", "find card id: " + cardId, DefineManager.LOG_LEVEL_DEBUG)
                    return indexOfCardInfo
        LogManager.PrintLog("CardDatabaseManager", "SearchCardById", "cannot find card id: " + cardId, DefineManager.LOG_LEVEL_WARN)
    else:
        return None
    return None