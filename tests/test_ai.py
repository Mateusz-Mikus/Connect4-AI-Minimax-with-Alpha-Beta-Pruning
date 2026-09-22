from copy import deepcopy

import Ai
import Board

#Funkcja pomocnicza

def make_position(moves):
    board = Board.createBoard()
    piece = 1

    for col in moves:
        Board.drop_piece(board, col, piece)
        piece = 2 if piece == 1 else 1

    return board


def test_bot_chooses_winning_move():
    for with_alpha_beta in [False, True]:
        board = make_position([6,0,6,1,5,2,5])

        assert Ai.get_best_move(board, 2, with_alpha_beta) == 3


def test_bot_blocks_opponents_win():
    for with_alpha_beta in [False, True]:
        board = make_position([0,6,1,6,2])

        assert Ai.get_best_move(board, 2, with_alpha_beta) == 3

def test_search_does_not_change_board():
    for with_alpha_beta in [True, False]:
        board = make_position([3,2,4,3,0])

        before_board = deepcopy(board)

        move = Ai.get_best_move(board, 3, with_alpha_beta)

        assert before_board == board

def test_algorithms_return_same_score():
    for move in [[0,3,0,4,0,4], [3,2,4,3,0], []]:
        board = make_position(move)

        for depth in [1,2,3,4,5]:
            for maximizing_bot in [False, True]:
                score = Ai.minimax(board, depth, maximizing_bot)
                score_alpha_beta = Ai.minimax_alpha_beta(board, depth, maximizing_bot, -1000000000, 1000000000)

                assert score == score_alpha_beta