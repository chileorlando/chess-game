import pygame
from board import Board

class Game:
    def __init__(self, win):
        self.board = Board()
        self.win = win

    def update(self):
        """Redraws the game board and pieces."""
        self.board.draw(self.win)
        pygame.display.update()

    def handle_click(self, pos):
        """Handles piece selection and movement."""
        row, col = pos[1] // 80, pos[0] // 80
        print(f"Clicked on row {row}, col {col}")
