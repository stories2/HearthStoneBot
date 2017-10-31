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
    return