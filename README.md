# neural-chess

A chess-playing AI application built with Python, Pygame, and TensorFlow.

## Overview

This project comprises a chess-playing AI that uses a deep neural network to determine its moves. The user can play as the white pieces, with the AI automatically playing as the black pieces after each move. The game state is visualized using the Pygame library, while the AI's logic is backed by TensorFlow.

## Structure

- `chess_display.py`: Manages the visual representation of the chessboard and its pieces using Pygame.
- `chess_game.py`: Contains the game logic and the ChessGame class that manages the game state.
- `main.py`: The entry point for running the game where the user plays against the AI.
- `model.py`: Contains the TensorFlow model and board encoding logic.
- `train.py`: Trains the AI model through self-play and updates based on game outcomes.

## Setup

1. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Train the model (iterations are optional)

    ```bash
    python train.py --iterations 1000
    ```

3. Run the game

    ```bash
    python main.py
    ```
