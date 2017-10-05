from Settings import DefineManager
import LogManager

def PrintFieldStatus(fieldDictionaryData):
    fieldStatusPlayer1 = ["", "", "", "", "", "", "", ""]
    fieldStatusPlayer2 = ["", "", "", "", "", "", "", ""]
    fieldPrintFormat = "{0:>10} |{1:>10} |{2:>10} |{3:>10} |{4:>10} |{5:>10} |{6:>10} |{7:>10} |"

    for indexOfFieldNumber, indexOfCard in fieldDictionaryData.iteritems():
        if indexOfCard[0][3] != 0:
            playerNumber = int(indexOfCard[0][DefineManager.PLAYER_NUMBER_SAVED_POINT])
            zonePosition = int(indexOfCard[0][3])

            if playerNumber == 1:
                fieldStatusPlayer1[zonePosition] = indexOfCard[0][0]
            elif playerNumber == 2:
                fieldStatusPlayer2[zonePosition] = indexOfCard[0][0]
            else:
                LogManager.PrintLog("AdvancedPrintManager", "PrintFieldStatus", "unknown player", DefineManager.LOG_LEVEL_INFO)

    fieldOfPlayer1 = fieldPrintFormat.format(*fieldStatusPlayer1)
    fieldOfPlayer2 = fieldPrintFormat.format(*fieldStatusPlayer2)

    LogManager.PrintLog("AdvancedPrintManager", "PrintFieldStatus", "player1: " + fieldOfPlayer1,
                        DefineManager.LOG_LEVEL_INFO)
    LogManager.PrintLog("AdvancedPrintManager", "PrintFieldStatus", "player2: " + fieldOfPlayer2,
                        DefineManager.LOG_LEVEL_INFO)