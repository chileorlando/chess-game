import pygame

SQUARE_SIZE = 80
PIECE_IMAGES = {
    "white_pawn": "assets/white_pawn.png",
    "black_pawn": "assets/black_pawn.png",
    # Add other piece images...
}

class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.image = pygame.image.load(PIECE_IMAGES[f"{color}_{self.__class__.__name__.lower()}"])

    def draw(self, win):
        """Draws the piece on the board."""
        win.blit(self.image, (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE))

class Pawn(Piece): pass
class Rook(Piece): pass
class Knight(Piece): pass
class Bishop(Piece): pass
class Queen(Piece): pass
class King(Piece): pass
