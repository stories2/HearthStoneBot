from Settings import DefineManager
from Utils import LogManager, CardDatabaseManager

def FieldMainObserver(fieldData):
    fieldStatusBasedId = []
    fieldStatusCard = []
    fieldStatusBasedId = ParseFieldStatus(fieldData)
    fieldStatusCard = GetEachCardSpec(fieldStatusBasedId)
    FieldSpecObserver(fieldStatusCard)

def FieldSpecObserver(fieldSpecStatusData):

    fieldSpecPlayer1 = fieldSpecStatusData[0]
    fieldSpecPlayer2 = fieldSpecStatusData[1]

    fieldStatusPlayer1 = ["", "", "", "", "", "", "", ""]
    fieldStatusPlayer2 = ["", "", "", "", "", "", "", ""]
    fieldPrintFormat = "{0:>10} |{1:>10} |{2:>10} |{3:>10} |{4:>10} |{5:>10} |{6:>10} |{7:>10} |"


    for indexCounter in fieldSpecPlayer1:
        indexOfCardSpec = fieldSpecPlayer1[indexCounter]
        if indexOfCardSpec != None:
            try:
                if indexOfCardSpec.has_key(u"attack") and indexOfCardSpec.has_key(u"health") and indexOfCardSpec.has_key(u"cost"):
                    attackValue = indexOfCardSpec[u"attack"]
                    healthValue = indexOfCardSpec[u"health"]
                    costValue = indexOfCardSpec[u"cost"]
                    fieldStatusPlayer1[indexCounter] = str(attackValue) + "/" + str(healthValue) + "/" + str(costValue)
            except:
                fieldStatusPlayer1[indexCounter] = "?/?/?"

    for indexCounter in fieldSpecPlayer2:
        indexOfCardSpec = fieldSpecPlayer2[indexCounter]
        if indexOfCardSpec != None:
            try:
                if indexOfCardSpec.has_key(u"attack") and indexOfCardSpec.has_key(u"health") and indexOfCardSpec.has_key(u"cost"):
                    attackValue = indexOfCardSpec[u"attack"]
                    healthValue = indexOfCardSpec[u"health"]
                    costValue = indexOfCardSpec[u"cost"]
                    fieldStatusPlayer2[indexCounter] = str(attackValue) + "/" + str(healthValue) + "/" + str(costValue)
            except:
                fieldStatusPlayer2[indexCounter] = "?/?/?"

    fieldOfPlayer1 = fieldPrintFormat.format(*fieldStatusPlayer1)
    fieldOfPlayer2 = fieldPrintFormat.format(*fieldStatusPlayer2)

    LogManager.PrintLog("FieldObserver", "FieldSpecObserver", "player1: " + fieldOfPlayer1,
                        DefineManager.LOG_LEVEL_INFO)
    LogManager.PrintLog("FieldObserver", "FieldSpecObserver", "player2: " + fieldOfPlayer2,
                        DefineManager.LOG_LEVEL_INFO)


def GetEachCardSpec(fieldStatusData):
    fieldStatusPlayer1 = fieldStatusData[0]
    fieldStatusPlayer2 = fieldStatusData[1]

    fieldSpecPlayer1 = {}
    fieldSpecPlayer2 = {}

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
    fieldPrintFormat = "{0:>10} |{1:>10} |{2:>10} |{3:>10} |{4:>10} |{5:>10} |{6:>10} |{7:>10} |"

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

    fieldOfPlayer1 = fieldPrintFormat.format(*fieldStatusPlayer1)
    fieldOfPlayer2 = fieldPrintFormat.format(*fieldStatusPlayer2)

    LogManager.PrintLog("FieldObserver", "ParseFieldStatus", "player1: " + fieldOfPlayer1,
                        DefineManager.LOG_LEVEL_INFO)
    LogManager.PrintLog("FieldObserver", "ParseFieldStatus", "player2: " + fieldOfPlayer2,
                        DefineManager.LOG_LEVEL_INFO)
    return [fieldStatusPlayer1, fieldStatusPlayer2]