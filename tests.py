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
        move_counter = 0
        move = Move(formatted_string, move_counter)
        expected_origin = (6, 0)
        expected_destination = (5, 0)
        expected_color = Game.WHITE
        expected_other_color = Game.BLACK
        expected_piece = Pawn(expected_color)

        self.assertEqual(expected_origin, move.get_origin())
        self.assertEqual(expected_destination, move.get_destination())
        self.assertEqual(expected_color, move.get_color())
        self.assertEqual(expected_other_color, move.get_other_color())
        self.assertEqual(expected_piece, move.get_piece())
        self.assertEqual(formatted_string, move.get_formatted_string())

    def test_ok_origin_piece(self):
        cases = [
            {
                "name": "ok_origin_piece",
                "formatted_string": "PA2A3",
                "expected_ok_origin_piece": True
            },
            {
                "name": "not_ok_origin_piece",
                "formatted_string": "RA2A3",
                "expected_ok_origin_piece": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board()
                board.create_move(case["formatted_string"])

                actual_ok_origin_piece = board.ok_origin_piece()

                self.assertEqual(case["expected_ok_origin_piece"], actual_ok_origin_piece)

    def test_ok_origin_color(self):
        cases = [
            {
                "name": "ok_origin_color",
                "formatted_string": "PA2A3",
                "expected_ok_origin_color": True
            },
            {
                "name": "not_ok_origin_color",
                "formatted_string": "PA7A6",
                "expected_ok_origin_color": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board()
                board.create_move(case["formatted_string"])

                actual_ok_origin_color = board.ok_origin_color()

                self.assertEqual(case["expected_ok_origin_color"], actual_ok_origin_color)

    def test_can_move_from_origin_to_destination(self):
        cases = [
            {
                "name": "can_move",
                "formatted_string": "PA2A3",
                "expected_can_move": True
            },
            {
                "name": "cannot_move",
                "formatted_string": "PA2A5",
                "expected_can_move": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board()
                board.create_move(case["formatted_string"])

                actual_can_move = board.can_move_from_origin_to_destination()

                self.assertEqual(case["expected_can_move"], actual_can_move)

    def test_move_checks_king(self):
        cases = [
            {
                "name": "move_checks_king",
                "layout": {
                    (6, 2): King(Game.WHITE),
                    (5, 2): Queen(Game.WHITE),
                    (3, 2): Rook(Game.BLACK)
                },
                "formatted_string": "QC3D3",
                "expected_move_checks_king": True
            },
            {
                "name": "move_doesnt_check_king",
                "layout": {
                    (6, 3): King(Game.WHITE),
                    (5, 2): Queen(Game.WHITE),
                    (3, 2): Rook(Game.BLACK)
                },
                "formatted_string": "QC3D3",
                "expected_move_checks_king": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board(case["layout"])
                board.create_move(case["formatted_string"])

                actual_move_checks_king = board.move_checks_king()

                self.assertEqual(case["expected_move_checks_king"], actual_move_checks_king)

    def test_can_move(self):
        layout = {
            (6, 3): King(Game.WHITE),
            (5, 2): Queen(Game.WHITE),
            (3, 2): Rook(Game.BLACK)
        }
        board = Board(layout)
        move_string = "QC3D3"
        expected_can_move = True

        actual_can_move = board.can_move(move_string)

        self.assertEqual(expected_can_move, actual_can_move)

class EndMoveTestCase(unittest.TestCase):
    def test_can_move_king(self):
        cases = [
            {
                "name": "can_move_king",
                "layout": {
                    (3, 0): King(Game.BLACK),
                    (6, 0): Rook(Game.WHITE)
                },
                "formatted_string": "RB2A2",
                "expected_can_move_king": True
            },
            {
                "name": "cannot_move_king",
                "layout": {
                    (3, 0): King(Game.BLACK),
                    (7, 1): Queen(Game.WHITE),
                    (6, 0): Rook(Game.WHITE)
                },
                "formatted_string": "RB2A2",
                "expected_can_move_king": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board(case["layout"])
                board.create_move(case["formatted_string"])

                actual_can_move_king = board.can_move_king()

                self.assertEqual(case["expected_can_move_king"], actual_can_move_king)

    def test_can_capture_king_attacker(self):
        cases = [
            {
                "name": "can_capture_king_attacker",
                "layout": {
                    (3, 0): King(Game.BLACK),
                    (5, 2): Knight(Game.BLACK),
                    (6, 0): Rook(Game.WHITE)
                },
                "formatted_string": "RB2A2",
                "expected_can_capture": True
            },
            {
                "name": "cannot_capture_king_attacker",
                "layout": {
                    (3, 0): King(Game.BLACK),
                    (5, 2): Knight(Game.BLACK),
                    (6, 0): Rook(Game.WHITE),
                    (6, 3): Bishop(Game.WHITE)
                },
                "formatted_string": "RB2A2",
                "expected_can_capture": False
            },
            {
                "name": "cannot_capture_king_attacker_makes_check",
                "layout": {
                    (3, 0): King(Game.BLACK),
                    (5, 2): Knight(Game.BLACK),
                    (6, 0): Rook(Game.WHITE),
                    (6, 3): Bishop(Game.WHITE)
                },
                "formatted_string": "RB2A2",
                "expected_can_capture": False
            },
            {
                "name": "cannot_capture_king_attacker_two_attackers",
                "layout": {
                    (3, 0): King(Game.BLACK),
                    (5, 2): Knight(Game.BLACK),
                    (6, 0): Rook(Game.WHITE),
                    (4, 2): Knight(Game.WHITE)
                },
                "formatted_string": "NA3C4",
                "expected_can_capture": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board(case["layout"])
                board.create_move(case["formatted_string"])

                actual_can_capture = board.can_capture_king_attacker()

                self.assertEqual(case["expected_can_capture"], actual_can_capture)

    def test_can_block_king_attacker(self):
        cases = [
            {
                "name": "can_block_king_attacker_up_vertical",
                "layout": {
                    (3, 3): King(Game.BLACK),
                    (0, 3): Rook(Game.WHITE),
                    (1, 4): Queen(Game.BLACK)
                },
                "formatted_string": "RC8D8",
                "expected_can_block": True
            },
            {
                "name": "can_block_king_attacker_up_right_diagonal",
                "layout": {
                    (3, 3): King(Game.BLACK),
                    (0, 6): Bishop(Game.WHITE),
                    (1, 4): Queen(Game.BLACK)
                },
                "formatted_string": "BH7G8",
                "expected_can_block": True
            },
            {
                "name": "can_block_king_attacker_right_horizontal",
                "layout": {
                    (3, 3): King(Game.BLACK),
                    (3, 6): Rook(Game.WHITE),
                    (1, 4): Queen(Game.BLACK)
                },
                "formatted_string": "RG6G5",
                "expected_can_block": True
            },
            {
                "name": "can_block_king_attacker_down_right_diagonal",
                "layout": {
                    (3, 3): King(Game.BLACK),
                    (6, 6): Bishop(Game.WHITE),
                    (1, 4): Queen(Game.BLACK)
                },
                "formatted_string": "BF1G2",
                "expected_can_block": True
            },
            {
                "name": "can_block_king_attacker_down_vertical",
                "layout": {
                    (3, 3): King(Game.BLACK),
                    (6, 3): Rook(Game.WHITE),
                    (5, 2): Queen(Game.BLACK)
                },
                "formatted_string": "RB2A2",
                "expected_can_block": True
            },
            {
                "name": "can_block_king_attacker_down_left_diagonal",
                "layout": {
                    (3, 3): King(Game.BLACK),
                    (6, 0): Bishop(Game.WHITE),
                    (5, 2): Queen(Game.BLACK)
                },
                "formatted_string": "BB1A2",
                "expected_can_block": True
            },
            {
                "name": "can_block_king_attacker_left_horizontal",
                "layout": {
                    (3, 3): King(Game.BLACK),
                    (3, 0): Rook(Game.WHITE),
                    (5, 2): Queen(Game.BLACK)
                },
                "formatted_string": "RA4A5",
                "expected_can_block": True
            },
            {
                "name": "can_block_king_attacker_up_left_diagonal",
                "layout": {
                    (3, 3): King(Game.BLACK),
                    (0, 0): Queen(Game.WHITE),
                    (5, 2): Queen(Game.BLACK)
                },
                "formatted_string": "QA7A8",
                "expected_can_block": True
            },
            {
                "name": "cannot_block_king_attacker",
                "layout": {
                    (3, 0): King(Game.BLACK),
                    (5, 2): Bishop(Game.BLACK),
                    (6, 0): Rook(Game.WHITE)
                },
                "formatted_string": "RB2A2",
                "expected_can_block": False
            },
            {
                "name": "cannot_block_king_attacker_makes_check",
                "layout": {
                    (3, 0): King(Game.BLACK),
                    (5, 2): Knight(Game.BLACK),
                    (6, 0): Rook(Game.WHITE),
                    (6, 3): Bishop(Game.WHITE)
                },
                "formatted_string": "RB2A2",
                "expected_can_block": False
            },
            {
                "name": "cannot_block_king_attacker_two_attackers",
                "layout": {
                    (3, 0): King(Game.BLACK),
                    (5, 2): Knight(Game.BLACK),
                    (6, 0): Rook(Game.WHITE),
                    (4, 2): Knight(Game.WHITE)
                },
                "formatted_string": "NA3C4",
                "expected_can_block": False
            }
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board(case["layout"])
                board.create_move(case["formatted_string"])

                actual_can_block = board.can_block_king_attacker()

                self.assertEqual(case["expected_can_block"], actual_can_block)

    def test_king_checkmate(self):
        layout = {
            (3, 0): King(Game.BLACK),
            (6, 0): Rook(Game.WHITE),
            (7, 1): Queen(Game.WHITE)
        }
        board = Board(layout)
        formatted_string = "RB2A2"
        board.create_move(formatted_string)
        expected_checkmate = True

        actual_checkmate = board.king_checkmate()

        self.assertEqual(expected_checkmate, actual_checkmate)

class BoardGetDestinationsFromOriginTestCase(unittest.TestCase):
    def test_board_get_destinations_from_origin(self):
        cases = [
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
