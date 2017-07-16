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

            entityDetailMessage = re.search("player=(.+?)]", searchedLogMessage.group(1))

            if entityDetailMessage != None:

                foundedEntityDetailResult = [entityDetailMessage.group(1)]

                # LogManager.PrintLog("ShowEntityObserver", "IsShowEntityModeStartPoint", "entity detail: " + foundedEntityDetailResult[0], DefineManager.LOG_LEVEL_INFO)

                SetIsShowEntityMode(True)
                foundedResult = [foundedEntityDetailResult[0], searchedLogMessage.group(2)]
                LogManager.PrintLog("ShowEntityObserver", "IsShowEntityModeStartPoint", "player: " + foundedResult[0] + " card: " + foundedResult[1], DefineManager.LOG_LEVEL_INFO)
                return foundedResult
            else:
                LogManager.PrintLog("ShowEntityObserver", "IsShowEntityModeStartPoint", "Wrong entity accepted", DefineManager.LOG_LEVEL_WARN)
    else:
        LogManager.PrintLog("ShowEntityObserver", "IsShowEntityModeStartPoint", "Show entity mode already true", DefineManager.LOG_LEVEL_WARN)
        return []

def GetShowEntityModeTagAndValue(logMessage):
    searchedLogMessage = re.search("         tag=(.+?) value=(.+?)\n", logMessage)
    if searchedLogMessage != None:
        foundedResult = [searchedLogMessage.group(1), searchedLogMessage.group(2)]
        LogManager.PrintLog("ShowEntityObserver", "GetShowEntityModeTagAndValue", "tag: " + foundedResult[0] + " value: " + foundedResult[1], DefineManager.LOG_LEVEL_INFO)
    else:
        SetIsShowEntityMode(False)
        LogManager.PrintLog("ShowEntityObserver", "GetShowEntityModeTagAndValue", "get tag and value disabled", DefineManager.LOG_LEVEL_WARN)
