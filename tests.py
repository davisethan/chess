import unittest
from Board import Board
from Game import Game
from Piece import Pawn, Knight, Bishop, Rook, Queen, King

# class BoardOriginCorrectColorTestCase(unittest.TestCase):
#     def test_board_white_origin_correct_color(self):
#         cases = [
#             {
#                 "name": "white_move",
#                 "origin": (6, 0),
#                 "expected_origin_correct_color": True
#             },
#             {
#                 "name": "black_move",
#                 "origin": (1, 0),
#                 "expected_origin_correct_color": False
#             }
#         ]
#         for case in cases:
#             with self.subTest(case["name"]):
#                 board = Board()

#                 actual_origin_correct_color = board._origin_correct_color(case["origin"])

#                 self.assertEqual(case["expected_origin_correct_color"], actual_origin_correct_color)

#     def test_board_black_origin_correct_color(self):
#         cases = [
#             {
#                 "name": "black_move",
#                 "origin": (1, 0),
#                 "expected_origin_correct_color": True
#             },
#             {
#                 "name": "white_move",
#                 "origin": (6, 0),
#                 "expected_origin_correct_color": False
#             }
#         ]
#         for case in cases:
#             with self.subTest(case["name"]):
#                 board = Board()
#                 board.add_move("PA2A3")

#                 actual_origin_correct_color = board._origin_correct_color(case["origin"])

#                 self.assertEqual(case["expected_origin_correct_color"], actual_origin_correct_color)

# class BoardCanMove(unittest.TestCase):
#     def test_board_is_correct_move_format(self):
#         cases = [
#             {
#                 "name": "correct_move_format",
#                 "move": "PA2A3",
#                 "expected_is_correct_move_format": True
#             },
#             {
#                 "name": "not_correct_move_format",
#                 "move": "ZA2A3",
#                 "expected_is_correct_move_format": False
#             }
#         ]
#         for case in cases:
#             with self.subTest(case["name"]):
#                 board = Board()
#                 board.set_move(case["move"])

#                 actual_is_correct_move_format = board._is_correct_move_format()

#                 self.assertEqual(case["expected_is_correct_move_format"], actual_is_correct_move_format)

#     def test_board_is_correct_origin_piece(self):
#         cases = [
#             {
#                 "name": "correct_origin_piece",
#                 "move": "PA2A3",
#                 "expected_is_correct_origin_piece": True
#             },
#             {
#                 "name": "origin_wrong_piece",
#                 "move": "NA2A3",
#                 "expected_is_correct_origin_piece": False
#             },
#             {
#                 "name": "origin_no_piece",
#                 "move": "PA3A4",
#                 "expected_is_correct_origin_piece": False
#             }
#         ]
#         for case in cases:
#             with self.subTest(case["name"]):
#                 board = Board()
#                 board.set_move(case["move"])

#                 actual_is_correct_origin_piece = board._is_correct_origin_piece()

#                 self.assertEqual(case["expected_is_correct_origin_piece"], actual_is_correct_origin_piece)

#     def test_board_is_correct_origin_color(self):
#         move = "PA2A3"
#         board = Board()
#         board.set_move(move)
#         expected_is_correct_origin_color = True

#         actual_is_correct_origin_color = board._is_correct_origin_color()

#         self.assertEqual(expected_is_correct_origin_color, actual_is_correct_origin_color)

class KingCheckTestCase(unittest.TestCase):
    def test_king_check(self):
        cases = [
            {
                "name": "king_check",
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (3, 2): Rook(Game.BLACK)
                },
                "expected_king_check": True
            },
            {
                "name": "not_king_check",
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (5, 2): Queen(Game.WHITE),
                    (3, 2): Rook(Game.BLACK)
                },
                "expected_king_check": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board(case["layout"])

                actual_king_check = board.king_with_color_check(Game.WHITE)

                self.assertEqual(case["expected_king_check"], actual_king_check)

    def test_move_from_origin_to_destination_makes_king_with_color_check(self):
        cases = [
            {
                "name": "king_check",
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (5, 2): Queen(Game.WHITE),
                    (3, 2): Rook(Game.BLACK)
                },
                "origin": (5, 2),
                "destination": (5, 3),
                "expected_king_check": True
            },
            {
                "name": "not_king_check",
                "layout": {
                    (6, 3): King(Game.WHITE),
                    (5, 2): Queen(Game.WHITE),
                    (3, 2): Rook(Game.BLACK)
                },
                "origin": (5, 2),
                "destination": (5, 3),
                "expected_king_check": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board(case["layout"])

                actual_king_check = board.move_from_origin_to_destination_makes_king_with_color_check(case["origin"], case["destination"], Game.WHITE)

                self.assertEqual(case["expected_king_check"], actual_king_check)

    def test_king_with_color_can_move(self):
        cases = [
            {
                "name": "king_can_move",
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (3, 2): Rook(Game.BLACK)
                },
                "expected_king_can_move": True
            },
            {
                "name": "king_can_not_move",
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (5, 1): Knight(Game.WHITE),
                    (6, 1): Knight(Game.WHITE),
                    (7, 1): Knight(Game.WHITE),
                    (7, 2): Knight(Game.WHITE),
                    (7, 3): Knight(Game.WHITE),
                    (6, 3): Knight(Game.WHITE),
                    (5, 3): Knight(Game.WHITE),
                    (3, 2): Rook(Game.BLACK)
                },
                "expected_king_can_move": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board(case["layout"])

                actual_king_can_move = board.king_with_color_can_move(Game.WHITE)

                self.assertEqual(case["expected_king_can_move"], actual_king_can_move)

    def test_can_capture_king_with_color_attacker(self):
        cases = [
            {
                "name": "can_capture_king_attacker",
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (3, 2): Rook(Game.BLACK),
                    (3, 3): Queen(Game.WHITE)
                },
                "expected_can_capture_king_attacker": True
            },
            {
                "name": "two_attackers_can_not_capture_king_attacker",
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (3, 2): Rook(Game.BLACK),
                    (3, 3): Queen(Game.WHITE),
                    (5, 4): Knight(Game.BLACK)
                },
                "expected_can_capture_king_attacker": False
            },
            {
                "name": "can_not_capture_king_attacker",
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (3, 2): Rook(Game.BLACK),
                    (5, 3): Queen(Game.WHITE)
                },
                "expected_can_capture_king_attacker": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board(case["layout"])

                actual_can_capture_king_attacker = board.can_capture_king_with_color_attacker(Game.WHITE)

                self.assertEqual(case["expected_can_capture_king_attacker"], actual_can_capture_king_attacker)

class BoardGetDestinationsFromOriginTestCase(unittest.TestCase):
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

# class BoardCurrentKingCheckFromOriginToDestination(unittest.TestCase):
#     def test_board_current_king_check_from_origin_to_destination(self):
#         cases = [
#             {
#                 "name": "current_king_check",
#                 "origin": (5, 2),
#                 "destination": (5, 3),
#                 "layout": {
#                     (6, 2): King(Game.WHITE),
#                     (5, 2): Queen(Game.WHITE),
#                     (3, 2): Rook(Game.BLACK)
#                 },
#                 "expected_current_king_check_from_origin_to_destination": True
#             },
#             {
#                 "name": "not_current_king_check",
#                 "origin": (5, 2),
#                 "destination": (5, 3),
#                 "layout": {
#                     (6, 3): King(Game.WHITE),
#                     (5, 2): Queen(Game.WHITE),
#                     (3, 2): Rook(Game.BLACK)
#                 },
#                 "expected_current_king_check_from_origin_to_destination": False
#             }
#         ]
#         for case in cases:
#             with self.subTest(case["name"]):
#                 board = Board(case["layout"])

#                 actual_current_king_check_from_origin_to_destination = board._current_king_check_from_origin_to_destination(case["origin"], case["destination"])

#                 self.assertEqual(case["expected_current_king_check_from_origin_to_destination"], actual_current_king_check_from_origin_to_destination)

# class BoardOtherKingCheck(unittest.TestCase):
#     def test_board_other_king_check(self):
#         cases = [
#             {
#                 "name": "other_king_check",
#                 "layout": {
#                     (3, 2): Rook(Game.WHITE),
#                     (6, 2): King(Game.BLACK)
#                 },
#                 "expected_other_king_check": True
#             },
#             {
#                 "name": "not_other_king_check",
#                 "layout": {
#                     (3, 2): Rook(Game.WHITE),
#                     (6, 3): King(Game.BLACK)
#                 },
#                 "expected_other_king_check": False
#             }
#         ]
#         for case in cases:
#             with self.subTest(case["name"]):
#                 board = Board(case["layout"])

#                 actual_other_king_check = board._other_king_check()

#                 self.assertEqual(case["expected_other_king_check"], actual_other_king_check)

#     def test_board_other_king_can_move(self):
#         layout = {
#             (3, 2): Rook(Game.WHITE),
#             (6, 2): King(Game.BLACK)
#         }
#         board = Board(layout)
#         expected_other_king_can_move = True

#         actual_other_king_can_move = board._other_king_can_move()

#         self.assertEqual(expected_other_king_can_move, actual_other_king_can_move)

if __name__ == "__main__":
    unittest.main()
