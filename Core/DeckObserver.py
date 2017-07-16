from Utils import LogManager
from Settings import DefineManager
import ShowEntityObserver
import HideEntityObserver

deckObserverPlayer1 = {}
deckObserverPlayer2 = {}

def GameObservingInit():
    global deckObserverPlayer1
    global deckObserverPlayer2

    deckObserverPlayer1 = {}
    deckObserverPlayer2 = {}

def ParseShowEntity(logMessage):
    # found show entity start point
    if ShowEntityObserver.GetIsShowEntityMode() == False:
        ShowEntityObserver.IsShowEntityModeStartPoint(logMessage)
    # crawl card tag datas
    else:
        selectedCardInfo = ShowEntityObserver.GetShowEntityModeTagAndValue(logMessage)
        if selectedCardInfo != None:
            if selectedCardInfo["CONTROLLER"] == DefineManager.PLAYER_NUMBER_1:
                deckObserverPlayer1[selectedCardInfo["ENTITY_ID"]] = selectedCardInfo
                LogManager.PrintLog("DeckObserver", "ParseShowEntity", "player#1 selected card#" +
                                    selectedCardInfo["ENTITY_ID"] + ": " + selectedCardInfo["CARD_ID"], DefineManager.LOG_LEVEL_INFO)
            else:
                deckObserverPlayer2[selectedCardInfo["ENTITY_ID"]] = selectedCardInfo
                LogManager.PrintLog("DeckObserver", "ParseShowEntity", "player#2 selected card#" +
                                    selectedCardInfo["ENTITY_ID"] + ": " + selectedCardInfo["CARD_ID"], DefineManager.LOG_LEVEL_INFO)

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