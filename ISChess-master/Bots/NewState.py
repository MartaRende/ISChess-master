from collections import deque

from Heuristics import Heuristics
from Moves import Moves
from Node import Node


class NewState:
    def __init__(self, player_sequence, board):
        self.moves = Moves(player_sequence,board)
        self.root = None
        self.hash_map = {}
        self.tot_depth = 0
        self.current_board = self.moves.board

    def create_main_node(self):
        w = self.moves.heuristics.calculate_weight(self.moves.board)
        self.root = Node(w)
        return self.root


    def create_child(self, parent_node, newboard, depth):
        weight = self.moves.heuristics.calculate_weight(newboard)
        child_node = Node(weight)
        parent_node.add_child(child_node)
        return child_node


    def create_tree(self, n):
        self.root = self.create_main_node()
        self.create_tree_bfs(self.root, n)
       # self.root.print_tree(1)

    def create_tree_bfs(self, root_node, depth):
        queue = deque([(root_node, self.current_board, depth, True)])

        while queue:


            current_node, current_board, current_depth, is_maximizing = queue.popleft()
            if current_depth <= 0:
                return
            print("current depth", current_depth)
            poss_positions = self.moves.find_new_state(current_board)

            for poss in poss_positions:
                new_data = self.moves.new_board(poss[0], poss[1], poss[2], poss[3])
                child_node = self.create_child(current_node, new_data, current_depth)

                if current_depth == depth and new_data != self.moves.board:
                    self.hash_map[child_node] = new_data

                next_player = not is_maximizing
                queue.append((child_node, new_data, current_depth - 1, next_player))






