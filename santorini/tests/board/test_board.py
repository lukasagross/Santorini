import pytest

from santorini.board.board import Board, BoardError


def test_valid_init():
    board1 = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]

    assert Board(board1).board == board1

    board2 = [[0, 0, 0, 0, 0],
              [0, 3, 0, 0, 2],
              [0, 0, 1, 0, 0],
              [1, 0, 0, 1, 0],
              [0, 0, 4, 0, 0]]

    assert Board(board2).board == board2

    board3 = [[0, [2, "white1"], 0, 0, 0],
              [0, 3, 0, 0, [2, "blue2"]],
              [0, 0, [1, "blue1"], 0, 0],
              [[1, "white2"], 0, 0, 1, 0],
              [0, 0, 4, 0, 0]]

    assert Board(board3).board == board3


def test_invalid_init():
    board1 = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]

    with pytest.raises(BoardError):
        # Wrong Width
        assert Board(board1).board == board1

    board2 = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]

    with pytest.raises(BoardError):
        # Wrong length
        assert Board(board2).board == board2

    board3 = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 5, 0],
              [0, 0, 0, 0, 0]]

    with pytest.raises(BoardError):
        # Height larger than max height
        assert Board(board3).board == board3

    board4 = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, "blue1"],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]

    with pytest.raises(BoardError):
        # Cell not instance of int
        assert Board(board4).board == board4

    board5 = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [[0, "white1", "white2"], 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]

    with pytest.raises(BoardError):
        # Occupied cell list has length 3
        assert Board(board5).board == board5

    board6 = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [["blue1", "white1"], 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]

    with pytest.raises(BoardError):
        # Occupied cell height is not int
        assert Board(board6).board == board6

    board7 = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [[0, 0], 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]

    with pytest.raises(BoardError):
        # Occupied cell worker is not str
        assert Board(board7).board == board7

    board8 = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [-1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]

    with pytest.raises(BoardError):
        # Cell has negative height
        assert Board(board8).board == board8

    board9 = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [[-1, "white1"], 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]

    with pytest.raises(BoardError):
        # Occupied cell has negative height
        assert Board(board9).board == board9

    board10 = [[0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [[0, "red1"], 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]]

    with pytest.raises(BoardError):
        # Occupied cell has invalid worker
        assert Board(board10).board == board10

    board11 = [[0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [[0, "blue0"], 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]]

    with pytest.raises(BoardError):
        # Occupied cell has invalid worker
        assert Board(board11).board == board11

    board12 = [[0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [[0, "blue4"], 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]]

    with pytest.raises(BoardError):
        # Occupied cell has invalid worker
        assert Board(board12).board == board12

    board13 = [[0, 0, 0, 0, 0],
               [[0, "blue1"], 0, 0, 0, 0],
               [[0, "blue1"], 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]]

    with pytest.raises(BoardError):
        # Duplicated worker
        assert Board(board13).board == board13
