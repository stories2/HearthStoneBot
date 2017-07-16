from Settings import DefineManager
import logging
import datetime

def PrintLog(targetClassName = DefineManager.DEFAULT_CLASS_NAME, targetMethodName = DefineManager.DEFAULT_METHOD_NAME,
             logDescription = DefineManager.DEFAULT_LOG_MESSAGE, logLevel = DefineManager.LOG_LEVEL_DEBUG):

    logPrintedDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    logMessage = logPrintedDate + " {" + targetClassName + "} [" + targetMethodName + "] (" + logDescription + ")"
    logger = logging.getLogger()
    if logLevel == DefineManager.LOG_LEVEL_DEBUG:
        logger.setLevel(logging.DEBUG)
        logging.debug(logMessage)
    elif logLevel == DefineManager.LOG_LEVEL_INFO:
        logger.setLevel(logging.INFO)
        logging.info(logMessage)
    elif logLevel == DefineManager.LOG_LEVEL_WARN:
        logger.setLevel(logging.WARN)
        logging.warn(logMessage)
    elif logLevel == DefineManager.LOG_LEVEL_ERROR:
        logger.setLevel(logging.ERROR)
        logging.error(logMessage)
    else:
        logging.warn(logPrintedDate + DefineManager.DEFAULT_PRINT_MESSAGE)