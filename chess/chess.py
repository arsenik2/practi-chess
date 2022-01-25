from chess.board import Board
from chess.square import Square
from chess.pieces import Bishop, King, Knight, Pawn, Queen, Rook


class Chess:

    BOARD_SIZE = 8

    def __init__(self):
        self.board = Board(self.BOARD_SIZE, self.BOARD_SIZE)
        self.init_chess_board()

    def init_chess_board(self):
        self.board.board = [Square(i, j) for i in 'abcdefgh' for j in range(1, 9)]
        self.board.place_piece(0, 0, Rook(True))
        self.board.place_piece(0, 1, Knight(True))
        self.board.place_piece(0, 2, Bishop(True))
        self.board.place_piece(0, 3, Queen(True))
        self.board.place_piece(0, 4, King(True))
        self.board.place_piece(0, 5, Bishop(True))
        self.board.place_piece(0, 6, Knight(True))
        self.board.place_piece(0, 7, Rook(True))
        for i in range(self.BOARD_SIZE):
            self.board.place_piece(1, i, Pawn(True))
            self.board.place_piece(6, i, Pawn(False))
        self.board.place_piece(7, 0, Rook(False))
        self.board.place_piece(7, 1, Knight(False))
        self.board.place_piece(7, 2, Bishop(False))
        self.board.place_piece(7, 3, Queen(False))
        self.board.place_piece(7, 4, King(False))
        self.board.place_piece(7, 5, Bishop(False))
        self.board.place_piece(7, 6, Knight(False))
        self.board.place_piece(7, 7, Rook(False))
