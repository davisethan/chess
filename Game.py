class Game:
    SIZE = 8
    ROWS = ("1", "2", "3", "4", "5", "6", "7", "8")
    COLUMNS = ("A", "B", "C", "D", "E", "F", "G", "H")
    WHITE = "WHITE"
    BLACK = "BLACK"
    FORMATTED_STRING = "^[P|N|B|R|Q|K][A-H][1-8][A-H][1-8]$"
    PAWN_STRING = "P"
    KNIGHT_STRING = "N"
    BISHOP_STRING = "B"
    ROOK_STRING = "R"
    QUEEN_STRING = "Q"
    KING_STRING = "K"
    CHECK = "CHECK"
    WHITE_WON = "WHITE_WON"
    BLACK_WON = "BLACK_WON"
    UNFINISHED = "UNFINISHED"
    WHITE_PAWN_ROW = 6
    BLACK_PAWN_ROW = 1
