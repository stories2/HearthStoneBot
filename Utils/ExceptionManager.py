from Settings import DefineManager
import LogManager
import re

def DetectOutOfLog(logMessage):
    outOfLogMessage = re.search("Truncating log, which has reached the size limit of (.+?)\n", logMessage)

    if outOfLogMessage != None:
        LogManager.PrintLog("ExceptionManager", "DetectOutOfLog", "log message will discontinue, size: " +
                            outOfLogMessage.group(1), DefineManager.LOG_LEVEL_WARN)
        return True
    return False