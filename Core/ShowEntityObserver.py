from Settings import DefineManager
from Utils import LogManager
import re

isShowEntityMode = False

def SetIsShowEntityMode(isShowEntityModeStatus):
    global isShowEntityMode
    isShowEntityMode = isShowEntityModeStatus

def GetIsShowEntityMode():
    global isShowEntityMode
    return isShowEntityMode

def IsShowEntityModeStartPoint(logMessage):
    if GetIsShowEntityMode() == False:
        searchedLogMessage = re.search("SHOW_ENTITY - Updating Entity=(.+?) CardID=(.+?)\n", logMessage)
        if searchedLogMessage != None:
            SetIsShowEntityMode(True)
            foundedResult = [searchedLogMessage.group(1), searchedLogMessage.group(2)]
            LogManager.PrintLog("ShowEntityObserver", "IsShowEntityModeStartPoint", "entity: " + foundedResult[0] + " card: " + foundedResult[1], DefineManager.LOG_LEVEL_INFO)
            return foundedResult
    else:
        LogManager.PrintLog("ShowEntityObserver", "IsShowEntityModeStartPoint", "Show entity mode already true", DefineManager.LOG_LEVEL_WARN)
        return []

def GetShowEntityModeTagAndValue(logMessage):
    searchedLogMessage = re.search("tag=(.+?) value=(.+?)\n", logMessage)
    if searchedLogMessage != None:
        foundedResult = [searchedLogMessage.group(1), searchedLogMessage.group(2)]
        LogManager.PrintLog("ShowEntityObserver", "GetShowEntityModeTagAndValue", "tag: " + foundedResult[0] + " value: " + foundedResult[1], DefineManager.LOG_LEVEL_INFO)
    else:
        SetIsShowEntityMode(False)
        LogManager.PrintLog("ShowEntityObserver", "GetShowEntityModeTagAndValue", "get tag and value disabled", DefineManager.LOG_LEVEL_WARN)
