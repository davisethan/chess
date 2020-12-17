from typing import Set
from Game import Game
from Piece import Pawn, Knight, Bishop, Rook, Queen, King

class Board:
    def __init__(self, board = {}) -> None:
        default_board = {
            "A1": Rook(Game.WHITE),
            "B1": Knight(Game.WHITE),
            "C1": Bishop(Game.WHITE),
            "D1": Queen(Game.WHITE),
            "E1": King(Game.WHITE),
            "F1": Bishop(Game.WHITE),
            "G1": Knight(Game.WHITE),
            "H1": Rook(Game.WHITE),
            "A2": Pawn(Game.WHITE),
            "B2": Pawn(Game.WHITE),
            "C2": Pawn(Game.WHITE),
            "D2": Pawn(Game.WHITE),
            "E2": Pawn(Game.WHITE),
            "F2": Pawn(Game.WHITE),
            "G2": Pawn(Game.WHITE),
            "H2": Pawn(Game.WHITE),
            "A7": Pawn(Game.BLACK),
            "B7": Pawn(Game.BLACK),
            "C7": Pawn(Game.BLACK),
            "D7": Pawn(Game.BLACK),
            "E7": Pawn(Game.BLACK),
            "F7": Pawn(Game.BLACK),
            "G7": Pawn(Game.BLACK),
            "H7": Pawn(Game.BLACK),
            "A8": Rook(Game.BLACK),
            "B8": Knight(Game.BLACK),
            "C8": Bishop(Game.BLACK),
            "D8": Queen(Game.BLACK),
            "E8": King(Game.BLACK),
            "F8": Bishop(Game.BLACK),
            "G8": Knight(Game.BLACK),
            "H8": Rook(Game.BLACK),
        }

        self._board = board or default_board

    def get_destinations_from_origin(self, origin: str) -> Set[str]:
        piece = self._board[origin]
        destinations = piece.get_destinations_from_origin(origin)
        destinations = self._filter_color(destinations, piece.get_color())
        return destinations

    def _filter_color(self, destinations: Set[str], color: str) -> Set[str]:
        return {destination for destination in destinations if destination not in self._board or color != self._board[destination].get_color()}
