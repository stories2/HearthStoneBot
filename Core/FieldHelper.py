from Settings import DefineManager
from Utils import LogManager

def CalculateProcess(fieldData):
    LogManager.PrintLog("FieldHelper",
                        "CalculateProcess", "player field data accepted",
                        DefineManager.LOG_LEVEL_INFO)
    BestCardSwap(fieldData, 0)
    BestCardSwap(fieldData, 1)
    return

def BestCardSwap(fieldData, playerNumber):
    LogManager.PrintLog("FieldHelper",
                        "BestCardSwap", "calculate best card swap player : " + str(playerNumber),
                        DefineManager.LOG_LEVEL_INFO)
    return

def SimulateCardSwap(fieldData, playerNumber, attackCardInfo, defendCardInfo):
    LogManager.PrintLog("FieldHelper",
                        "SimulateCardSwap", "player: " + str(playerNumber) +
                        " attacker: " + " ".join(str(x) for x in attackCardInfo) +
                        " defender: " + " ".join(str(x) for x in defendCardInfo),
                        DefineManager.LOG_LEVEL_INFO)
    linkList = []
    playground = []
    length = len(attackCardInfo)
    for i in range(1, length):
        attacker = attackCardInfo[i]
        linkList.append([0, attacker, fieldData[playerNumber][attacker][0]]) # attack
        linkList.append([attacker, 0, fieldData[playerNumber][attacker][1]]) # health

    playerNumber = (playerNumber + 1) % 2
    for i in range(1, length):
        defender = defendCardInfo[i]
        linkList.append([DefineManager.MAXIMUM_FIELD_CARD_NUM * 2 - 1, defender + DefineManager.MAXIMUM_FIELD_CARD_NUM - 1, fieldData[playerNumber][defender][0]]) # attack
        linkList.append([defender + DefineManager.MAXIMUM_FIELD_CARD_NUM - 1, DefineManager.MAXIMUM_FIELD_CARD_NUM * 2 - 1, fieldData[playerNumber][defender][1]]) # health

    playerNumber = (playerNumber + 1) % 2
    for i in range(1, length):
        attacker = attackCardInfo[i]
        defender = defendCardInfo[i]
        linkList.append([attacker, defender + DefineManager.MAXIMUM_FIELD_CARD_NUM - 1, fieldData[playerNumber][attacker][0]])
        linkList.append([defender + DefineManager.MAXIMUM_FIELD_CARD_NUM - 1, attacker, fieldData[(playerNumber + 1) % 2][defender][0]])

    for i in range(0, DefineManager.MAXIMUM_FIELD_CARD_NUM * 2):
        rowTemplate = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        playground.append(rowTemplate)

    for indexOfLink in linkList:
        x = indexOfLink[0]
        y = indexOfLink[1]
        cost = indexOfLink[2]
        playground[y][x] = cost
    return