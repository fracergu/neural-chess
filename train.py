import argparse
import os
import tensorflow as tf
from model import create_model, board_to_input
from chess_game import ChessGame
import numpy as np
import chess
from chess_display import update_display

parser = argparse.ArgumentParser(description='Train the chess model.')
parser.add_argument('--iterations', type=int, default=100, help='Number of training iterations.')
args = parser.parse_args()

model = create_model()

model_path = "chess_model.h5"
if os.path.exists(model_path):
    model.load_weights(model_path)

for _ in range(args.iterations):
    game = ChessGame()

    while not game.board.is_game_over():
        input_data = board_to_input(game.board)
        predictions = model.predict(np.array([input_data]))[0]

        legal_moves = list(game.board.legal_moves)

        # Filter predictions to only legal moves
        legal_predictions = [(move, predictions[chess.SQUARES.index(move.to_square)]) for move in legal_moves]
        sorted_moves = sorted(legal_predictions, key=lambda x: -x[1])

        # Exploratory move
        if np.random.random() < 0.1:  # 10% chance
            best_move = np.random.choice(legal_moves)
        else:
            best_move = sorted_moves[0][0]

        game.move_piece(best_move)

        # Calculate reward based on the move's consequence
        reward = 0
        if game.board.is_checkmate():
            reward = 1  # Only focus on checkmate

        model.fit(np.array([input_data]), np.array([reward]), epochs=1)

        update_display(game.board)

    # After game over, provide additional reward/penalty based on game result
    result = game.board.result()
    if result == "1-0":  # white wins
        reward = 1
    elif result == "0-1":  # black wins
        reward = -1
    else:  # draw
        reward = 0

    model.fit(np.array([input_data]), np.array([reward]), epochs=1)

model.save_weights(model_path)
