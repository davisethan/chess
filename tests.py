import unittest
from Board import Board
from Game import Game
from Piece import Pawn, Knight

class BoardTestCase(unittest.TestCase):
    def test_board_get_destinations_from_origin(self):
        cases = [
            {
                "name": "one_piece",
                "origin": "D4",
                "layout": {
                    "D4": Knight(Game.WHITE),
                },
                "expected_destinations": {"C6", "E6", "F5", "F3", "E2", "C2", "B3", "B5"},
            },
            {
                "name": "many_pieces",
                "origin": "D4",
                "layout": {
                    "D4": Knight(Game.WHITE),
                    "B5": Pawn(Game.BLACK),
                    "F5": Pawn(Game.BLACK),
                    "C6": Pawn(Game.WHITE),
                    "E6": Pawn(Game.WHITE),
                },
                "expected_destinations": {"F5", "F3", "E2", "C2", "B3", "B5"},
            },
            {
                "name": "board_edge",
                "origin": "B1",
                "layout": {
                    "B1": Knight(Game.WHITE),
                },
                "expected_destinations": {"A3", "C3", "D2"},
            },
        ]
        for case in cases:
            with self.subTest(case["name"]):
                board = Board(case["layout"])

                actual_destinations = board.get_destinations_from_origin(case["origin"])

                self.assertEqual(case["expected_destinations"], actual_destinations)
        

if __name__ == "__main__":
    unittest.main()
