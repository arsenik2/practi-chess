from chess.chess import Chess

chess = Chess()
# for square in chess.board.board[::-1]:
#     print(square)

# print(chess.board.get_square(7, 0))

for i in range(chess.BOARD_SIZE - 1, -1, -1):
    print(' | '.join([str(chess.board.get_square(i, j)) for j in range(chess.BOARD_SIZE)]))

for i in range(chess.BOARD_SIZE - 1, -1, -1):
    print(' | '.join([chess.board.get_square(i, j).get_color() for j in range(chess.BOARD_SIZE)]))
