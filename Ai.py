def evaluate_window(window, piece):
    score = 0
    opp_piece = 1 if piece == 2 else 2
    if window.count(piece) == 4:
        score += 10000
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 50
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 10

    if window.count(opp_piece) == 2 and window.count(0) == 2:
        score -= 40
    elif window.count(opp_piece) == 3 and window.count(0) == 1:
        score -= 500
    elif window.count(opp_piece) == 4:
        score -= 10000

    return score

def evaluate_board(board, piece):
    score = 0

    for c in range(7):
        for r in range(3):
            window = [board[r+i][c] for i in range(4)]
            score += evaluate_window(window, piece)

    for r in range(6):
        for c in range(4):
            window = [board[r][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    for c in range(4):
        for r in range(3, 6):
            window = [board[r-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    for c in range(4):
        for r in range(3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score