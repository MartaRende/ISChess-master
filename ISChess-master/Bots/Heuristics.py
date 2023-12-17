import random

import numpy as np
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
        return weight


    def choose_weighted_random_weight(self, hash_map_board, hash_map_piece, best_value):
        weight =  []
        prov_hash_map = {}
        for key, value in hash_map_board.items():
            if key.value == best_value:
                if hash_map_piece[key][0] == 'p':
                    weight.append(100)
                    prov_hash_map[key] = value
                if hash_map_piece[key][0] == 'n':
                    weight.append(70)
                    prov_hash_map[key] = value
                if hash_map_piece[key][0] == 'r':
                    weight.append(60)
                    prov_hash_map[key] = value
                if hash_map_piece[key][0] == 'b':
                    weight.append(70)
                    prov_hash_map[key] = value
                if hash_map_piece[key][0] == 'q':
                    weight.append(10)
                    prov_hash_map[key] = value
                if hash_map_piece[key][0] == 'k':
                    weight.append(15)
                    prov_hash_map[key] = value
        chosen_value = random.choices(list(prov_hash_map.values()), weight, k=1)[0]
        return chosen_value

    def choose_random_weight(self, hash_map, best_value):
        poss_values = []
        for key, value in  hash_map.items():
            if key.value == best_value:
                poss_values.append(value)
        random.shuffle(poss_values)
        return poss_values[0]



