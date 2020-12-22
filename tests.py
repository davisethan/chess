import unittest
from Board import Board
from Game import Game
from Piece import Pawn, Knight, Bishop, Rook, Queen, King

class BoardCanMoveTestCase(unittest.TestCase):
    def test_board_white_origin_correct_color(self):
        cases = [
            {
                "name": "white_move",
                "origin": (6, 0),
                "expected_origin_correct_color": True
            },
            {
                "name": "black_move",
                "origin": (1, 0),
                "expected_origin_correct_color": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board()

                actual_origin_correct_color = board._origin_correct_color(case["origin"])

                self.assertEqual(case["expected_origin_correct_color"], actual_origin_correct_color)

    def test_board_black_origin_correct_color(self):
        cases = [
            {
                "name": "black_move",
                "origin": (1, 0),
                "expected_origin_correct_color": True
            },
            {
                "name": "white_move",
                "origin": (6, 0),
                "expected_origin_correct_color": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board()
                board.add_move("PA2A3")

                actual_origin_correct_color = board._origin_correct_color(case["origin"])

                self.assertEqual(case["expected_origin_correct_color"], actual_origin_correct_color)

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
            },
            {
                "name": "rook",
                "origin": (4, 2),
                "layout": {
                    (4, 2): Rook(Game.WHITE)
                },
                "expected_destinations": {(3, 2), (2, 2), (1, 2), (0, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (5, 2), (6, 2), (7, 2), (4, 1), (4, 0)}
            },
            {
                "name": "rook_and_pieces",
                "origin": (4, 2),
                "layout": {
                    (4, 2): Rook(Game.WHITE),
                    (2, 2): Pawn(Game.WHITE),
                    (4, 4): Pawn(Game.WHITE),
                    (6, 2): Pawn(Game.BLACK),
                    (4, 0): Pawn(Game.BLACK)
                },
                "expected_destinations": {(3, 2), (4, 3), (5, 2), (6, 2), (4, 1), (4, 0)}
            },
            {
                "name": "queen",
                "origin": (4, 2),
                "layout": {
                    (4, 2): Queen(Game.WHITE)
                },
                "expected_destinations": {(3, 3), (2, 4), (1, 5), (0, 6), (5, 3), (6, 4), (7, 5), (5, 1), (6, 0), (3, 1), (2, 0), (3, 2), (2, 2), (1, 2), (0, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (5, 2), (6, 2), (7, 2), (4, 1), (4, 0)}
            },
            {
                "name": "queen_and_pieces",
                "origin": (4, 2),
                "layout": {
                    (4, 2): Queen(Game.WHITE),
                    (2, 0): Pawn(Game.WHITE),
                    (2, 2): Pawn(Game.WHITE),
                    (2, 4): Pawn(Game.WHITE),
                    (4, 4): Pawn(Game.WHITE),
                    (6, 4): Pawn(Game.BLACK),
                    (6, 2): Pawn(Game.BLACK),
                    (6, 0): Pawn(Game.BLACK),
                    (4, 0): Pawn(Game.BLACK)
                },
                "expected_destinations": {(3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (6, 4), (5, 2), (6, 2), (5, 1), (6, 0), (4, 1), (4, 0)}
            },
            {
                "name": "king",
                "origin": (4, 2),
                "layout": {
                    (4, 2): King(Game.WHITE)
                },
                "expected_destinations": {(3, 2), (3, 3), (4, 3), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1)}
            },
            {
                "name": "king_and_pieces",
                "origin": (4, 2),
                "layout": {
                    (4, 2): King(Game.WHITE),
                    (3, 1): Knight(Game.WHITE),
                    (3, 2): Knight(Game.WHITE),
                    (3, 3): Knight(Game.WHITE),
                    (4, 3): Knight(Game.WHITE),
                    (5, 3): Knight(Game.BLACK),
                    (5, 2): Knight(Game.BLACK),
                    (5, 1): Knight(Game.BLACK),
                    (4, 1): Knight(Game.BLACK)
                },
                "expected_destinations": {(5, 3), (5, 2), (5, 1), (4, 1)}
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board(case["layout"])

                actual_destinations = board._get_destinations_from_origin(case["origin"])

                self.assertEqual(case["expected_destinations"], actual_destinations)

    def test_board_current_king_check_from_origin_to_destination(self):
        cases = [
            {
                "name": "current_king_check",
                "origin": (5, 2),
                "destination": (5, 3),
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (5, 2): Queen(Game.WHITE),
                    (3, 2): Rook(Game.BLACK)
                },
                "expected_current_king_check_from_origin_to_destination": True
            },
            {
                "name": "not_current_king_check",
                "origin": (5, 2),
                "destination": (5, 3),
                "layout": {
                    (6, 3): King(Game.WHITE),
                    (5, 2): Queen(Game.WHITE),
                    (3, 2): Rook(Game.BLACK)
                },
                "expected_current_king_check_from_origin_to_destination": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board(case["layout"])

                actual_current_king_check_from_origin_to_destination = board._current_king_check_from_origin_to_destination(case["origin"], case["destination"])

                self.assertEqual(case["expected_current_king_check_from_origin_to_destination"], actual_current_king_check_from_origin_to_destination)

        

if __name__ == "__main__":
    unittest.main()
