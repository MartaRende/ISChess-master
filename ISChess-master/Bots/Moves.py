from Bots.Heuristics import Heuristics


class Moves:
    def __init__(self,player_sequence, board):
        self.heuristics = Heuristics(player_sequence, board)
        self.board = board
        self.color_bot = []
        self.color_bot= self.heuristics.color_bot # ex [w]
        self.color_adv = self.heuristics.color_adv
        self.color = self.color_bot
        self.count = 0

    def pawn(self, x, y, current_board):
        newPos = []
        board_length = len(current_board)
        print("pos", x, y)

        def is_valid_position(row, col):
            return 0 <= row < board_length and 0 <= col < board_length

        # Movimento in avanti
        new_x, new_y = x + 1, y
        if is_valid_position(new_x, new_y) and current_board[new_x][new_y] == '':
            newPos.append([x, y, new_x, new_y])

        # Verifica delle posizioni diagonali solo se esiste una pedina avversaria da mangiare
        for dx, dy in [(1, 1), (-1, 1)]:
            new_x, new_y = x + dx, y + dy
            if is_valid_position(new_x, new_y) and current_board[new_x][new_y]:
                if current_board[new_x][new_y][1] in self.color_adv:
                    newPos.append([x, y, new_x, new_y])

        print("ped", newPos)
        return newPos

    def rook(self, x, y, current_board):
        newPos = []
        board_length = len(current_board)


        for i in range(x + 1, board_length):
            if current_board[i][y] == '':
                newPos.append([x, y, i, y])
            elif current_board[i][y][1] not in self.color:
                newPos.append([x, y, i, y])
                break
            else:
                break

        for i in range(x - 1, -1, -1):
            if current_board[i][y] == '':
                newPos.append([x, y, i, y])
            elif current_board[i][y][1] not in self.color:
                newPos.append([x, y, i, y])
                break
            else:
                break

        for j in range(y + 1, board_length):
            if current_board[x][j] == '':
                newPos.append([x, y, x, j])
            elif current_board[x][j][1] not in self.color:
                newPos.append([x, y, x, j])
                break
            else:
                break

        for j in range(y - 1, -1, -1):
            if current_board[x][j] == '':
                newPos.append([x, y, x, j])
            elif current_board[x][j][1] not in self.color:
                newPos.append([x, y, x, j])
                break
            else:
                break

        print("rook", newPos)
        return newPos

    def king(self, x, y, current_board):
        newPos = []
        board_length = len(current_board)

        # Verifica le nuove posizioni all'interno dei limiti della griglia di gioco per il re
        possible_moves = [
            (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
            (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)
        ]

        for i, j in possible_moves:
            if 0 <= i < board_length and 0 <= j < board_length:
                if current_board[i][j] == '' or current_board[i][j][1] not in self.color:
                    newPos.append([x, y, i, j])

        print("king", newPos)
        return newPos

    def queen(self, x, y, current_board):
        newPos = []
        board_length = len(current_board)

        # Verifica le nuove posizioni all'interno dei limiti della griglia di gioco per la regina
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            i, j = x + dx, y + dy
            while 0 <= i < board_length and 0 <= j < board_length:
                if current_board[i][j] == '':
                    newPos.append([x, y, i, j])
                elif current_board[i][j][1] not in self.color:
                    newPos.append([x, y, i, j])
                    break
                else:
                    break
                i += dx
                j += dy

        print("queen", newPos)
        return newPos

    def bishop(self, x, y, current_board):
        newPos = []
        board_length = len(current_board)

        i, j = x + 1, y + 1
        while i < board_length and j < board_length:
            if current_board[i][j] == '':
                newPos.append([x, y, i, j])
            elif current_board[i][j][1] not in self.color:
                newPos.append([x, y, i, j])
                break
            else:
                break
            i += 1
            j += 1

        i, j = x - 1, y - 1
        while i >= 0 and j >= 0:
            if current_board[i][j] == '':
                newPos.append([x, y, i, j])
            elif current_board[i][j][1] not in self.color:
                newPos.append([x, y, i, j])
                break
            else:
                break
            i -= 1
            j -= 1

        i, j = x + 1, y - 1
        while i < board_length and j >= 0:
            if current_board[i][j] == '':
                newPos.append([x, y, i, j])
            elif current_board[i][j][1] not in self.color:
                newPos.append([x, y, i, j])
                break
            else:
                break
            i += 1
            j -= 1

        i, j = x - 1, y + 1
        while i >= 0 and j < board_length:
            if current_board[i][j] == '':
                newPos.append([x, y, i, j])
            elif current_board[i][j][1] not in self.color:
                newPos.append([x, y, i, j])
                break
            else:
                break
            i -= 1
            j += 1

        print("bishop", newPos)
        return newPos

    def knights(self, x, y, current_board):
        newPos = []
        board_length = len(current_board)

        possible_moves = [
            (x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1),
            (x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2)
        ]

        for i, j in possible_moves:
            if 0 <= i < board_length and 0 <= j < board_length:
                if current_board[i][j] == '' or current_board[i][j][1] not in self.color:
                    newPos.append([x, y, i, j])

        print("knights", newPos)
        return newPos

    def new_board(self, oldx, oldy, newx, newy,current_board):
        newdata = []

        for i in range(len(current_board)):
            row = []
            for j in range(len(current_board[i])):
                if i == newx and j == newy:
                    row.append(current_board[oldx][oldy])
                else:
                    row.append(current_board[i][j])
            newdata.append(row)
        print(newdata[oldx][oldy])
        newdata[oldx][oldy] = ''
        print(oldx,oldy,newx,newy)
        print("new board", newdata)
        return newdata

    def find_actual_color(self,current_depth,depth):
        if depth % 2 == 0:
            if current_depth % 2 == 0:
                self.color = self.color_bot
            else:
                self.color = self.color_adv
        else:
            if current_depth % 2 == 0:
                self.color = self.color_adv
            else:
                self.color = self.color_bot
        return self.color
    def find_new_state(self, current_board,current_depth,depth):
        all_poss_position = []
        self.color = self.find_actual_color(current_depth,depth)

        for i in range(len(current_board)):
            for j in range(len(current_board[i])):
                if current_board[i][j] != '':
                    print("board",current_board)
                    if current_board[i][j][0] == 'p' and current_board[i][j][1]in self.color:
                        all_poss_position += self.pawn(i,j,current_board)
                    if current_board[i][j][0] == 'r' and current_board[i][j][1]in self.color:
                        all_poss_position += self.rook(i,j,current_board)
                    if current_board[i][j][0] == 'n' and current_board[i][j][1]in self.color:
                        all_poss_position += self.knights(i,j,current_board)
                    if current_board[i][j][0] == 'b' and current_board[i][j][1]in self.color:
                        all_poss_position += self.bishop(i,j,current_board)
                    if current_board[i][j][0] == 'q' and current_board[i][j][1]in self.color:
                        all_poss_position += self.queen(i,j,current_board)
                    if current_board[i][j][0] == 'k'and current_board[i][j][1]in self.color:
                        all_poss_position += self.king(i,j,current_board)
        print(all_poss_position)

        return all_poss_position



