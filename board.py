import pygame
from pieces import Piece, Pawn, Rook, Knight, Bishop, Queen, King

# Constants
ROWS, COLS = 8, 8
SQUARE_SIZE = 80

class Board:
    def __init__(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.create_board()

    def create_board(self):
        """Initializes pieces on the board."""
        # Place pawns
        for col in range(COLS):
            self.board[1][col] = Pawn("black", 1, col)
            self.board[6][col] = Pawn("white", 6, col)

        # Place other pieces
        back_row = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece in enumerate(back_row):
            self.board[0][i] = piece("black", 0, i)
            self.board[7][i] = piece("white", 7, i)

    def draw(self, win):
        """Draws the chessboard and pieces."""
        colors = [pygame.Color("white"), pygame.Color("gray")]
        for row in range(ROWS):
            for col in range(COLS):
                color = colors[(row + col) % 2]
                pygame.draw.rect(win, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                piece = self.board[row][col]
                if piece:
                    piece.draw(win)
