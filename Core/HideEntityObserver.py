import re
from Utils import LogManager
from Settings import DefineManager

def CheckHideEntity(logMessage):
    foundedEntityGroup = re.search("     HIDE_ENTITY - Entity=(.+?) tag=(.+?) value=(.+?)\n", logMessage)

    if foundedEntityGroup != None:
        hideEntityData = [foundedEntityGroup.group(1), foundedEntityGroup.group(2), foundedEntityGroup.group(3)]
        # LogManager.PrintLog("HideEntityObserver", "CheckHideEntity", "entity: " + hideEntityData[0] + " tag: " + hideEntityData[1] + " value: " + hideEntityData[2], DefineManager.LOG_LEVEL_INFO)

        hideEntityDetail = re.search("name=(.+?) id=(.+?) zone=(.+?) zonePos=(.+?) cardId=(.+?) player=(.+?)]", hideEntityData[0])

        if hideEntityDetail != None:

            hideEntityData[0] = [hideEntityDetail.group(1), hideEntityDetail.group(2), hideEntityDetail.group(3), hideEntityDetail.group(4),
                                 hideEntityDetail.group(5), hideEntityDetail.group(6)]

            # LogManager.PrintLog("HideEntityObserver", "CheckHideEntity",
            #                     "entity: " + hideEntityData[0] + " tag: " + hideEntityData[1] + " value: " +
            #                     hideEntityData[2], DefineManager.LOG_LEVEL_INFO)
            LogManager.PrintLog("HideEntityObserver", "CheckHideEntity", "entity: " + " ".join(hideEntityData[0]) +
                                " tag: " + hideEntityData[1] + " value: " + hideEntityData[2], DefineManager.LOG_LEVEL_INFO)

            return hideEntityData[0]
        else:
            LogManager.PrintLog("HideEntityObserver", "CheckHideEntity", "wrong entity accepted", DefineManager.LOG_LEVEL_WARN)
    return None