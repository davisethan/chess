from typing import Set, Tuple
from abc import ABC
from Game import Game

class Piece(ABC):
    def __init__(self, color: str) -> None:
        self._color = color

    def get_color(self):
        return self._color

    def get_destinations_from_origin(self, origin: str) -> Set[str]:
        pass

    def is_destination_from_origin(self, origin:str, destination: str) -> bool:
        destinations = self.get_destinations_from_origin(origin)
        return destination in destinations

    def _get_point_from_square(self, square: str) -> Tuple[int]:
        point_x = Game.ROWS[::-1].index(square[1])
        point_y = Game.COLUMNS.index(square[0])
        return (point_x, point_y)

    def _get_square_from_point(self, point: Tuple[int]) -> str:
        square_row = Game.ROWS[::-1][point[0]]
        square_column = Game.COLUMNS[point[1]]
        return f"{square_column}{square_row}"

class Pawn(Piece):
    pass

class Knight(Piece):
    def get_destinations_from_origin(self, origin: str) -> Set[str]:
        destinations = set()
        
        destinations |= self._get_up_vertical_destinations_from_origin(origin)
        destinations |= self._get_right_horizontal_destinations_from_origin(origin)
        destinations |= self._get_down_vertical_destinations_from_origin(origin)
        destinations |= self._get_left_horizontal_destinations_from_origin(origin)
        
        return destinations

    def _get_up_vertical_destinations_from_origin(self, origin: str) -> Set[str]:
        point = self._get_point_from_square(origin)
        row = point[0] - 2
        columns = (point[1] - 1, point[1] + 1,)
        up_vertical_destinations = {f"{self._get_square_from_point((row, column))}" for column in columns if 0 <= row and 0 <= column and Game.SIZE > column}
        return up_vertical_destinations

    def _get_right_horizontal_destinations_from_origin(self, origin: str) -> Set[str]:
        point = self._get_point_from_square(origin)
        rows = (point[0] - 1, point[0] + 1,)
        column = point[1] + 2
        right_horizontal_destinations = {f"{self._get_square_from_point((row, column))}" for row in rows if 0 <= row and Game.SIZE > row and Game.SIZE > column}
        return right_horizontal_destinations

    def _get_down_vertical_destinations_from_origin(self, origin: str) -> Set[str]:
        point = self._get_point_from_square(origin)
        row = point[0] + 2
        columns = (point[1] - 1, point[1] + 1,)
        down_vertical_destinations = {f"{self._get_square_from_point((row, column))}" for column in columns if Game.SIZE > row and 0 <= column and Game.SIZE > column}
        return down_vertical_destinations

    def _get_left_horizontal_destinations_from_origin(self, origin: str) -> Set[str]:
        point = self._get_point_from_square(origin)
        rows = (point[0] - 1, point[0] + 1,)
        column = point[1] - 2
        left_horizontal_destinations = {f"{self._get_square_from_point((row, column))}" for row in rows if 0 <= row and Game.SIZE > row and 0 <= column}
        return left_horizontal_destinations

class Bishop(Piece):
    pass

class Rook(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass
