from chess_game import ChessGame, play_game
from model import create_model
from chess_display import main_loop

model = create_model()
model.load_weights("chess_model.h5")

game = ChessGame()
print(game.get_board())

while not game.board.is_game_over():
    move_uci = input("Enter your move (UCI format): ")
    move = chess.Move.from_uci(move_uci)
    game.move_piece(move)
    print(game.get_board())

    play_game(model)

