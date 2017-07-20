from Settings import DefineManager
from Utils import LogManager
import re

def DetectGameStatus(logMessage):
    tagChangeEntityData = re.search("TAG_CHANGE Entity=(.+?) tag=PLAYSTATE value=(.+?)\n", logMessage)

    if tagChangeEntityData != None:
        LogManager.PrintLog("TagChangeEntityObserver", "DetectGameStatus", "entity: " + tagChangeEntityData.group(1) +
                            " value: " + tagChangeEntityData.group(2), DefineManager.LOG_LEVEL_INFO)
        return [tagChangeEntityData.group(1), tagChangeEntityData.group(2)]
    return None

def IsGameComplete(logMessage):
    checkedStatusValue = DetectGameStatus(logMessage)

    if checkedStatusValue != None:
        if checkedStatusValue[1] == "LOST" or checkedStatusValue[1] == "WON":
            LogManager.PrintLog("TagChangeEntityObserver", "IsGameComplete", "End of Game, Player " + " ".join(checkedStatusValue), DefineManager.LOG_LEVEL_INFO)
            return True
    return False

def IsGameStart(logMessage):
    if logMessage.find("CREATE_GAME") != DefineManager.NOT_AVAILABLE:
        LogManager.PrintLog("TagChangeEntityObserver", "IsGameStart", "Start of Game", DefineManager.LOG_LEVEL_INFO)
        return True
    return False

def DetectFieldCard(logMessage):
    tagChangeEntityData = re.search("TAG_CHANGE Entity=(.+?) tag=NUM_TURNS_IN_PLAY value=(.+?)\n", logMessage)
    if tagChangeEntityData != None:
        LogManager.PrintLog("TagChangeEntityObserver", "DetectFieldCard", "entity: " + tagChangeEntityData.group(1) +
                            " value: " + tagChangeEntityData.group(2), DefineManager.LOG_LEVEL_INFO)

def DetectTurns(logMessage):
    tagChangeEntityData = re.search("TAG_CHANGE Entity=(.+?) tag=STEP value=(.+?)\n", logMessage)
    if tagChangeEntityData != None:
        LogManager.PrintLog("TagChangeEntityObserver", "DetectTurns", "entity: " + tagChangeEntityData.group(1) +
                            " value: " + tagChangeEntityData.group(2), DefineManager.LOG_LEVEL_INFO)
        if tagChangeEntityData.group(2) == "MAIN_READY":
            LogManager.PrintLog("TagChangeEntityObserver", "DetectTurns", "Print field status", DefineManager.LOG_LEVEL_INFO)
        elif tagChangeEntityData.group(2) == "MAIN_START_TRIGGERS":
            LogManager.PrintLog("TagChangeEntityObserver", "DetectTurns", "MAIN_START_TRIGGERS", DefineManager.LOG_LEVEL_INFO)