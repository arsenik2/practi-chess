from chess.piece import Piece


class Rook(Piece):

    def __init__(self, color):
        super(Rook, self).__init__("Rook", "R", color)
