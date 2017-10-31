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
    defCardStatus = [0, 0, 0, 0, 0, 0, 0, 0]
    length = len(attackCardInfo)
    for i in range(1, length):
        attacker = attackCardInfo[i]
        if attacker > 0:
            linkList.append([0, attacker, fieldData[playerNumber][attacker][0]]) # attack
            linkList.append([attacker, 0, fieldData[playerNumber][attacker][1]]) # health

    playerNumber = (playerNumber + 1) % 2 # defender
    for i in range(1, length):
        defender = defendCardInfo[i]
        if defender > 0:
            defCardStatus[defender] = 1
            linkList.append([DefineManager.MAXIMUM_FIELD_CARD_NUM * 2 + 1, defender + DefineManager.MAXIMUM_FIELD_CARD_NUM + 1, fieldData[playerNumber][defender][0]]) # attack
            linkList.append([defender + DefineManager.MAXIMUM_FIELD_CARD_NUM + 1, DefineManager.MAXIMUM_FIELD_CARD_NUM * 2 + 1, fieldData[playerNumber][defender][1]]) # health

    playerNumber = (playerNumber + 1) % 2 # attacker
    for i in range(1, length):
        attacker = attackCardInfo[i]
        defender = defendCardInfo[i]
        if attacker > 0 and defender > 0:
            linkList.append([attacker, defender + DefineManager.MAXIMUM_FIELD_CARD_NUM + 1, fieldData[playerNumber][attacker][0]])
            linkList.append([defender + DefineManager.MAXIMUM_FIELD_CARD_NUM + 1, attacker, fieldData[(playerNumber + 1) % 2][defender][0]])

    for i in range(0, DefineManager.MAXIMUM_FIELD_CARD_NUM * 2 + 2):
        rowTemplate = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        playground.append(rowTemplate)

    for indexOfLink in linkList:
        x = indexOfLink[0]
        y = indexOfLink[1]
        cost = indexOfLink[2]
        playground[y][x] = cost

    for y in range(1, DefineManager.MAXIMUM_FIELD_CARD_NUM * 2 + 1):
        for x in range(1, y):
            if playground[y][x] > 0:
                # LogManager.PrintLog("FieldHelper", "SimulateCardSwap",
                #                     "<" + str(x) + ", " + str(y) + "> : " + str(playground[y][x]), DefineManager.LOG_LEVEL_INFO)
                defenderAttack = playground[y][DefineManager.MAXIMUM_FIELD_CARD_NUM * 2 + 1]
                defenderHealth = playground[DefineManager.MAXIMUM_FIELD_CARD_NUM * 2 + 1][y]
                attackerAttack = playground[y][x]
                if defenderHealth > 0:
                    playground[DefineManager.MAXIMUM_FIELD_CARD_NUM * 2 + 1][y] -= attackerAttack
                    if playground[DefineManager.MAXIMUM_FIELD_CARD_NUM * 2 + 1][y] <= 0:
                        playground[y][DefineManager.MAXIMUM_FIELD_CARD_NUM * 2 + 1] = 0
                    playground[0][x] -= defenderAttack
                    if playground[0][x] < 0:
                        playground[0][x] = 0
    sum = 0
    for index in range(0, DefineManager.MAXIMUM_FIELD_CARD_NUM * 2 + 1):
        sum = sum + playground[0][index]
        sum = sum - playground[index][DefineManager.MAXIMUM_FIELD_CARD_NUM * 2 + 1]

    playerNumber = (playerNumber + 1) % 2 # defender
    for index in range(1, DefineManager.MAXIMUM_FIELD_CARD_NUM + 1):
        if fieldData[playerNumber][index][0] != DefineManager.NOT_AVAILABLE and defCardStatus[index] != 1:
            sum = sum - fieldData[playerNumber][index][0]
    LogManager.PrintLog("FieldHelper", "SimulateCardSwap",
                        "the score is: " + str(sum), DefineManager.LOG_LEVEL_INFO)
    return sum