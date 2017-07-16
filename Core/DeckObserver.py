import ShowEntityObserver

def ParseShowEntity(logMessage):
    # found show entity start point
    if ShowEntityObserver.GetIsShowEntityMode() == False:
        ShowEntityObserver.IsShowEntityModeStartPoint(logMessage)
    # crawl card tag datas
    else:
        ShowEntityObserver.GetShowEntityModeTagAndValue(logMessage)