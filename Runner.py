# -*- coding: utf-8 -*-
from Core import FileIO, FieldHelper
from Utils import CardDatabaseManager

CardDatabaseManager.StaticCradDataLoader()

# FileIO.StaticLoader()
FileIO.RealtimeLoader()
# fieldData = [
#     [
#         [-1, -1, -1],
#         [3, 4, 1],
#         [-1, -1, -1],
#         [1, 11, 2],
#         [-1, -1, -1],
#         [-1, -1, -1],
#         [-1, -1, -1],
#         [-1, -1, -1]
#     ],
#
#     [
#         [-1, -1, -1],
#         [5, 4, 3],
#         [-1, -1, -1],
#         [5, 1, 4],
#         [-1, -1, -1],
#         [-1, -1, -1],
#         [-1, -1, -1],
#         [-1, -1, -1]
#     ]
# ]
# playerNumber = 0
# attackCardInfo = [0, 1, 0, 3, 0, 0, 0, 0] # 필드 데이터 배열에 몇번지에 카드가 있는지 그 번호를 쓰고 1:1 대응
# defendCardInfo = [0, 3, 0, 3, 0, 0, 0, 0]
# FieldHelper.SimulateCardSwap(fieldData, playerNumber, attackCardInfo, defendCardInfo)
# FieldHelper.RecursiveSearcher(playerNumber, fieldData, 1, [attackCardInfo, defendCardInfo])
# FieldHelper.GetBestSwap(playerNumber)