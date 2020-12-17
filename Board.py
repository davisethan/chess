from typing import Set, Tuple
from Game import Game
from Piece import Pawn, Knight, Bishop, Rook, Queen, King

class Board:
    def __init__(self, layout = {}) -> None:
        default_layout = {
            (7, 0): Rook(Game.WHITE),
            (7, 1): Knight(Game.WHITE),
            (7, 2): Bishop(Game.WHITE),
            (7, 3): Queen(Game.WHITE),
            (7, 4): King(Game.WHITE),
            (7, 5): Bishop(Game.WHITE),
            (7, 6): Knight(Game.WHITE),
            (7, 7): Rook(Game.WHITE),
            (6, 0): Pawn(Game.WHITE),
            (6, 1): Pawn(Game.WHITE),
            (6, 2): Pawn(Game.WHITE),
            (6, 3): Pawn(Game.WHITE),
            (6, 4): Pawn(Game.WHITE),
            (6, 5): Pawn(Game.WHITE),
            (6, 6): Pawn(Game.WHITE),
            (6, 7): Pawn(Game.WHITE),
            (1, 0): Pawn(Game.BLACK),
            (1, 1): Pawn(Game.BLACK),
            (1, 2): Pawn(Game.BLACK),
            (1, 3): Pawn(Game.BLACK),
            (1, 4): Pawn(Game.BLACK),
            (1, 5): Pawn(Game.BLACK),
            (1, 6): Pawn(Game.BLACK),
            (1, 7): Pawn(Game.BLACK),
            (0, 0): Rook(Game.BLACK),
            (0, 1): Knight(Game.BLACK),
            (0, 2): Bishop(Game.BLACK),
            (0, 3): Queen(Game.BLACK),
            (0, 4): King(Game.BLACK),
            (0, 5): Bishop(Game.BLACK),
            (0, 6): Knight(Game.BLACK),
            (0, 7): Rook(Game.BLACK)
        }

        self._layout = layout or default_layout

    def get_destinations_from_origin(self, origin: Tuple[int]) -> Set[Tuple[int]]:
        if origin not in self._layout:
            return set()
        piece = self._layout[origin]
        destinations = piece.get_layout_destinations_from_origin(self._layout, origin)
        return destinations

    def _get_point_from_square(self, square: str) -> Tuple[int]:
        """From [A-H][1-8] to ([0-7],[0-7])"""
        point_x = Game.ROWS[::-1].index(square[1])
        point_y = Game.COLUMNS.index(square[0])
        return (point_x, point_y)

    def _get_square_from_point(self, point: Tuple[int]) -> str:
        """From ([0-7],[0-7]) to [A-H][1-8]"""
        square_row = Game.ROWS[::-1][point[0]]
        square_column = Game.COLUMNS[point[1]]
        return f"{square_column}{square_row}"
