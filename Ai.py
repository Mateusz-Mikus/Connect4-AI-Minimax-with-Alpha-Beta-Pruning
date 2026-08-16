import Board
import random

def evaluate_window(window, piece):
    score = 0
    opp_piece = 1 if piece == 2 else 2

    if window.count(piece) == 3 and window.count(0) == 1:
        score += 50
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 10

    if window.count(opp_piece) == 2 and window.count(0) == 2:
        score -= 40
    elif window.count(opp_piece) == 3 and window.count(0) == 1:
        score -= 500

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

def undo_move(board, col):
    for r in range(6):
        if board[r][col] != 0:
            board[r][col] = 0
            return

def is_game_finished(board):
    if Board.check_win(board, 1):
        return True
    if Board.check_win(board, 2):
        return True

    for c in range(7):
        if Board.is_valid_location(board, c):
            return False
    return True



#def minimax_alpha_beta(board, depth, maximizingBot, alpha, beta):
    if depth == 0 or is_game_finished(board):
        if is_game_finished(board):
            if Board.check_win(board, 2):
                return 1000000
            elif Board.check_win(board, 1):
                return -1000000
            else:
                return 0
        else:
            return evaluate_board(board, 2)

    if maximizingBot:
        best_result = -100000000
        for col in range(7):
            if Board.is_valid_location(board, col):
                Board.drop_piece(board, col, 2)

                result = minimax_alpha_beta(board, depth-1, False, alpha, beta)

                undo_move(board, col)
                if result > best_result:
                    best_result = result

                    alpha = max(best_result, alpha)

                if alpha >= beta:
                    break

                
        return best_result  

    else:
        worst_result = 100000000
        for col in range(7):
            if Board.is_valid_location(board, col):
                Board.drop_piece(board, col, 1)

                result = minimax_alpha_beta(board, depth-1, True, alpha, beta)

                undo_move(board, col)

                if result < worst_result:
                    worst_result = result

                    beta = min(beta, worst_result)


                if alpha >= beta:
                    break
        return worst_result



def minimax(board, depth, maximizingBot):

    if depth == 0 or is_game_finished(board):
        if is_game_finished(board):
            if Board.check_win(board, 2):
                return 1000000
            elif Board.check_win(board, 1):
                return -1000000
            else:
                return 0
        else:
            return evaluate_board(board, 2)

    if maximizingBot:
        best_result = -100000000
        for col in range(7):
            if Board.is_valid_location(board, col):
                Board.drop_piece(board, col, 2)

                result = minimax(board, depth-1, False)

                undo_move(board, col)
                if result > best_result:
                    best_result = result
        return best_result

    else:
        worst_result = 100000000
        for col in range(7):
            if Board.is_valid_location(board, col):
                Board.drop_piece(board, col, 1)

                result = minimax(board, depth-1, True)

                undo_move(board, col)

                if result < worst_result:
                    worst_result = result
        return worst_result


def get_best_move(board, depth):
    valid_loc = [c for c in range(7) if Board.is_valid_location(board, c)]
    best_col = random.choice(valid_loc)
    best_result = -1000000000
    for col in range(7):
        if Board.is_valid_location(board, col):
            Board.drop_piece(board, col, 2)
            result = minimax(board, depth-1, False)
            undo_move(board, col)

            if result > best_result:
                best_result = result
                best_col = col
    return best_col
