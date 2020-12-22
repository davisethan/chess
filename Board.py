from typing import Dict, Set, Tuple
from Game import Game
from Piece import Piece, Pawn, Knight, Bishop, Rook, Queen, King

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
        self._moves = []

    def add_move(self, move: str) -> None:
        self._moves.append(move)

    def _can_move_from_origin_to_destination(self, origin: Tuple[int], destination: Tuple[int]) -> bool:
        if not self._origin_correct_color(origin):
            return False
        elif destination not in self._get_destinations_from_origin(origin):
            return False
        elif self._current_king_check_from_origin_to_destination(origin, destination):
            return False
        else:
            return True

    def _origin_correct_color(self, origin: Tuple[int]) -> bool:
        piece = self._layout[origin]
        if 0 == len(self._moves) % 2 and Game.WHITE == piece.get_color():
            return True
        elif 1 == len(self._moves) % 2 and Game.BLACK == piece.get_color():
            return True
        else:
            return False

    def _get_destinations_from_origin(self, origin: Tuple[int]) -> Set[Tuple[int]]:
        if origin not in self._layout:
            return set()
        piece = self._layout[origin]
        destinations = piece.get_layout_destinations_from_origin(self._layout, origin)
        return destinations

    def _current_king_check_from_origin_to_destination(self, origin: Tuple[int], destination: Tuple[int]) -> bool:
        current_color = self._get_current_color()
        other_color = self._get_other_color()
        layout_copy = self._get_layout_from_origin_to_destination(origin, destination)
        current_king_origin = self._get_current_king_origin_from_current_color_and_layout(current_color, layout_copy)
        other_pieces_destinations = self._get_other_pieces_destinations_from_other_color_and_layout(other_color, layout_copy)

        return current_king_origin in other_pieces_destinations

    def _get_current_color(self) -> str:
        if 0 == len(self._moves) % 2:
            return Game.WHITE
        else:
            return Game.BLACK

    def _get_other_color(self) -> str:
        if 0 == len(self._moves) % 2:
            return Game.BLACK
        else:
            return Game.WHITE

    def _get_layout_from_origin_to_destination(self, origin: Tuple[int], destination: Tuple[int]) -> Dict[Tuple[int], Piece]:
        layout_copy = dict(self._layout)
        layout_copy[destination] = layout_copy[origin]
        del layout_copy[origin]

        return layout_copy

    def _get_current_king_origin_from_current_color_and_layout(self, current_color: str, layout: Dict[Tuple[int], Piece]) -> Tuple[int]:
        current_king_origin = tuple()
        
        for origin in layout:
            piece = layout[origin]
            if isinstance(piece, King) and current_color == piece.get_color():
                current_king_origin = origin

        return current_king_origin

    def _get_other_pieces_destinations_from_other_color_and_layout(self, other_color: str, layout: Dict[Tuple[int], Piece]) -> Set[Tuple[int]]:
        other_pieces_destinations = set()
        
        for origin in layout:
            piece = layout[origin]
            if other_color == piece.get_color():
                other_pieces_destinations |= piece.get_layout_destinations_from_origin(layout, origin)

        return other_pieces_destinations

    # def _get_point_from_square(self, square: str) -> Tuple[int]:
    #     """From [A-H][1-8] to ([0-7],[0-7])"""
    #     point_x = Game.ROWS[::-1].index(square[1])
    #     point_y = Game.COLUMNS.index(square[0])
    #     return (point_x, point_y)

    # def _get_square_from_point(self, point: Tuple[int]) -> str:
    #     """From ([0-7],[0-7]) to [A-H][1-8]"""
    #     square_row = Game.ROWS[::-1][point[0]]
    #     square_column = Game.COLUMNS[point[1]]
    #     return f"{square_column}{square_row}"
