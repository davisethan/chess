from typing import Any, Dict, Set, Tuple
from abc import ABC
from Game import Game

class Piece(ABC):
    def __init__(self, color: str) -> None:
        self._color = color

    def get_color(self):
        return self._color

    def get_layout_destinations_from_origin(self, layout: Dict[Tuple[int], Any], origin: Tuple[int]) -> Set[Tuple[int]]:
        """
        layout: Dict[Tuple[int], Piece]
        destinations: Tuple[int]
        Set[Tuple[int]]
        """
        pass

    def _filter_layout_destinations_by_color(self, layout: Dict[Tuple[int], Any], destinations: Set[Tuple[int]]) -> Set[Tuple[int]]:
        """
        layout: Dict[Tuple[int], Piece]
        destinations: Set[Tuple[int]]
        Set[Tuple[int]]
        """
        return {destination for destination in destinations if destination not in layout or self._color != layout[destination].get_color()}

class Pawn(Piece):
    def get_layout_destinations_from_origin(self, layout: Dict[Tuple[int], Piece], origin: Tuple[int]) -> Set[Tuple[int]]:
        destinations = set()

        destinations |= self._get_pawn_layout_move_destinations_from_origin(layout, origin)
        destinations |= self._get_pawn_layout_attack_destinations_from_origin(layout, origin)

        return destinations

    def _get_pawn_layout_move_destinations_from_origin(self, layout: Dict[Tuple[int], Piece], origin: Tuple[int]) -> Set[Tuple[int]]:
        color = self._color
        row = origin[0]
        column = origin[1]
        if Game.WHITE == color:
            if Game.WHITE_PAWN_ROW == row:
                return {(row - 1, column), (row - 2, column)}
            elif 0 < row:
                return {(row - 1, column)}
            else:
                return set()
        elif Game.BLACK == color:
            if Game.BLACK_PAWN_ROW == row:
                return {(row + 1, column), (row + 2, column)}
            elif Game.SIZE - 1 > row:
                return {(row + 1, column)}
            else:
                return set()

    def _get_pawn_layout_attack_destinations_from_origin(self, layout: Dict[Tuple[int], Piece], origin: Tuple[int]) -> Set[Tuple[int]]:
        color = self._color
        if Game.WHITE == color:
            row = origin[0] - 1
        elif Game.BLACK == color:
            row = origin[0] + 1
        columns = (origin[1] - 1, origin[1] + 1)
        destinations = {(row, column) for column in columns if Game.SIZE > row and 0 <= column and Game.SIZE > column and (row, column) in layout and color != layout[(row, column)].get_color()}
        return destinations

class Knight(Piece):
    def get_layout_destinations_from_origin(self, layout: Dict[Tuple[int], Piece], origin: Tuple[int]) -> Set[Tuple[int]]:
        destinations = set()
        
        destinations |= self._get_up_vertical_destinations_from_origin(origin)
        destinations |= self._get_right_horizontal_destinations_from_origin(origin)
        destinations |= self._get_down_vertical_destinations_from_origin(origin)
        destinations |= self._get_left_horizontal_destinations_from_origin(origin)
        destinations = self._filter_layout_destinations_by_color(layout, destinations)

        return destinations

    def _get_up_vertical_destinations_from_origin(self, origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0] - 2
        columns = (origin[1] - 1, origin[1] + 1)
        up_vertical_destinations = {(row, column) for column in columns if 0 <= row and 0 <= column and Game.SIZE > column}
        return up_vertical_destinations

    def _get_right_horizontal_destinations_from_origin(self, origin: Tuple[int]) -> Set[Tuple[int]]:
        rows = (origin[0] - 1, origin[0] + 1)
        column = origin[1] + 2
        right_horizontal_destinations = {(row, column) for row in rows if 0 <= row and Game.SIZE > row and Game.SIZE > column}
        return right_horizontal_destinations

    def _get_down_vertical_destinations_from_origin(self, origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0] + 2
        columns = (origin[1] - 1, origin[1] + 1)
        down_vertical_destinations = {(row, column) for column in columns if Game.SIZE > row and 0 <= column and Game.SIZE > column}
        return down_vertical_destinations

    def _get_left_horizontal_destinations_from_origin(self, origin: Tuple[int]) -> Set[Tuple[int]]:
        rows = (origin[0] - 1, origin[0] + 1)
        column = origin[1] - 2
        left_horizontal_destinations = {(row, column) for row in rows if 0 <= row and Game.SIZE > row and 0 <= column}
        return left_horizontal_destinations

class Bishop(Piece):
    pass

class Rook(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass
