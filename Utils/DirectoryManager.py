from Settings import DefineManager
import LogManager
import os
import re

def SearchDirectoryFiles(targetDirectoryPath):
    return os.listdir(targetDirectoryPath)

def FindLatestLogFile(hearthStoneLogFilesPath = DefineManager.DEFAULT_HEARTH_STONE_LOG_FILES_PATH):
    listOfFiles = SearchDirectoryFiles(hearthStoneLogFilesPath)

    latestSavedFile = listOfFiles[-1]

    LogManager.PrintLog("DirectoryManager", "FindLatestLogFile", "last file: " + latestSavedFile, DefineManager.LOG_LEVEL_INFO)

    return latestSavedFile

def MakeNewDirectory(targetDirectoryPath, newDirectoryName):
    if not os.path.exists(targetDirectoryPath + newDirectoryName):
        os.makedirs(targetDirectoryPath + newDirectoryName)
        LogManager.PrintLog("DirectoryManager", "MakeNewDirectory", "create dir: " + newDirectoryName, DefineManager.LOG_LEVEL_INFO)
        return True
    LogManager.PrintLog("DirectoryManager", "MakeNewDirectory", "the dir already exist", DefineManager.LOG_LEVEL_WARN)
    return False