from Utils import LogManager
from Settings import DefineManager
import ShowEntityObserver
import HideEntityObserver
import TagChangeEntityObserver

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
                LogManager.PrintLog("DeckObserver", "ParseShowEntity", "whose card is this? card#"  +
                                        selectedCardInfo["ENTITY_ID"] + ": " + selectedCardInfo["CARD_ID"], DefineManager.LOG_LEVEL_WARN)

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