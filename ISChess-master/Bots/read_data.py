import numpy as np


class ElaborateData:
    def __init__(self,player_sequence, board):
        self.player_sequence = player_sequence
        self.board = np.array(board)
#not usefull
    def read_data(self):
        with open(self.file_path, "r") as file:
            arr = []
            for line in file:
                # Split each line into elements (assuming space-separated values)
                line_elements = line.split(',')  # Change the split delimiter if necessary
                arr.append(line_elements)
        return arr
    #not usefull
    def read_clean_data(self):
        data = self.read_data()
        self.newdata = [[item.rstrip('\n') for item in sublist] for sublist in data]
        return  self.newdata

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
            elif newline[i]== 'b':
                color_adv.append((newline[i]))

        return color_bot,color_adv








