from Board import Board
from Game import Game

class Chess:
    def play(_print = print, _input = input) -> None:
        chess = Chess(_print, _input)
        
        while Game.UNFINISHED == chess.get_game_state():
            move = ""
            while not chess._board.can_move(move):
                move = chess._input("Make move:")

            chess._board.do_move()
            
            end = chess._board.end_move()
            if Game.CHECK == end:
                chess._print("Check!")
            elif Game.WHITE_WON == end:
                chess._print("Check!")
                chess._print("Checkmate")
                chess.set_game_state(Game.WHITE_WON)
            elif Game.BLACK_WON == end:
                chess._print("Check!")
                chess._print("Checkmate")
                chess.set_game_state(Game.BLACK_WON)

    def __init__(self, _print = print, _input = input) -> None:
        self._board = Board()
        self._print = _print
        self._input = _input
        self._game_state = Game.UNFINISHED

    def get_game_state(self) -> str:
        return self._game_state

    def set_game_state(self, game_state: str) -> None:
        self._game_state = game_state

if __name__ == "__main__":
    Chess.play()
