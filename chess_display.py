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

def draw_board(board):
    for row in range(8):
        for col in range(8):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(WINDOW, color, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            piece = board.piece_at(chess.square(row, col))
            if piece:
                piece_image = PIECES[str(piece)]
                WINDOW.blit(piece_image, (row * SQUARE_SIZE, col * SQUARE_SIZE))

    pygame.display.flip()

def main_loop():
    board = chess.Board()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board(board)

    pygame.quit()

def update_display(board):
    draw_board(board)
    pygame.display.flip()
