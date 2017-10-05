from Settings import DefineManager
from Utils import LogManager, CardDatabaseManager

def FieldMainObserver(fieldData):
    fieldStatusBasedId = []
    fieldStatusCard = []
    fieldStatusBasedId = ParseFieldStatus(fieldData)
    fieldStatusCard = GetEachCardSpec(fieldStatusBasedId)

def GetEachCardSpec(fieldStatusData):
    fieldStatusPlayer1 = fieldStatusData[0]
    fieldStatusPlayer2 = fieldStatusData[1]

    fieldSpecPlayer1 = []
    fieldSpecPlayer2 = []

    indexCounter = 0

    for indexOfCardId in fieldStatusPlayer1:
        fieldSpecPlayer1[indexCounter] = CardDatabaseManager.SearchCardById(indexOfCardId)
        indexCounter += 1

    indexCounter = 0

    for indexOfCardId in fieldStatusPlayer2:
        fieldSpecPlayer2[indexCounter] = CardDatabaseManager.SearchCardById(indexOfCardId)
        indexCounter += 1

    return [fieldSpecPlayer1, fieldSpecPlayer2]

def ParseFieldStatus(fieldData):
    fieldStatusPlayer1 = ["", "", "", "", "", "", "", ""]
    fieldStatusPlayer2 = ["", "", "", "", "", "", "", ""]

    for indexOfFieldNumber, indexOfCard in fieldData.iteritems():
        if indexOfCard[0][3] != 0:
            playerNumber = int(indexOfCard[0][DefineManager.PLAYER_NUMBER_SAVED_POINT])
            zonePosition = int(indexOfCard[0][3])

            if playerNumber == 1:
                fieldStatusPlayer1[zonePosition] = indexOfCard[0][4]
            elif playerNumber == 2:
                fieldStatusPlayer2[zonePosition] = indexOfCard[0][4]
            else:
                LogManager.PrintLog("FieldObserver", "ParseFieldStatus", "unknown player", DefineManager.LOG_LEVEL_WARN)

    return [fieldStatusPlayer1, fieldStatusPlayer2]