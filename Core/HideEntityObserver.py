import re
from Utils import LogManager
from Settings import DefineManager

def CheckHideEntity(logMessage):
    foundedEntityGroup = re.search("     HIDE_ENTITY - Entity=(.+?) tag=(.+?) value=(.+?)\n", logMessage)

    if foundedEntityGroup != None:
        hideEntityData = [foundedEntityGroup.group(1), foundedEntityGroup.group(2), foundedEntityGroup.group(3)]
        LogManager.PrintLog("HideEntityObserver", "CheckHideEntity", "entity: " + hideEntityData[0] + " tag: " + hideEntityData[1] + " value: " + hideEntityData[2], DefineManager.LOG_LEVEL_INFO)
