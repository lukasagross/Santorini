"""
Class representing a Santorini board
"""

from itertools import chain
from operator import itemgetter



class BoardError(Exception):
    """
    Exception raised by the Board class when building invalid boards
    """


class Board:
    """
    Class representing a Santorini board
    """
    LENGTH = 5
    WIDTH = 5
    MAX_HEIGHT = 4
    MAX_WORKERS = 3
    COLORS = ["white", "blue"]

    def __init__(self, board):
        if len(board) != Board.WIDTH or any(len(row) != Board.LENGTH for row in board):
            raise BoardError(f"Board dimensions must be {Board.LENGTH}x{Board.WIDTH}")

        flat_board = [cell for row in board for cell in row]

        def is_unoccupied(cell):
            return isinstance(cell, int)

        unoccupied = list(filter(is_unoccupied, flat_board))

        def is_occupied(cell):
            return (isinstance(cell, list)
                    and len(cell) == 2
                    and isinstance(cell[0], int)
                    and isinstance(cell[1], str))

        occupied = list(filter(is_occupied, flat_board))

        if len(unoccupied) + len(occupied) != Board.LENGTH * Board.WIDTH:
            raise BoardError(f"Cells must be int or list[int str]")

        if not all(0 <= cell <= Board.MAX_HEIGHT for cell in chain(unoccupied, map(itemgetter(0), occupied))):
            raise BoardError(f"No cell can have height >{Board.MAX_HEIGHT} or <0")

        workers = list(map(itemgetter(1), occupied))

        if len(workers) != len(set(workers)):
            raise BoardError("Workers must be unique")

        def is_worker(worker):
            for color in Board.COLORS:
                for num in range(1, 1 + Board.MAX_WORKERS):
                    if worker == color + str(num):
                        return True
            return False

        if not all(is_worker(worker) for worker in workers):
            raise BoardError("Workers must have format [color][number]")

        self.board = board

    def place_worker(self, worker, pos):
        """
        Create a new board with a new worker at pos
        :param worker: string name of the worker
        :param pos: list[int int] position to place the worker
        :return: Board with the new worker at pos
        :raise: BoardError if pos is an occupied cell or does not exist
        """

    def move_worker(self, worker, direction):
        """
        Create a new board with a worker moved one cell over
        :param worker: string name of the worker
        :param direction: string name of the direction
        :return: Board with the worker moved one unit
        :raise: BoardError if the destination cell does not exist
        """
