from chess.piece import Piece


class Pawn(Piece):

    def __init__(self, color):
        super(Pawn, self).__init__("Pawn", None, color)
        