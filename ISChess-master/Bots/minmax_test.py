import time

import numpy as np

from Bots.NewState_test import NewState_test


class Maximizer_test:
    def __init__(self,player_sequence, board ):
        self.newstate = NewState_test(player_sequence,board)
        self.depth = 3
        self.newstate.create_tree(self.depth)
        print(self.newstate.count_state)
        self.board = np.array(board) #old_board


    def minimax(self,node, depth, maximizingPlayer=True):
        if node is None:
            node = self.newstate.root
        if node.is_leaf() or depth == 0:
            return node.value
        if maximizingPlayer:
            max_value = float('-inf')
            for child_node in node.children:
                v = self.minimax(child_node, depth - 1, False)
                max_value = max(max_value, v)
            node.value = max_value
            return max_value
        else:
            min_value = float('inf')
            for child_node in node.children:
                v = self.minimax(child_node, depth - 1, True)
                min_value= min(min_value, v)
            node.value = min_value
            return min_value

    def find_new_state(self):

        best_value = self.minimax(self.newstate.root,  self.depth, True)
        print("best",best_value)
        return self.newstate.moves.heuristics.choose_weighted_random_weight(self.newstate.hash_map_board,self.newstate.hash_map_piece,best_value)

    def determine_final_position(self):
        new_board = np.array(self.find_new_state())
        print("new_board", new_board)
        print("old_board", self.board)

        differences = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != new_board[i][j]:
                    differences.append((i, j))
        if len(differences) != 2:
            print("Error")
            return None

        start_pos, end_pos = differences[0], differences[1]


        piece = ''
        if len(self.board[start_pos[0]][start_pos[1]]) > 1 and self.board[start_pos[0]][start_pos[1]][
            1] in self.newstate.moves.color_bot:
            piece = self.board[start_pos[0]][start_pos[1]]
        elif len(self.board[end_pos[0]][end_pos[1]]) > 1 and self.board[end_pos[0]][end_pos[1]][
            1] in self.newstate.moves.color_bot:
            piece = self.board[end_pos[0]][end_pos[1]]
            temp = end_pos
            end_pos = start_pos
            start_pos = temp
        return start_pos, end_pos


