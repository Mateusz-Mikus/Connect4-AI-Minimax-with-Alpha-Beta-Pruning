def createBoard():
    return [[0 for c in range(7)] for r in range(6)]

def printBoard(board):
    for i in board:
        print(i)

def drop_piece(board, col, piece):
    for r in range(5, -1, -1):
        if board[r][col] == 0:
            board[r][col] = piece
            return


def check_win(board, piece):
    for r in range(6):
        for c in range(4):
            if (board[r][c] == piece and
                board[r][c+1] == piece and
                board[r][c+2] == piece and
                board[r][c+3] == piece):
                return True

    for c in range(7):
        for r in range(3):
            if (board[r][c] == piece and
                board[r+1][c] == piece and
                board[r+2][c] == piece and
                board[r+3][c] == piece):
                return True
    
    for c in range(4):
        for r in range(3, 6):
            if (board[r][c] == piece and
                board[r-1][c+1] == piece and
                board[r-2][c+2] == piece and
                board[r-3][c+3] == piece):
                return True
            
    for c in range(4):
        for r in range(3):
            if (board[r][c] == piece and
                board[r+1][c+1] == piece and
                board[r+2][c+2] == piece and
                board[r+3][c+3] == piece):
                return True

