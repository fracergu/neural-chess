from chess_game import ChessGame, play_game, board_to_input
from model import create_model
from chess_display import main_loop
import numpy as np
import chess

model = create_model()
model.load_weights("chess_model.h5")

def handle_move(move):
    game.move_piece(move)

    if game.board.is_game_over():
        return

    # Luego de que el jugador mueve, el modelo juega automáticamente como negras
    input_data = board_to_input(game.board)
    predictions = model.predict(np.array([input_data]))[0]
    legal_moves = list(game.board.legal_moves)
    legal_predictions = [(move, predictions[chess.SQUARES.index(move.to_square)]) for move in legal_moves]
    sorted_moves = sorted(legal_predictions, key=lambda x: -x[1])
    best_move = sorted_moves[0][0]
    game.move_piece(best_move)

game = ChessGame()
main_loop(game.board, handle_move)