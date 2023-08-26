import numpy as np
import chess
import tensorflow as tf
from model import create_model, board_to_input

class ChessGame:
    def __init__(self):
        self.board = chess.Board()

    def move_piece(self, move):
        self.board.push(move)

    def get_board(self):
        return str(self.board)

def play_game(model):
    game = ChessGame()
    while not game.board.is_game_over():
        input_data = board_to_input(game.board)
        predictions = model.predict(np.array([input_data]))
        move = chess.Move.from_uci(predictions[0])
        game.move_piece(move)
    return game.board.result()

