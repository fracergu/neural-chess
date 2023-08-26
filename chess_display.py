import pygame
import chess

# Dimensiones
WIDTH, HEIGHT = 480, 480
SQUARE_SIZE = WIDTH // 8

PIECE_SIZE_WIDTH = 1920 // 6  
PIECE_SIZE_HEIGHT = 640 // 2 

DARK_BROWN = (101, 67, 33)   
LIGHT_BROWN = (205, 133, 63) 

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def load_piece_image(x, y):
    image = spritesheet.subsurface((x * PIECE_SIZE_WIDTH, y * PIECE_SIZE_HEIGHT, PIECE_SIZE_WIDTH, PIECE_SIZE_HEIGHT))
    return pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))

spritesheet = pygame.image.load("sprites/chess-sprites.png")
PIECES = {
    'K': load_piece_image(0, 0),
    'Q': load_piece_image(1, 0),
    'B': load_piece_image(2, 0),
    'N': load_piece_image(3, 0),
    'R': load_piece_image(4, 0),
    'P': load_piece_image(5, 0),
    'k': load_piece_image(0, 1),
    'q': load_piece_image(1, 1),
    'b': load_piece_image(2, 1),
    'n': load_piece_image(3, 1),
    'r': load_piece_image(4, 1),
    'p': load_piece_image(5, 1),
}

dragging = False
dragged_piece = None
dragged_from_square = None

def draw_board(board):
    for row in range(8):
        for col in range(8):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(WINDOW, color, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            piece = board.piece_at(chess.square(row, col))
            if piece:
                piece_image = PIECES[str(piece)]
                WINDOW.blit(piece_image, (row * SQUARE_SIZE, col * SQUARE_SIZE))

    if dragging and dragged_piece:
        x, y = pygame.mouse.get_pos()
        WINDOW.blit(PIECES[dragged_piece], (x - SQUARE_SIZE // 2, y - SQUARE_SIZE // 2))

    pygame.display.flip()

def get_square_from_coords(x, y):
    return x // SQUARE_SIZE, y // SQUARE_SIZE

def main_loop(board, handle_move):
    global dragging, dragged_piece, dragged_from_square
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = get_square_from_coords(x, y)
                square = chess.square(row, col)
                piece = board.piece_at(square)
                if piece and piece.color == chess.WHITE:  # Si es una pieza blanca
                    dragging = True
                    dragged_piece = str(piece)
                    dragged_from_square = square

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                row, col = get_square_from_coords(x, y)
                to_square = chess.square(row, col)
                if dragging and dragged_from_square is not None:
                    move = chess.Move(dragged_from_square, to_square)
                    promo_move = None
                    if board.piece_at(dragged_from_square).symbol() == 'P' and to_square in chess.SQUARES[56:64]:
                        promo_move = chess.Move(dragged_from_square, to_square, promotion=chess.QUEEN)
                    elif board.piece_at(dragged_from_square).symbol() == 'p' and to_square in chess.SQUARES[0:8]:
                        promo_move = chess.Move(dragged_from_square, to_square, promotion=chess.QUEEN)

                    if promo_move and promo_move in board.legal_moves:
                        handle_move(promo_move)
                    elif move in board.legal_moves:
                        handle_move(move)

                dragging = False
                dragged_piece = None
                dragged_from_square = None


        draw_board(board)

    pygame.quit()

def update_display(board):
    draw_board(board)
    pygame.display.flip()
