import re
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
        self._move = ""


    def king_with_color_check(self, color: str) -> bool:
        king_origin = tuple()
        for origin in self._layout:
            if isinstance(self._layout[origin], King) and color == self._layout[origin].get_color():
                king_origin = origin

        king_check = False
        for origin in self._layout:
            if color != self._layout[origin].get_color() and king_origin in self._get_destinations_from_origin(origin):
                king_check = True
        return king_check


    def move_from_origin_to_destination_makes_king_with_color_check(self, origin: Tuple[int], destination: Tuple[int], color: str) -> bool:
        memento = dict(self._layout)
        # Do move
        self._layout[destination] = self._layout[origin]
        self._layout.pop(origin)
        # King check
        king_check = self.king_with_color_check(color)
        # if king_check:
        self._layout = memento
        return king_check

    def king_with_color_can_move(self, color: str) -> bool:
        king_origin = tuple()
        for origin in self._layout:
            if isinstance(self._layout[origin], King) and color == self._layout[origin].get_color():
                king_origin = origin
        king_destinations = self._get_destinations_from_origin(king_origin)

        other_color_destinations = set()
        for origin in self._layout:
            if color != self._layout[origin].get_color():
                other_color_destinations |= self._get_destinations_from_origin(origin)

        return 0 < len(king_destinations - other_color_destinations)

    def can_capture_king_with_color_attacker(self, color: str) -> bool:
        king_origin = tuple()
        for origin in self._layout:
            if isinstance(self._layout[origin], King) and color == self._layout[origin].get_color():
                king_origin = origin

        king_attacker_origins = set()
        for origin in self._layout:
            if king_origin in self._get_destinations_from_origin(origin):
                king_attacker_origins.add(origin)

        if 1 < len(king_attacker_origins):
            return False
        king_attacker_origin = tuple(king_attacker_origins)[0]
        
        capture_king_attacker_origins = set()
        for origin in self._layout:
            if king_attacker_origin in self._get_destinations_from_origin(origin):
                capture_king_attacker_origins.add(origin)
        can_capture_king_attacker = False
        for capture_king_attack_origin in capture_king_attacker_origins:
            if not self.move_from_origin_to_destination_makes_king_with_color_check(capture_king_attack_origin, king_attacker_origin, color):
                can_capture_king_attacker = True

        return can_capture_king_attacker

    def can_block_king_with_color_attacker(self, color: str) -> bool:
        king_origin = tuple()
        for origin in self._layout:
            if isinstance(self._layout[origin], King) and color == self._layout[origin].get_color():
                king_origin = origin

        king_attacker_origin = tuple()
        for origin in self._layout:
            if king_origin in self._get_destinations_from_origin(origin):
                king_attacker_origin = origin

        destinations = set()
        row = king_origin[0]
        column = king_origin[1]
        other_row = king_attacker_origin[0]
        other_column = king_attacker_origin[1]
        # up vertical
        if row > other_row and column == other_column:
            index = 1
            destination = (row - index, column)
            while king_attacker_origin != destination:
                destinations.add(destination)
                index += 1
                destination = (row - index, column)
        # up right diagonal
        elif row > other_row and column < other_column and abs(row - other_row) == abs(column - other_column):
            index = 1
            destination = (row - index, column + index)
            while king_attacker_origin != destination:
                destinations.add(destination)
                index += 1
                destination = (row - index, column + index)
        # right horizontal
        elif row == other_row and column < other_column:
            index = 1
            destination = (row, column + index)
            while king_attacker_origin != destination:
                destinations.add(destination)
                index += 1
                destination = (row, column + index)
        # right down diagonal
        elif row < other_row and column < other_column:
            index = 1
            destination = (row + index, column + index)
            while king_attacker_origin != destination:
                destinations.add(destination)
                index += 1
                destination = (row + index, column + index)
        # down vertical
        elif row < other_row and column == other_column:
            index = 1
            destination = (row + index, column)
            while king_attacker_origin != destination:
                destinations.add(destination)
                index += 1
                destination = (row + index, column)
        # down left diagonal
        elif row < other_row and column > other_column:
            index = 1
            destination = (row + index, column - index)
            while king_attacker_origin != destination:
                destinations.add(destination)
                index += 1
                destination = (row + index, column - index)
        # left horizontal
        elif row == other_row and column > other_column:
            index = 1
            destination = (row, column - index)
            while king_attacker_origin != destination:
                destinations.add(destination)
                index += 1
                destination = (row, column - index)
        # up left diagonal
        elif row > other_row and column > other_column:
            index = 1
            destination = (row - index, column - index)
            while king_attacker_origin != destination:
                destinations.add(destination)
                index += 1
                destination = (row - index, column - index)

        block_king_attacker_origins = set()
        for origin in self._layout:
            if color == self._layout[origin].get_color() and 0 < len(destinations & self._get_destinations_from_origin(origin)):
                block_king_attacker_origins.add(origin)
        can_block_king_attacker = False
        for block_king_attacker_origin in block_king_attacker_origins:
            for destination in destinations:
                if not self.move_from_origin_to_destination_makes_king_with_color_check(block_king_attacker_origin, destination, color):
                    can_block_king_attacker = True

        return can_block_king_attacker


    def set_move(self, move: str) -> None:
        self._move = move

    def can_move(self) -> bool:
        if not self._is_correct_move_format():
            return False
        elif not self._is_correct_origin_piece():
            return False
        elif not self._is_correct_origin_color():
            return False
        elif not self._can_move_from_origin_to_destination():
            return False
        elif not self._is_king_check_by_color(self._get_current_color()):
            return False
        else:
            return True

    def _is_correct_move_format(self) -> bool:
        regex = "^[P|N|B|R|Q|K][A-H][1-8][A-H][1-8]$"
        return None != re.search(regex, self._move)

    def _is_correct_origin_piece(self) -> bool:
        origin = self._get_origin_from_move()
        move_piece = self._move[0]
        if "P" == move_piece and origin in self._layout and isinstance(self._layout[origin], Pawn):
            return True
        elif "N" == move_piece and origin in self._layout and isinstance(self._layout[origin], Knight):
            return True
        elif "B" == move_piece and origin in self._layout and isinstance(self._layout[origin], Bishop):
            return True
        elif "R" == move_piece and origin in self._layout and isinstance(self._layout[origin], Rook):
            return True
        elif "Q" == move_piece and origin in self._layout and isinstance(self._layout[origin], Queen):
            return True
        elif "K" == move_piece and origin in self._layout and isinstance(self._layout[origin], King):
            return True
        else:
            return False

    def _get_origin_from_move(self) -> Tuple[int]:
        move_origin = self._move[1:3]
        row = Game.ROWS[::-1].index(move_origin[1])
        column = Game.COLUMNS.index(move_origin[0])
        return (row, column)

    # def _is_correct_origin_color(self) -> bool:
    #     current_color = 

    # def add_move(self, move: str) -> None:
    #     self._moves.append(move)

    # def _can_move_from_origin_to_destination(self, origin: Tuple[int], destination: Tuple[int]) -> bool:
    #     if not self._origin_correct_color(origin):
    #         return False
    #     elif not Piece.is_layout_destination_from_origin(layout, destination, origin):
    #         return False
    #     elif self._current_king_check_from_origin_to_destination(origin, destination):
    #         return False
    #     else:
    #         return True

    # def _can_move_from_origin_to_destination_with_color(self, origin: Tuple[int], destination: Tuple[int], color: str) -> bool:
    #     if destination not in self._get_destinations_from_origin(origin):
    #         return False
        
    #     return self._king_with_color_check(color)

    # def _king_with_color_check(self, color: str) -> bool:
    #     king_origin = self._king_with_color_origin(color)

    # def _origin_correct_color(self, origin: Tuple[int]) -> bool:
    #     piece = self._layout[origin]
    #     if 0 == len(self._moves) % 2 and Game.WHITE == piece.get_color():
    #         return True
    #     elif 1 == len(self._moves) % 2 and Game.BLACK == piece.get_color():
    #         return True
    #     else:
    #         return False

    def _get_destinations_from_origin(self, origin: Tuple[int]) -> Set[Tuple[int]]:
        if origin not in self._layout:
            return set()
        piece = self._layout[origin]
        destinations = piece.get_layout_destinations_from_origin(self._layout, origin)
        return destinations

    # def _current_king_check_from_origin_to_destination(self, origin: Tuple[int], destination: Tuple[int]) -> bool:
    #     current_color = self._get_current_color()
    #     other_color = self._get_other_color()
    #     layout = self._get_layout_from_origin_to_destination(origin, destination)
    #     current_king_origin = self._get_king_origin_from_color_and_layout(current_color, layout)
    #     destinations = self._get_destinations_from_color_and_layout(other_color, layout)

    #     return current_king_origin in destinations

    # def _get_current_color(self) -> str:
    #     if 0 == len(self._moves) % 2:
    #         return Game.WHITE
    #     else:
    #         return Game.BLACK

    # def _get_other_color(self) -> str:
    #     if 0 == len(self._moves) % 2:
    #         return Game.BLACK
    #     else:
    #         return Game.WHITE

    # def _get_layout_from_origin_to_destination(self, origin: Tuple[int], destination: Tuple[int]) -> Dict[Tuple[int], Piece]:
    #     layout = dict(self._layout)
    #     layout[destination] = layout[origin]
    #     del layout[origin]

    #     return layout

    # def _get_king_origin_from_color_and_layout(self, color: str, layout: Dict[Tuple[int], Piece]) -> Tuple[int]:
    #     king_origin = tuple()
        
    #     for origin in layout:
    #         piece = layout[origin]
    #         if isinstance(piece, King) and color == piece.get_color():
    #             king_origin = origin

    #     return king_origin

    # def _get_destinations_from_color_and_layout(self, color: str, layout: Dict[Tuple[int], Piece]) -> Set[Tuple[int]]:
    #     destinations = set()
        
    #     for origin in layout:
    #         piece = layout[origin]
    #         if color == piece.get_color():
    #             destinations |= piece.get_layout_destinations_from_origin(layout, origin)

    #     return destinations

    # def _end_move(self) -> None:
    #     # Get colors
    #     current_color = self._get_current_color()
    #     other_color = self._get_other_color()

    #     # Other King check
    #     if not self._other_king_check():
    #         return
    #     else:
    #         self._print("Check!")

    #     # Other King checkmate
    #     if self._other_king_can_move():
    #         return
    #     # elif self._can_capture_attacker():
    #     #     return
    #     # elif self._can_block_attacker:
    #     #     return
    #     # else:
    #     #     self._print("Checkmate")
    #     #     if Game.WHITE == current_color:
    #     #         return Game.WHITE_WON
    #     #     else:
    #     #         return Game.BLACK_WON

    # def _other_king_check(self) -> bool:
    #     current_color = self._get_current_color()
    #     other_color = self._get_other_color()
    #     other_king_origin = self._get_king_origin_from_color_and_layout(other_color, self._layout)
    #     destinations = self._get_destinations_from_color_and_layout(current_color, self._layout)

    #     return other_king_origin in destinations

    # def _other_king_can_move(self):
    #     other_color = self._get_other_color()
    #     other_king_origin = self._get_king_origin_from_color_and_layout(other_color, self._layout)
    #     other_king_destinations = self._get_destinations_from_origin(other_king_origin)
    #     other_king_can_move = False

    #     print("other_king_origin", other_king_origin)
    #     print("other_king_destinations", other_king_destinations)

    #     for other_king_destination in other_king_destinations:
    #         if self._can_move_from_origin_to_destination(other_king_origin, other_king_destination):
    #             other_king_can_move = True
    #         else:
    #             print("Python")

    #     return other_king_can_move

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
