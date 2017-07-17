from Settings import DefineManager
import LogManager
import os
import shutil
import glob
import re

def SearchDirectoryFiles(targetDirectoryPath):
    # return os.listdir(targetDirectoryPath)
    return glob.glob(targetDirectoryPath + "/*.log")

def FindLatestLogFile(hearthStoneLogFilesPath = DefineManager.DEFAULT_HEARTH_STONE_LOG_FILES_PATH):
    listOfFiles = SearchDirectoryFiles(hearthStoneLogFilesPath)

    latestSavedFile = listOfFiles[-1]

    LogManager.PrintLog("DirectoryManager", "FindLatestLogFile", "last file: " + latestSavedFile, DefineManager.LOG_LEVEL_INFO)

    return latestSavedFile

def MakeNewDirectory(targetDirectoryPath, newDirectoryName):
    if not os.path.exists(targetDirectoryPath + newDirectoryName):
        os.makedirs(targetDirectoryPath + newDirectoryName + "/")
        LogManager.PrintLog("DirectoryManager", "MakeNewDirectory", "create dir: " + newDirectoryName, DefineManager.LOG_LEVEL_INFO)
        return True
    LogManager.PrintLog("DirectoryManager", "MakeNewDirectory", "the dir already exist", DefineManager.LOG_LEVEL_WARN)
    return False

def MoveFileToDirectory(targetDirectoryPath, targetFileName, targetFolderPath):
    MakeNewDirectory(targetDirectoryPath, targetFolderPath)

    try:
        shutil.move(targetDirectoryPath + targetFileName, targetDirectoryPath + targetFolderPath + "/" + targetFileName)

        LogManager.PrintLog("DirectoryManager", "MoveFileToDirectory", "file moved successfully", DefineManager.LOG_LEVEL_INFO)
    except:
        LogManager.PrintLog("DirectoryManager", "MoveFileToDirectory", "file move process has problem", DefineManager.LOG_LEVEL_ERROR)
