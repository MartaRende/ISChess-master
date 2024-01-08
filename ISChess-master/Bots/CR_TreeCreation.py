from collections import deque

from Bots.CR_Moves import Moves
from Bots.CR_Node import Node

# to build the tree
class TreeCreation:
    def __init__(self, player_sequence, board):
        self.moves = Moves(player_sequence,board)
        self.root = None
        self.hash_map_board = {} #to save all the possible boards for the next moves
        self.hash_map_piece = {} #save the pieces for to do the random weighted heuristics
        self.current_board = self.moves.board
#creation of the root
    def create_main_node(self):
        w = self.moves.chessStrategy.calculate_weight(self.moves.board)
        self.root = Node(w)
        return self.root

#creation of the child
    def create_child(self, parent_node, newboard):
        weight = self.moves.chessStrategy.calculate_weight(newboard)
        child_node = Node(weight)
        parent_node.add_child(child_node)
        return child_node

#creation of the entire tree
    def create_tree(self, n):
        self.root = self.create_main_node()
        self.create_tree_bfs(self.root, n-1)
# creation of the tree with a bfs approach
    def create_tree_bfs(self, root_node, depth):
        queue = deque([(root_node, self.current_board, depth, True)])
        visited = set()
        while queue:
            current_node, current_board, current_depth, is_maximizing = queue.popleft()

            if current_depth <= 0:
                continue

            poss_positions = self.moves.find_new_state(current_board, current_depth, depth)

            for poss in poss_positions:

                new_data, piece = self.moves.new_board(poss[0], poss[1], poss[2], poss[3], current_board)


                if tuple(map(tuple, new_data)) not in visited:
                    child_node = self.create_child(current_node, new_data)

                    visited.add(tuple(map(tuple, new_data)))
                    if current_depth == depth:
                        self.hash_map_board[child_node] = new_data
                        self.hash_map_piece[child_node] = piece

                    next_player = not is_maximizing
                    queue.append((child_node, new_data, current_depth - 1, next_player))









