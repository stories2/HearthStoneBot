from Settings import DefineManager
from Utils import LogManager, ExceptionManager, DirectoryManager
import subprocess
import DeckObserver

def RealtimeLoader(targetFilePath = DefineManager.DEFAULT_LOG_FILE_SAVED_PATH):
    LogManager.PrintLog("FileIO", "RealtimeLoader", "Load file path: " + targetFilePath, DefineManager.LOG_LEVEL_INFO)

    hearthStoneLogFile = subprocess.Popen(['tail', '-F', targetFilePath], stdout = subprocess.PIPE, stderr = subprocess.PIPE)

    while True:
        logMessage = hearthStoneLogFile.stdout.readline()

        if not logMessage:
            LogManager.PrintLog("FileIO", "RealtimeLoader", "File read process ended", DefineManager.LOG_LEVEL_INFO)
            break

        else:
            # LogManager.PrintLog("FileIO", "RealtimeLoader", logMessage, DefineManager.LOG_LEVEL_INFO)
            DeckObserver.ParseShowEntity(logMessage)

def StaticLoader(targetFilePath = DefineManager.DEFAULT_LOG_FILE_SAVED_PATH):
    LogManager.PrintLog("FileIO", "StaticLoader", "Load file path: " + targetFilePath, DefineManager.LOG_LEVEL_INFO)

    hearthStoneLogFile = open(targetFilePath)

    DeckObserver.GameObservingInit()

    while True:
        logMessage = hearthStoneLogFile.readline()

        if ExceptionManager.DetectOutOfLog(logMessage):
            DirectoryManager.FindLatestLogFile()

        if not logMessage:
            LogManager.PrintLog("FileIO", "StaticLoader", "File read process ended", DefineManager.LOG_LEVEL_INFO)
            break

        else:
            # LogManager.PrintLog("FileIO", "StaticLoader", logMessage, DefineManager.LOG_LEVEL_INFO)
            # DeckObserver.IsShowEntityModeStartPoint(logMessage)
            DeckObserver.ParseShowEntity(logMessage)