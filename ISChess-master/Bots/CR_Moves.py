from Bots.CR_ChessStrategy import ChessStrategy


class Moves:
    def __init__(self,player_sequence, board):
        self.chessStrategy = ChessStrategy(player_sequence, board)
        self.board = board
        self.color_bot = []
        self.color_bot= self.chessStrategy.color_bot
        self.color_adv = self.chessStrategy.color_adv
        self.color = self.color_adv
# function for all possibles movements of pieces
# they return an array with all possible positions of all pieces in a board
    def pawn(self, x, y, current_board):
        newPos = []
        board_length = len(current_board)
        direction = 1 if self.color == self.color_bot else -1  # Determine pawn's direction based on its color

        def is_valid_move(dx, dy):
            return 0 <= x + dx < board_length and 0 <= y + dy < board_length

        def can_move(dx, dy):
            return is_valid_move(dx, dy) and current_board[x + dx][y + dy] == ''

        def can_capture(dx, dy):
            return is_valid_move(dx, dy) and current_board[x + dx][y + dy] != '' and current_board[x + dx][y + dy][
                1] not in self.color

        if can_move(direction, 0):  # Moving one step forward
            newPos.append([x, y, x + direction, y])

        if can_capture(direction, -1):  # Capture diagonally left
            newPos.append([x, y, x + direction, y - 1])
        if can_capture(direction, 1):  # Capture diagonally right
            newPos.append([x, y, x + direction, y + 1])

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

        return newPos

    def king(self, x, y, current_board):
        newPos = []
        board_length = len(current_board)

        possible_moves = [
            (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
            (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)
        ]

        for i, j in possible_moves:
            if 0 <= i < board_length and 0 <= j < board_length:
                if current_board[i][j] == '' or current_board[i][j][1] not in self.color:
                    newPos.append([x, y, i, j])
                elif current_board[i][j][0] == 'p' and current_board[i][j][1] not in self.color:
                    newPos.append([x, y, i, j])
                    break
        return newPos

    def queen(self, x, y, current_board):
        newPos = []
        board_length = len(current_board)
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
                elif current_board[i][j][0] == 'p' and current_board[i][j][1] not in self.color:
                    newPos.append([x, y, i, j])
                    break

        return newPos
# function that create a possible future board
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
        piece = newdata[oldx][oldy]
        newdata[oldx][oldy] = ''
        return newdata,piece
# for dividing the color of the bot and the color of the adversary --> it works only for 1vs1
    def find_actual_color(self,current_depth,depth):
        if (depth % 2) == 0:
            if current_depth %2 ==0:
                self.color = self.color_bot
            else:
                self.color=self.color_adv
        else :
            if current_depth %2 !=0:
                self.color = self.color_bot
            else:
                self.color=self.color_adv
        return self.color
# this function put in an array all the possible positions for all pieces
    def find_new_state(self, current_board,current_depth,depth):
        all_poss_position = []
        self.color = self.find_actual_color(current_depth,depth)

        for i in range(len(current_board)):
            for j in range(len(current_board[i])):
                if current_board[i][j] != '':
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
        return all_poss_position



