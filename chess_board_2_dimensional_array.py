# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:50:45 2020

@author: heart
"""

EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
    
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)
