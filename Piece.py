from typing import Any, Dict, Set, Tuple
from abc import ABC
from Game import Game

class Piece(ABC):
    def __init__(self, color: str = Game.WHITE) -> None:
        self._color = color

    def __eq__(self, other):
        return type(self) == type(other) and self._color == other._color

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
    def get_layout_destinations_from_origin(self, layout: Dict[Tuple[int], Piece], origin: Tuple[int]) -> Set[Tuple[int]]:
        destinations = set()

        destinations |= self._get_layout_up_right_diagonal_destinations_from_origin(layout, origin)
        destinations |= self._get_layout_down_right_diagonal_destinations_from_origin(layout, origin)
        destinations |= self._get_layout_down_left_diagonal_destinations_from_origin(layout, origin)
        destinations |= self._get_layout_up_left_diagonal_destinations_from_origin(layout, origin)

        return destinations

    def _get_layout_up_right_diagonal_destinations_from_origin(self, layout: Dict[Tuple[int], Piece], origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0]
        column = origin[1]
        up_right_diagonal_destinations = set()
        index = 1
        destination = (row - index, column + index)

        while 0 <= row - index and Game.SIZE > column + index and destination not in layout:
            up_right_diagonal_destinations.add(destination)
            index += 1
            destination = (row - index, column + index)

        if destination in layout and self._color != layout[destination].get_color():
            up_right_diagonal_destinations.add(destination)

        return up_right_diagonal_destinations

    def _get_layout_down_right_diagonal_destinations_from_origin(self, layout: Dict[Tuple[int], Piece], origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0]
        column = origin[1]
        down_right_diagonal_destinations = set()
        index = 1
        destination = (row + index, column + index)

        while Game.SIZE > row + index and Game.SIZE > column + index and destination not in layout:
            down_right_diagonal_destinations.add(destination)
            index += 1
            destination = (row + index, column + index)

        if destination in layout and self._color != layout[destination].get_color():
            down_right_diagonal_destinations.add(destination)

        return down_right_diagonal_destinations

    def _get_layout_down_left_diagonal_destinations_from_origin(self, layout: Dict[Tuple[int], Piece], origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0]
        column = origin[1]
        down_left_diagonal_destinations = set()
        index = 1
        destination = (row + index, column - index)

        while Game.SIZE > row + index and 0 <= column - index and destination not in layout:
            down_left_diagonal_destinations.add(destination)
            index += 1
            destination = (row + index, column - index)

        if destination in layout and self._color != layout[destination].get_color():
            down_left_diagonal_destinations.add(destination)

        return down_left_diagonal_destinations

    def _get_layout_up_left_diagonal_destinations_from_origin(self, layout: Dict[Tuple[int], Piece], origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0]
        column = origin[1]
        up_left_diagonal_destinations = set()
        index = 1
        destination = (row - index, column - index)

        while 0 <= row - index and 0 <= column - index and destination not in layout:
            up_left_diagonal_destinations.add(destination)
            index += 1
            destination = (row - index, column - index)

        if destination in layout and self._color != layout[destination].get_color():
            up_left_diagonal_destinations.add(destination)

        return up_left_diagonal_destinations

class Rook(Piece):
    def get_layout_destinations_from_origin(self, layout: Dict[Tuple[int], Piece], origin: Tuple[int]) -> Set[Tuple[int]]:
        destinations = set()

        destinations |= self._get_layout_up_vertical_destinations_from_origin(layout, origin)
        destinations |= self._get_layout_right_horizontal_destinations_from_origin(layout, origin)
        destinations |= self._get_layout_down_vertical_destinations_from_origin(layout, origin)
        destinations |= self._get_layout_left_horizontal_destinations_from_origin(layout, origin)

        return destinations

    def _get_layout_up_vertical_destinations_from_origin(self, layout: Dict[Tuple[int], Piece], origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0]
        column = origin[1]
        up_vertical_destinations = set()
        index = 1
        destination = (row - index, column)

        while 0 <= row - index and destination not in layout:
            up_vertical_destinations.add(destination)
            index += 1
            destination = (row - index, column)

        if destination in layout and self._color != layout[destination].get_color():
            up_vertical_destinations.add(destination)

        return up_vertical_destinations

    def _get_layout_right_horizontal_destinations_from_origin(self, layout: Dict[Tuple[int], Piece], origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0]
        column = origin[1]
        right_horizontal_destinations = set()
        index = 1
        destination = (row, column + index)

        while Game.SIZE > column + index and destination not in layout:
            right_horizontal_destinations.add(destination)
            index += 1
            destination = (row, column + index)

        if destination in layout and self._color != layout[destination].get_color():
            right_horizontal_destinations.add(destination)

        return right_horizontal_destinations

    def _get_layout_down_vertical_destinations_from_origin(self, layout: Dict[Tuple[int], Piece], origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0]
        column = origin[1]
        down_vertical_destinations = set()
        index = 1
        destination = (row + index, column)

        while Game.SIZE > row + index and destination not in layout:
            down_vertical_destinations.add(destination)
            index += 1
            destination = (row + index, column)

        if destination in layout and self._color != layout[destination].get_color():
            down_vertical_destinations.add(destination)

        return down_vertical_destinations

    def _get_layout_left_horizontal_destinations_from_origin(self, layout: Dict[Tuple[int], Piece], origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0]
        column = origin[1]
        left_horizontal_destinations = set()
        index = 1
        destination = (row, column - index)

        while 0 <= column - index and destination not in layout:
            left_horizontal_destinations.add(destination)
            index += 1
            destination = (row, column - index)

        if destination in layout and self._color != layout[destination].get_color():
            left_horizontal_destinations.add(destination)

        return left_horizontal_destinations

class Queen(Piece):
    def get_layout_destinations_from_origin(self, layout: Dict[Tuple[int], Piece], origin: Tuple[int]) -> Set[Tuple[int]]:
        destinations = set()

        destinations |= Bishop().get_layout_destinations_from_origin(layout, origin)
        destinations |= Rook().get_layout_destinations_from_origin(layout, origin)

        return destinations

class King(Piece):
    def get_layout_destinations_from_origin(self, layout: Dict[Tuple[int], Piece], origin: Tuple[int]) -> Set[Tuple[int]]:
        destinations = set()

        destinations |= self._get_up_vertical_destinations_from_origin(origin)
        destinations |= self._get_up_right_diagonal_destinations_from_origin(origin)
        destinations |= self._get_right_horizontal_destinations_from_origin(origin)
        destinations |= self._get_down_right_diagonal_destinations_from_origin(origin)
        destinations |= self._get_down_vertical_destinations_from_origin(origin)
        destinations |= self._get_down_left_diagonal_destinations_from_origin(origin)
        destinations |= self._get_left_horizontal_destinations_from_origin(origin)
        destinations |= self._get_up_left_diagonal_destinations_from_origin(origin)
        destinations = self._filter_layout_destinations_by_color(layout, destinations)

        return destinations

    def _get_up_vertical_destinations_from_origin(self, origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0]
        column = origin[1]
        destinations = set()
        
        if 0 <= row - 1:
            destinations.add((row - 1, column))

        return destinations

    def _get_up_right_diagonal_destinations_from_origin(self, origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0]
        column = origin[1]
        destinations = set()
        
        if 0 <= row - 1 and Game.SIZE > column + 1:
            destinations.add((row - 1, column + 1))

        return destinations

    def _get_right_horizontal_destinations_from_origin(self, origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0]
        column = origin[1]
        destinations = set()
        
        if Game.SIZE > column + 1:
            destinations.add((row, column + 1))

        return destinations

    def _get_down_right_diagonal_destinations_from_origin(self, origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0]
        column = origin[1]
        destinations = set()
        
        if Game.SIZE > row + 1 and Game.SIZE > column + 1:
            destinations.add((row + 1, column + 1))

        return destinations

    def _get_down_vertical_destinations_from_origin(self, origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0]
        column = origin[1]
        destinations = set()
        
        if Game.SIZE > row + 1:
            destinations.add((row + 1, column))

        return destinations

    def _get_down_left_diagonal_destinations_from_origin(self, origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0]
        column = origin[1]
        destinations = set()
        
        if Game.SIZE > row + 1 and 0 <= column - 1:
            destinations.add((row + 1, column - 1))

        return destinations

    def _get_left_horizontal_destinations_from_origin(self, origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0]
        column = origin[1]
        destinations = set()
        
        if 0 <= column - 1:
            destinations.add((row, column - 1))

        return destinations

    def _get_up_left_diagonal_destinations_from_origin(self, origin: Tuple[int]) -> Set[Tuple[int]]:
        row = origin[0]
        column = origin[1]
        destinations = set()
        
        if 0 <= row - 1 and 0 <= column - 1:
            destinations.add((row - 1, column - 1))

        return destinations
