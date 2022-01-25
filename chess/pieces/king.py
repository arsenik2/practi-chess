from chess.piece import Piece


class King(Piece):

    def __init__(self, color):
        super(King, self).__init__("King", "K", color)
