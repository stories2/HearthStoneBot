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