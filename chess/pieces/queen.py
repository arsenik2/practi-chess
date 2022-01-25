from chess.piece import Piece


class Queen(Piece):

    def __init__(self, color):
        super(Queen, self).__init__("Queen", "Q", color)
