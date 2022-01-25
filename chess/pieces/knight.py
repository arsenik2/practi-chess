from chess.piece import Piece


class Knight(Piece):

    def __init__(self, color):
        super(Knight, self).__init__("Knight", "N", color)
