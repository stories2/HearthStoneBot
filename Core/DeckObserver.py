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
            LogManager.PrintLog("DeckObserver", "IsShowEntityModeStartPoint", "entity: " + foundedResult[0] + " card: " + foundedResult[1], DefineManager.LOG_LEVEL_INFO)
            return foundedResult
    else:
        return []

#def ParseShowEntity(logMessage):
