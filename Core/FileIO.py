from Settings import DefineManager
from Utils import LogManager

def RealtimeLoader(targetFilePath = DefineManager.DEFAULT_LOG_FILE_SAVED_PATH):
    LogManager.PrintLog("FileIO", "RealtimeLoader", "Load file path: " + targetFilePath, DefineManager.LOG_LEVEL_INFO)