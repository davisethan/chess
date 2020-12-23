import re
from typing import Any, Dict, Set, Tuple
from Game import Game
from Piece import Piece, Pawn, Knight, Bishop, Rook, Queen, King

class Move:
    def __init__(self, formatted_string: str, move_counter: int) -> None:
        self._origin = self._get_origin_from_formatted_string(formatted_string)
        self._destination = self._get_destination_from_formatted_string(formatted_string)
        self._color = self._get_color_from_move_counter(move_counter)
        self._other_color = self._get_other_color_from_move_counter(move_counter)
        self._piece = self._get_piece_from_formatted_string(formatted_string)
        self._formatted_string = formatted_string

    def get_origin(self) -> Tuple[int]:
        return self._origin

    def get_destination(self) -> Tuple[int]:
        return self._destination

    def get_color(self) -> str:
        return self._color

    def get_other_color(self) -> str:
        return self._other_color

    def get_piece(self) -> Piece:
        return self._piece

    def get_formatted_string(self) -> str:
        return self._formatted_string

    def _get_origin_from_formatted_string(self, formatted_string: str) -> Tuple[int]:
        origin_string = formatted_string[1:3]
        row = self._get_row_from_square_string(origin_string)
        column = self._get_column_from_square_string(origin_string)
        return (row, column)
    
    def _get_row_from_square_string(self, square_string: str) -> int:
        return Game.ROWS[::-1].index(square_string[1])

    def _get_column_from_square_string(self, square_string: str) -> int:
        return Game.COLUMNS.index(square_string[0])

    def _get_destination_from_formatted_string(self, formatted_string: str) -> Tuple[int]:
        destination_string = formatted_string[3:5]
        row = self._get_row_from_square_string(destination_string)
        column = self._get_column_from_square_string(destination_string)
        return (row, column)

    def _get_color_from_move_counter(self, move_counter: int) -> str:
        if 0 == move_counter % 2:
            return Game.WHITE
        else:
            return Game.BLACK

    def _get_other_color_from_move_counter(self, move_counter: int) -> str:
        if 0 == move_counter % 2:
            return Game.BLACK
        else:
            return Game.WHITE

    def _get_piece_from_formatted_string(self, formatted_string: str) -> Piece:
        piece_string = formatted_string[0]
        if Game.PAWN_STRING == piece_string:
            return Pawn(self._color)
        elif Game.KNIGHT_STRING == piece_string:
            return Knight(self._color)
        elif Game.BISHOP_STRING == piece_string:
            return Bishop(self._color)
        elif Game.ROOK_STRING == piece_string:
            return Rook(self._color)
        elif Game.QUEEN_STRING == piece_string:
            return Queen(self._color)
        else:
            return King(self._color)

class Board:
    def __init__(self, layout: Dict[Tuple[int], Piece] = {}) -> None:
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
        self._layout_memento = {}
        self._move = None
        self._move_memento = None
        self._moves = []

    def can_move(self, move_string: str) -> bool:
        if not self.move_string_formatted(move_string):
            return False
        
        self.create_move(move_string)
        
        if not self.ok_origin_piece():
            return False
        elif not self.ok_origin_color():
            return False
        elif not self.can_move_from_origin_to_destination():
            return False
        elif self.move_checks_king():
            return False
        else:
            return True

    def move_string_formatted(self, move_string: str) -> bool:
        return None != re.search(Game.FORMATTED_STRING, move_string)

    def create_move(self, move_string: str) -> None:
        self._move = Move(move_string, len(self._moves))
        
    def ok_origin_piece(self) -> bool:
        return self._layout[self._move.get_origin()] == self._move.get_piece()

    def ok_origin_color(self) -> bool:
        if 0 == len(self._moves) % 2 and Game.WHITE == self._layout[self._move.get_origin()].get_color():
            return True
        elif 1 == len(self._moves) % 2 and Game.BLACK == self._layout[self._move.get_origin()].get_color():
            return True
        else:
            return False

    def can_move_from_origin_to_destination(self) -> bool:
        destination = self._move.get_destination()
        destinations = self._get_destinations_from_origin(self._move.get_origin())
        return destination in destinations

    def _get_destinations_from_origin(self, origin: Tuple[int]) -> Set[Tuple[int]]:
        piece = self._layout[origin]
        destinations = piece.get_layout_destinations_from_origin(self._layout, origin)
        return destinations

    def move_checks_king(self) -> bool:
        self._do_move()
        king_check = self._king_check_for_color(self._move.get_color())
        self._undo_move()
        return king_check

    def _do_move(self) -> None:
        self._layout_memento = dict(self._layout)
        self._layout[self._move.get_destination()] = self._layout[self._move.get_origin()]
        self._layout.pop(self._move.get_origin())

    def _king_check_for_color(self, color: str) -> bool:
        king_origin = self._get_king_origin_for_color(color)
        king_check = False
        for origin in self._layout:
            if king_origin in self._get_destinations_from_origin(origin):
                king_check = True
        
        return king_check

    def _get_king_origin_for_color(self, color: str) -> Tuple[int]:
        king_origin = tuple()
        for origin in self._layout:
            if isinstance(self._layout[origin], King) and color == self._layout[origin].get_color():
                king_origin = origin
        
        return king_origin

    def _undo_move(self) -> None:
        self._layout = self._layout_memento

    def end_move(self) -> None:
        pass

    def can_move_king(self) -> bool:
        king_origin = self._get_king_origin_for_color(self._move.get_other_color())
        king_destinations = self._get_destinations_from_origin(king_origin)
        can_move_king = False
        for king_destination in king_destinations:
            if not self._can_move_from_origin_to_destination(king_origin, king_destination):
                can_move_king = True

        return can_move_king

    def _can_move_from_origin_to_destination(self, origin: Tuple[int], destination: Tuple[int]) -> bool:
        self._move_memento = self._move
        self._create_move_from_origin_and_destination(origin, destination)
        king_check = self.move_checks_king()
        self._move = self._move_memento
        return king_check

    def _create_move_from_origin_and_destination(self, origin: Tuple[int], destination: Tuple[int]) -> Move:
        origin_string = self._get_square_string_from_square(origin)
        destination_string = self._get_square_string_from_square(destination)
        piece_string = self._get_piece_string_from_origin(origin)
        formatted_string = piece_string + origin_string + destination_string
        self._move = Move(formatted_string, len(self._moves) + 1)

    def _get_square_string_from_square(self, square: Tuple[int]) -> str:
        row = square[0]
        column = square[1]
        row_string = Game.ROWS[::-1][row]
        column_string = Game.COLUMNS[column]
        return column_string + row_string

    def _get_piece_string_from_origin(self, origin: Tuple[int]) -> str:
        piece = self._layout[origin]
        if isinstance(piece, Pawn):
            return Game.PAWN_STRING
        elif isinstance(piece, Knight):
            return Game.KNIGHT_STRING
        elif isinstance(piece, Bishop):
            return Game.BISHOP_STRING
        elif isinstance(piece, Rook):
            return Game.ROOK_STRING
        elif isinstance(piece, Queen):
            return Game.QUEEN_STRING
        else:
            return Game.KING_STRING

    def can_capture_king_attacker(self) -> bool:
        if self._over_one_king_attacker():
            return False

        attacker_origin = self._get_king_attacker_origin()
        capture_attacker_origins = self._get_capture_attacker_origins_with_attacker_origin(attacker_origin)
        can_capture = False
        for capture_attacker_origin in capture_attacker_origins:
            if not self._can_move_from_origin_to_destination(capture_attacker_origin, attacker_origin):
                can_capture = True

        return can_capture

    def _over_one_king_attacker(self) -> bool:
        return 1 < len(self._get_king_attacker_origins())

    def _get_king_attacker_origins(self) -> Set[Tuple[int]]:
        king_origin = self._get_king_origin_for_color(self._move.get_other_color())
        attacker_origins = set()
        for origin in self._layout:
            if king_origin in self._get_destinations_from_origin(origin):
                attacker_origins.add(origin)

        return attacker_origins

    def _get_king_attacker_origin(self) -> Tuple[int]:
        attacker_origins = self._get_king_attacker_origins()
        return list(attacker_origins).pop()

    def _get_capture_attacker_origins_with_attacker_origin(self, attacker_origin: Tuple[int]) -> Set[Tuple[int]]:
        capture_attacker_origins = set()
        for origin in self._layout:
            if attacker_origin in self._get_destinations_from_origin(origin):
                capture_attacker_origins.add(origin)

        return capture_attacker_origins

    ###############
    # OLD VERSION #
    ###############

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

    def king_with_color_checkmate(self, color: str) -> bool:
        if self.king_with_color_can_move(color):
            return False
        elif self.can_capture_king_with_color_attacker(color):
            return False
        elif self.can_block_king_with_color_attacker(color):
            return False
        else:
            return True

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
