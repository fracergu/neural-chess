import numpy as np
import chess
import tensorflow as tf
from model import create_model, board_to_input

class ChessGame:
    def __init__(self):
        self.board = chess.Board()

    def move_piece(self, move):
        if self.board.is_pseudo_legal(move):
            if self.board.piece_at(move.from_square).symbol() == 'P' and move.to_square in chess.SQUARES[56:64]:
                move = chess.Move(move.from_square, move.to_square, promotion=chess.QUEEN)  # Promote to Queen
            elif self.board.piece_at(move.from_square).symbol() == 'p' and move.to_square in chess.SQUARES[0:8]:
                move = chess.Move(move.from_square, move.to_square, promotion=chess.QUEEN)  # Promote to Queen
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

