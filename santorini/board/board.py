"""
Class representing a Santorini board
"""


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

        if any(not (isinstance(cell, (int, list))) for cell in flat_board):
            raise BoardError(f"Cells must be int or list[int str]")

        if any(cell > Board.MAX_HEIGHT or cell < 0 for cell in flat_board if isinstance(cell, int)):
            raise BoardError(f"No cell can have height >{Board.MAX_HEIGHT} or <0")

        workers = set()

        for cell in filter(lambda cell: isinstance(cell, list), flat_board):
            if len(cell) != 2 or not (isinstance(cell[0], int) and isinstance(cell[1], str)):
                raise BoardError(f"Occupied cells must be list[int str], not {cell}")

            height, worker = cell

            if worker in workers:
                raise BoardError(f"Workers must be unique, {worker} was found twice")

            if height > Board.MAX_HEIGHT or height < 0:
                raise BoardError(f"No cell can have height > {Board.MAX_HEIGHT} or <0")

            if not any(worker == color + str(num)
                       for color in Board.COLORS
                       for num in range(1, 1 + Board.MAX_WORKERS)):
                raise BoardError(f"Workers must have format [color][number], not {worker}")

            workers.add(worker)

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
