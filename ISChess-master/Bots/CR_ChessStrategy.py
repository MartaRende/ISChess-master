import random

import numpy as np
from Bots.CR_ElaborateData import ElaborateData


class ChessStrategy :
    def __init__(self, player_sequence, board):
        self.color_bot = []
        self.elab_data = ElaborateData(player_sequence,board)
        self.data = board
        self.color_bot,self.color_adv = self.elab_data.find_bot_color()

#calculate the weight on the board
    def calculate_weight(self,board):
        weight = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if  board[i][j] != '':
                    if board[i][j][1] in self.color_bot:
                        if board[i][j][0] == 'p':
                            weight += 20
                        if board[i][j][0] == 'r' :
                            weight += 50
                        if board[i][j][0] == 'n' :
                            weight += 50
                        if board[i][j][0] == 'b' :
                            weight += 80
                        if board[i][j][0] == 'q':
                            weight += 900
                        if board[i][j][0] == 'k' :
                            weight += 9000
                    elif board[i][j][1] not in self.color_bot:
                        if board[i][j][0] == 'p':
                            weight -= 20
                        if board[i][j][0] == 'r':
                            weight -= 50
                        if board[i][j][0] == 'n':
                            weight -= 50
                        if board[i][j][0] == 'b' :
                            weight -= 80
                        if board[i][j][0] == 'q':
                            weight -= 900
                        if board[i][j][0] == 'k':
                            weight -= 9000
        return weight

# choose with a weighted random witch is the best movement to do
    def choose_weighted_random_weight(self, hash_map_board, hash_map_piece, best_value):
        weight =  []
        prov_hash_map = {}
        for key, value in hash_map_board.items():
            if key.value == best_value:
                if hash_map_piece[key][0] == 'p':
                    weight.append(250)
                    prov_hash_map[key] = value
                if hash_map_piece[key][0] == 'n':
                    weight.append(30)
                    prov_hash_map[key] = value
                if hash_map_piece[key][0] == 'r':
                    weight.append(60)
                    prov_hash_map[key] = value
                if hash_map_piece[key][0] == 'b':
                    weight.append(30)
                    prov_hash_map[key] = value
                if hash_map_piece[key][0] == 'q':
                    weight.append(10)
                    prov_hash_map[key] = value
                if hash_map_piece[key][0] == 'k':
                    weight.append(15)
                    prov_hash_map[key] = value
        chosen_value = random.choices(list(prov_hash_map.values()), weight, k=1)[0]
        return chosen_value





