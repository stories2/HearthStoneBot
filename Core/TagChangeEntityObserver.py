from Settings import DefineManager
from Utils import LogManager
import re

def DetectGameStatus(logMessage):
    tagChangeEntityData = re.search("TAG_CHANGE Entity=GameEntity tag=STATE value=(.+?)\n", logMessage)

    if tagChangeEntityData != None:
        LogManager.PrintLog("TagChangeEntityObserver", "DetectGameStatus", "value: " + tagChangeEntityData.group(1), DefineManager.LOG_LEVEL_INFO)
        return tagChangeEntityData.group(1)
    return None

def IsGameComplete(logMessage):
    checkedStatusValue = DetectGameStatus(logMessage)

    if checkedStatusValue != None:
        if checkedStatusValue == "COMPLETE":
            LogManager.PrintLog("TagChangeEntityObserver", "IsGameComplete", "End of Game", DefineManager.LOG_LEVEL_INFO)
            return True
    return False

def IsGameStart(logMessage):
    if logMessage.find("CREATE_GAME") != DefineManager.NOT_AVAILABLE:
        LogManager.PrintLog("TagChangeEntityObserver", "IsGameStart", "Start of Game", DefineManager.LOG_LEVEL_INFO)
        return True
    return False