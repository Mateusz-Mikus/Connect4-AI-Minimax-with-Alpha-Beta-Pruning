import Board

def test_pieces_fall_and_stack():
    board = Board.createBoard()

    Board.drop_piece(board, 3, 1)
    Board.drop_piece(board, 3, 2)

    assert board[5][3] == 1
    assert board[4][3] == 2
    assert board[3][3] == 0


def test_full_column_does_not_accept_another_piece():
    board = Board.createBoard()

    for piece in [1, 2, 1, 2, 1, 2]:
        Board.drop_piece(board, 0, piece)

    assert Board.is_valid_location(board, 0) is False

    Board.drop_piece(board, 0, 1)

    column = [board[row][0] for row in range(6)]

    assert column == [2, 1, 2, 1, 2, 1]

    assert Board.is_valid_location(board, 1) is True


def test_horizontal_win():
    for piece in [1, 2]:
        board = Board.createBoard()

        for c in [2,3,4,5]:
            Board.drop_piece(board, c, piece)

        assert Board.check_win(board, piece) is True



def test_vertical_win():
    for piece in [1, 2]:
        board = Board.createBoard()

        for _ in range(4):
            Board.drop_piece(board, 2, piece)

        assert Board.check_win(board, piece) is True


def test_diagonal_win_upwards():
    for piece in [1,2]:
        board = Board.createBoard()

        board[5][0] = piece
        board[4][1] = piece
        board[3][2] = piece
        board[2][3] = piece

        assert Board.check_win(board, piece) is True

def test_diagonal_win_downwards():
    for piece in [1,2]:
        board = Board.createBoard()

        board[2][3] = piece
        board[3][4] = piece
        board[4][5] = piece
        board[5][6] = piece

        assert Board.check_win(board, piece) is True