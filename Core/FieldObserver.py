from Settings import DefineManager
from Utils import LogManager, CardDatabaseManager

def FieldMainObserver(fieldData):
    fieldStatusBasedId = []
    fieldStatusBasedId = ParseFieldStatus(fieldData)

    

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