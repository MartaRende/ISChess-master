import numpy as np


class ElaborateData:
    def __init__(self,player_sequence, board):
        self.player_sequence = player_sequence
        self.board = np.array(board)


    #to find team it works only for 1vs1
    def find_bot_color(self):
        color_bot = []
        color_adv = []
        newline = ''

        for i in range(0, len(self.player_sequence), 3):
            newline += self.player_sequence[i:i + 2]

        for i in range(len(newline)):
            if newline[i] == self.player_sequence[0]:
                color_bot.append(newline[i + 1])
            elif newline[i]== self.player_sequence[3]:
                color_adv.append((newline[i+1]))
        return color_bot,color_adv








