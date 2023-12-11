from NewState import NewState



class Maximizer:
    def __init__(self,player_sequence, board ):
        self.depth = 3
        self.newstate = NewState(player_sequence,board)
        self.newstate.create_tree(self.depth)
        self.board = board #old_board


    def minimax(self,node = None, depth=3, maximizingPlayer=True):
        if node is None:
            node = self.newstate.root
        if node.is_leaf() or depth == 0:
            return node.value

        if maximizingPlayer:
            best_value = float('-inf')
            for child_node in node.children:
                v = self.minimax(child_node, depth - 1, False)
                best_value = max(best_value, v)
            return best_value
        else:
            best_value = float('inf')
            for child_node in node.children:
                v = self.minimax(child_node, depth - 1, True)

                best_value = min(best_value, v)

        return best_value

    def find_new_state(self):
        best_value = self.minimax(None,  3, True)
        print("best",best_value)
        val = []
        for key, value in self.newstate.hash_map.items():
            print(key.value,value)
            if key.value == best_value:
                print(key.value)
                val = value
                return val

    def determine_final_position(self):
        new_board = self.find_new_state()
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

        start_pos = differences[0]
        end_pos = differences[1]

        start_piece = self.board[start_pos[0]][start_pos[1]]
        end_piece = new_board[end_pos[0]][end_pos[1]]

        print("Initial piece:", start_piece, "Pos init:", start_pos)
        print("Final piece:", end_piece, "Pos fin:", end_pos)
        if start_piece[1] not in self.newstate.moves.color_bot:
            temp = end_pos
            end_pos = start_pos
            start_pos = temp

        return start_pos,end_pos






if __name__ == "__main__":

    player_sequence = '0w01b2'
    board = [
        ['rw', 'nw', 'bw', 'qw', 'kw', 'bw', 'nw', 'rw'],
        ['pw', 'pw', '', 'pw', '', 'pw', 'pw', 'pw'],
        ['', '', 'pw', '', 'pw', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['pb', 'pb', '', '', '', '', '', ''],
        ['', '', 'pb', 'pb', 'pb', 'pb', 'pb', 'pb'],
        ['rb', 'nb', 'bb', 'kb', 'qb', 'bb', 'nb', 'rb']
    ]

    maximize = Maximizer(player_sequence,board)
    x_old, y_old = maximize.determine_final_position()
    print(x_old, y_old)
