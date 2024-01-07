from collections import deque
import random

from Bots.Moves_test import Moves_test
from Bots.Node import Node


class NewState_test:
    def __init__(self, player_sequence, board):
        self.moves = Moves_test(player_sequence,board)
        self.root = None
        self.count_state = 0
        self.hash_map_board = {}
        self.hash_map_piece = {}
        self.current_board = self.moves.board

    def create_main_node(self):
        w = self.moves.heuristics.calculate_weight(self.moves.board)
        self.root = Node(w)
        self.count_state += 1
        return self.root


    def create_child(self, parent_node, newboard, depth):
        weight = self.moves.heuristics.calculate_weight(newboard)
        child_node = Node(weight)
        parent_node.add_child(child_node)
        self.count_state += 1
        return child_node


    def create_tree(self, n):
        self.root = self.create_main_node()
        self.create_tree_bfs(self.root, n-1)
        #self.root.print_tree(1)

    def create_tree_bfs(self, root_node, depth, max_children=15):
        queue = deque([(root_node, self.current_board, depth, True)])
        visited = set()
        while queue:
            current_node, current_board, current_depth, is_maximizing = queue.popleft()

            if current_depth <= 0:
                continue

            poss_positions = self.moves.find_new_state(current_board, current_depth, depth)
            created_children = 0
            random.shuffle(poss_positions)

            for poss in poss_positions:
                if created_children >= max_children and depth>2:
                    break

                new_data, piece = self.moves.new_board(poss[0], poss[1], poss[2], poss[3], current_board)
                if depth == 3:
                    print("board", new_data)

                if tuple(map(tuple, new_data)) not in visited:
                    child_node = self.create_child(current_node, new_data, current_depth)

                    visited.add(tuple(map(tuple, new_data)))
                    if current_depth == depth:
                        self.hash_map_board[child_node] = new_data
                        self.hash_map_piece[child_node] = piece

                    next_player = not is_maximizing
                    queue.append((child_node, new_data, current_depth - 1, next_player))

                    created_children += 1 








