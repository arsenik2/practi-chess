from flask_socketio import emit
from main import socket_, chess


@socket_.on('get_chess_board', namespace='/chess')
def get_chess_board():
    emit('chess_board', {'data': chess.board})
