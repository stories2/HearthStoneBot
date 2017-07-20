from Utils import LogManager
from Settings import DefineManager
import ShowEntityObserver
import HideEntityObserver
import TagChangeEntityObserver
import json

deckObserverPlayer1 = {}
deckObserverPlayer2 = {}

def GameObservingInit():
    global deckObserverPlayer1
    global deckObserverPlayer2

    deckObserverPlayer1 = {}
    deckObserverPlayer2 = {}

def ParseShowEntity(logMessage):
    global deckObserverPlayer1
    global deckObserverPlayer2

    if TagChangeEntityObserver.IsGameStart(logMessage):
        GameObservingInit()

    TagChangeEntityObserver.IsGameComplete(logMessage)
    TagChangeEntityObserver.DetectFieldCard(logMessage)
    TagChangeEntityObserver.DetectTurns(logMessage)

    # found show entity start point
    if ShowEntityObserver.GetIsShowEntityMode() == False:
        ShowEntityObserver.IsShowEntityModeStartPoint(logMessage)
    # crawl card tag datas
    else:
        selectedCardInfo = ShowEntityObserver.GetShowEntityModeTagAndValue(logMessage)
        if selectedCardInfo != None:
            if selectedCardInfo.has_key("CONTROLLER"):
                if selectedCardInfo["CONTROLLER"] == DefineManager.PLAYER_NUMBER_1:
                    deckObserverPlayer1[selectedCardInfo["ENTITY_ID"]] = selectedCardInfo
                    LogManager.PrintLog("DeckObserver", "ParseShowEntity", "player#1 selected card#" +
                                        selectedCardInfo["ENTITY_ID"] + ": " + selectedCardInfo["CARD_ID"], DefineManager.LOG_LEVEL_INFO)
                else:
                    deckObserverPlayer2[selectedCardInfo["ENTITY_ID"]] = selectedCardInfo
                    LogManager.PrintLog("DeckObserver", "ParseShowEntity", "player#2 selected card#" +
                                        selectedCardInfo["ENTITY_ID"] + ": " + selectedCardInfo["CARD_ID"], DefineManager.LOG_LEVEL_INFO)
            else:
                if selectedCardInfo.has_key("ENTITY_ID") and selectedCardInfo.has_key("CARD_ID"):
                    LogManager.PrintLog("DeckObserver", "ParseShowEntity", "whose card is this? card#"  +
                                            selectedCardInfo["ENTITY_ID"] + ": " + selectedCardInfo["CARD_ID"], DefineManager.LOG_LEVEL_WARN)
                else:
                    try:
                        LogManager.PrintLog("DeckObserver", "ParseShowEntity", "wrong card accepted\n" +
                                            json.dumps(selectedCardInfo), DefineManager.LOG_LEVEL_WARN)
                    except:
                        LogManager.PrintLog("DeckObserver", "ParseShowEntity", "cannot print wrong card", DefineManager.LOG_LEVEL_ERROR)

    # found hide entity
    hideCardInfo = HideEntityObserver.CheckHideEntity(logMessage)
    if hideCardInfo != None:
        if hideCardInfo[DefineManager.PLAYER_NUMBER_SAVED_POINT] == DefineManager.PLAYER_NUMBER_1:
            deckObserverPlayer1[hideCardInfo[DefineManager.CARD_ID_SAVED_POINT]] = {}
            LogManager.PrintLog("DeckObserver", "ParseShowEntity", "player#1 hide card#" +
                                hideCardInfo[DefineManager.CARD_ID_SAVED_POINT], DefineManager.LOG_LEVEL_INFO)
        else:
            deckObserverPlayer2[hideCardInfo[DefineManager.CARD_ID_SAVED_POINT]] = {}
            LogManager.PrintLog("DeckObserver", "ParseShowEntity", "player#2 hide card#" +
                                hideCardInfo[DefineManager.CARD_ID_SAVED_POINT], DefineManager.LOG_LEVEL_INFO)