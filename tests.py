import unittest
from Board import Board, Move
from Game import Game
from Piece import Pawn, Knight, Bishop, Rook, Queen, King

class CanMoveTestCase(unittest.TestCase):
    def test_move_string_formatted(self):
        cases = [
            {
                "name": "formatted_string",
                "move_string": "PA2A3",
                "expected_move_string_formatted": True
            },
            {
                "name": "unformatted_string",
                "move_string": "ZA2A3",
                "expected_move_string_formatted": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board()
        
                actual_move_string_formatted = board.move_string_formatted(case["move_string"])

                self.assertEqual(case["expected_move_string_formatted"], actual_move_string_formatted)

    def test_create_move(self):
        formatted_string = "PA2A3"
        move = Move(formatted_string, 0)
        expected_origin = (6, 0)
        expected_destination = (5, 0)
        expected_color = Game.WHITE
        expected_piece = Pawn(expected_color)

        self.assertEqual(expected_origin, move.get_origin())
        self.assertEqual(expected_destination, move.get_destination())
        self.assertEqual(expected_color, move.get_color())
        self.assertEqual(type(expected_piece), type(move.get_piece()))
        self.assertEqual(expected_piece.get_color(), move.get_piece().get_color())
        self.assertEqual(formatted_string, move.get_formatted_string())

###############
# OLD VERSION #
###############

class KingCheckTestCase(unittest.TestCase):
    @unittest.skip("")
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

    @unittest.skip("")
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

    @unittest.skip("")
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
            },
            {
                "name": "king_can_not_move_down",
                "layout": {
                    (0, 7): Rook(Game.BLACK),
                    (3, 7): King(Game.WHITE),
                    (2, 6): Pawn(Game.WHITE),
                    (3, 6): Pawn(Game.WHITE),
                    (4, 6): Pawn(Game.WHITE)
                },
                "expected_king_can_move": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board(case["layout"])

                actual_king_can_move = board.king_with_color_can_move(Game.WHITE)

                self.assertEqual(case["expected_king_can_move"], actual_king_can_move)

    @unittest.skip("")
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
            },
            {
                "name": "can_not_capture_king_attacker_makes_check",
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (3, 2): Rook(Game.BLACK),
                    (6, 6): Rook(Game.BLACK),
                    (6, 5): Queen(Game.WHITE)
                },
                "expected_can_capture_king_attacker": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board(case["layout"])

                actual_can_capture_king_attacker = board.can_capture_king_with_color_attacker(Game.WHITE)

                self.assertEqual(case["expected_can_capture_king_attacker"], actual_can_capture_king_attacker)

    @unittest.skip("")
    def test_can_block_king_with_color_attacker(self):
        cases = [
            {
                "name": "can_block_king_attacker",
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (3, 2): Rook(Game.BLACK),
                    (5, 3): Queen(Game.WHITE)
                },
                "expected_can_block_king_attacker": True
            },
            {
                "name": "can_not_block_king_attacker",
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (3, 2): Rook(Game.BLACK),
                    (7, 2): Queen(Game.WHITE)
                },
                "expected_can_block_king_attacker": False
            },
            {
                "name": "can_not_block_king_attacker_makes_check",
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (3, 2): Rook(Game.BLACK),
                    (6, 4): Queen(Game.WHITE),
                    (6, 5): Rook(Game.BLACK)
                },
                "expected_can_block_king_attacker": False
            },
            {
                "name": "can_block_king_attacker_bishop",
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (3, 5): Bishop(Game.BLACK),
                    (6, 4): Queen(Game.WHITE)
                },
                "expected_can_block_king_attacker": True
            },
            {
                "name": "can_not_block_king_attacker_bishop_makes_check",
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (3, 5): Bishop(Game.BLACK),
                    (6, 4): Queen(Game.WHITE),
                    (6, 5): Rook(Game.BLACK)
                },
                "expected_can_block_king_attacker": False
            },
            {
                "name": "can_block_king_attacker_right_horizontal",
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (6, 5): Rook(Game.BLACK),
                    (5, 4): Queen(Game.WHITE)
                },
                "expected_can_block_king_attacker": True
            },
            {
                "name": "can_block_king_attacker_right_down_diagonal",
                "layout": {
                    (4, 2): King(Game.WHITE),
                    (7, 5): Bishop(Game.BLACK),
                    (5, 4): Queen(Game.WHITE)
                },
                "expected_can_block_king_attacker": True
            },
            {
                "name": "can_block_king_attacker_down_vertical",
                "layout": {
                    (4, 2): King(Game.WHITE),
                    (7, 2): Rook(Game.BLACK),
                    (6, 3): Queen(Game.WHITE)
                },
                "expected_can_block_king_attacker": True
            },
            {
                "name": "can_block_king_attacker_down_left_diagonal",
                "layout": {
                    (3, 3): King(Game.WHITE),
                    (6, 0): Bishop(Game.BLACK),
                    (5, 2): Queen(Game.WHITE)
                },
                "expected_can_block_king_attacker": True
            },
            {
                "name": "can_block_king_attack_left_horizontal",
                "layout": {
                    (3, 3): King(Game.WHITE),
                    (3, 0): Rook(Game.BLACK),
                    (4, 1): Queen(Game.WHITE)
                },
                "expected_can_block_king_attacker": True
            },
            {
                "name": "can_block_king_attack_up_left_diagonal",
                "layout": {
                    (3, 3): King(Game.WHITE),
                    (0, 0): Bishop(Game.BLACK),
                    (2, 1): Queen(Game.WHITE)
                },
                "expected_can_block_king_attacker": True
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board(case["layout"])

                actual_can_block_king_attacker = board.can_block_king_with_color_attacker(Game.WHITE)

                self.assertEqual(case["expected_can_block_king_attacker"], actual_can_block_king_attacker)

class KingCheckmateTestCase(unittest.TestCase):
    @unittest.skip("")
    def test_king_with_color_checkmate(self):
        layout = {
            (0, 7): Rook(Game.BLACK),
            (0, 6): Queen(Game.BLACK),
            (2, 7): King(Game.WHITE)
        }
        board = Board(layout)
        expected_king_checkmate = True

        actual_king_checkmate = board.king_with_color_checkmate(Game.WHITE)

        self.assertEqual(expected_king_checkmate, actual_king_checkmate)

class BoardGetDestinationsFromOriginTestCase(unittest.TestCase):
    def test_board_get_destinations_from_origin(self):
        cases = [
            # {
            #     "name": "empty_origin",
            #     "origin": (0, 0),
            #     "layout": {
            #         (1, 1): Pawn(Game.BLACK)
            #     },
            #     "expected_destinations": set(),
            # },
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

if __name__ == "__main__":
    unittest.main()
