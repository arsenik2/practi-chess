from chess.piece import Piece


class Bishop(Piece):

    def __init__(self, color):
        super(Bishop, self).__init__("Bishop", "B", color)
