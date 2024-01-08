import time

import numpy as np
#
#   Example function to be implemented for
#       Single important function is next_best
#           color: a single character str indicating the color represented by this bot ('w' for white)
#           board: a 2d matrix containing strings as a descriptors of the board '' means empty location "XC" means a piece represented by X of the color C is present there
#           budget: time budget allowed for this turn, the function must return a pair (xs,ys) --> (xd,yd) to indicate a piece at xs, ys moving to xd, yd
#

from PyQt6 import QtCore

#   Be careful with modules to import from the root (don't forget the Bots.)
from Bots.ChessBotList import register_chess_bot
from Bots.CR_ChessMoveEvaluator import ChessMoveEvaluator
#   Simply move the pawns forward and tries to capture as soon as possible

def CR_chess_bot(player_sequence, board, time_budget, **kwargs):
    maximize = ChessMoveEvaluator(player_sequence, board)
    old, new = maximize.determine_final_position()

    return old,new


register_chess_bot("CR", CR_chess_bot)
