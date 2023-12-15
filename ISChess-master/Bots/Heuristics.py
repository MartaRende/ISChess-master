import random
from Bots.read_data import ElaborateData


class Heuristics :
    def __init__(self, player_sequence, board):
        self.color_bot = []
        self.elab_data = ElaborateData(player_sequence,board)
        self.data = board
        self.color_bot,self.color_adv = self.elab_data.find_bot_color()

    def calculate_weight(self,board):
        weight = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if  board[i][j] != '':
                    if board[i][j][0] == 'p' and board[i][j][1] in self.color_bot:
                        weight += 10
                    if board[i][j][0] == 'r' and board[i][j][1] in self.color_bot:
                        weight += 50
                    if board[i][j][0] == 'n' and board[i][j][1] in self.color_bot:
                        weight += 30
                    if board[i][j][0] == 'b' and board[i][j][1] in self.color_bot:
                        weight += 30
                    if board[i][j][0] == 'q'  and board[i][j][1] in self.color_bot:
                        weight += 90
                    if board[i][j][0] == 'k' and board[i][j][1] in self.color_bot:
                        weight += 900
                    if board[i][j][0] == 'p' and board[i][j][1] not in self.color_bot:
                        weight -= 10
                    if board[i][j][0] == 'r' and board[i][j][1] not in self.color_bot:
                        weight -= 50
                    if board[i][j][0] == 'n'and board[i][j][1] not in self.color_bot:
                        weight -= 30
                    if board[i][j][0] == 'b' and board[i][j][1] not in self.color_bot:
                        weight -= 30
                    if board[i][j][0] == 'q' and board[i][j][1] not in self.color_bot:
                        weight -= 90
                    if board[i][j][0] == 'k'and board[i][j][1] not in self.color_bot:
                        weight -= 900
        print(weight)
        return weight

    def choose_random_weight(self, boards):
        random.shuffle(boards)
        return boards[0]



