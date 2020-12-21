import unittest
from Board import Board
from Game import Game
from Piece import Pawn, Knight, Bishop

class BoardTestCase(unittest.TestCase):
    def test_board_get_destinations_from_origin(self):
        cases = [
            {
                "name": "empty_origin",
                "origin": (0, 0),
                "layout": {
                    (1, 1): Pawn(Game.BLACK)
                },
                "expected_destinations": set(),
            },
            {
                "name": "white_pawn_first_move",
                "origin": (6, 1),
                "layout": {
                    (6, 1): Pawn(Game.WHITE)
                },
                "expected_destinations": {(5, 1), (4, 1)}
            },
            {
                "name": "white_pawn_not_first_move",
                "origin": (5, 1),
                "layout": {
                    (5, 1): Pawn(Game.WHITE)
                },
                "expected_destinations": {(4, 1)}
            },
            {
                "name": "white_pawn_no_queen_promotion",
                "origin": (0, 1),
                "layout": {
                    (0, 1): Pawn(Game.WHITE)
                },
                "expected_destinations": set()
            },
            {
                "name": "white_pawn_attack",
                "origin": (6, 1),
                "layout": {
                    (6, 1): Pawn(Game.WHITE),
                    (5, 0): Pawn(Game.BLACK),
                    (5, 2): Pawn(Game.BLACK)
                },
                "expected_destinations": {(5, 1), (4, 1), (5, 0), (5, 2)}
            },
            {
                "name": "white_pawn_no_attack",
                "origin": (6, 1),
                "layout": {
                    (6, 1): Pawn(Game.WHITE),
                    (5, 0): Pawn(Game.WHITE),
                    (5, 2): Pawn(Game.WHITE)
                },
                "expected_destinations": {(5, 1), (4, 1)}
            },
            {
                "name": "black_pawn_first_move",
                "origin": (1, 1),
                "layout": {
                    (1, 1): Pawn(Game.BLACK)
                },
                "expected_destinations": {(2, 1), (3, 1)}
            },
            {
                "name": "black_pawn_not_first_move",
                "origin": (2, 1),
                "layout": {
                    (2, 1): Pawn(Game.BLACK)
                },
                "expected_destinations": {(3, 1)}
            },
            {
                "name": "black_pawn_attack",
                "origin": (1, 1),
                "layout": {
                    (1, 1): Pawn(Game.BLACK),
                    (2, 0): Pawn(Game.WHITE),
                    (2, 2): Pawn(Game.WHITE)
                },
                "expected_destinations": {(2, 1), (3, 1), (2, 0), (2, 2)}
            },
            {
                "name": "black_pawn_no_attack",
                "origin": (1, 1),
                "layout": {
                    (1, 1): Pawn(Game.BLACK),
                    (2, 0): Pawn(Game.BLACK),
                    (2, 2): Pawn(Game.BLACK)
                },
                "expected_destinations": {(2, 1), (3, 1)}
            },
            {
                "name": "knight",
                "origin": (4, 3),
                "layout": {
                    (4, 3): Knight(Game.WHITE)
                },
                "expected_destinations": {(2, 2), (2, 4), (3, 5), (5, 5), (6, 4), (6, 2), (5, 1), (3, 1)}
            },
            {
                "name": "knight_and_pieces",
                "origin": (4, 3),
                "layout": {
                    (4, 3): Knight(Game.WHITE),
                    (3, 1): Pawn(Game.BLACK),
                    (3, 5): Pawn(Game.BLACK),
                    (2, 2): Pawn(Game.WHITE),
                    (2, 4): Pawn(Game.WHITE)
                },
                "expected_destinations": {(3, 5), (5, 5), (6, 4), (6, 2), (5, 1), (3, 1)}
            },
            {
                "name": "knight_board_edge",
                "origin": (7, 1),
                "layout": {
                    (7, 1): Knight(Game.WHITE)
                },
                "expected_destinations": {(5, 0), (5, 2), (6, 3)}
            },
            {
                "name": "bishop",
                "origin": (4, 2),
                "layout": {
                    (4, 2): Bishop(Game.WHITE)
                },
                "expected_destinations": {(3, 3), (2, 4), (1, 5), (0, 6), (5, 3), (6, 4), (7, 5), (5, 1), (6, 0), (3, 1), (2, 0)}
            },
            {
                "name": "bishop_and_pieces",
                "origin": (4, 2),
                "layout": {
                    (4, 2): Bishop(Game.WHITE),
                    (2, 0): Pawn(Game.WHITE),
                    (2, 4): Pawn(Game.WHITE),
                    (6, 4): Pawn(Game.BLACK),
                    (6, 0): Pawn(Game.BLACK)
                },
                "expected_destinations": {(3, 1), (3, 3), (5, 1), (5, 3), (6, 0), (6, 4)}
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board(case["layout"])

                actual_destinations = board.get_destinations_from_origin(case["origin"])

                self.assertEqual(case["expected_destinations"], actual_destinations)
        

if __name__ == "__main__":
    unittest.main()
