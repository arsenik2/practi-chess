class Board:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = []

    def get_square(self, x, y):
        index = self.get_board_index(x, y)
        if len(self.board) > index:
            return self.board[index]
        return None

    def get_board_index(self, x, y):
        x = x % self.width
        y = y % self.height
        return self.height * y + x

    def place_piece(self, x, y, piece):
        square = self.get_square(x, y)
        if square:
            square.piece = piece
