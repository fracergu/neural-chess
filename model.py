import tensorflow as tf
import chess

def board_to_input(board):
    mapping = {
        '.': 0, 'P': 1, 'N': 2, 'B': 3, 'R': 4, 'Q': 5, 'K': 6,
        'p': -1, 'n': -2, 'b': -3, 'r': -4, 'q': -5, 'k': -6
    }
    board_str = str(board).replace(' ', '').replace('\n', '')
    input_data = [mapping[char] for char in board_str]
    return input_data

def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Input(shape=(64,)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(len(chess.SQUARES), activation='softmax')
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

