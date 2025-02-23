import pygame
from game import Game

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 640
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

def main():
    game = Game(WIN)
    running = True

    while running:
        game.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_click(pygame.mouse.get_pos())

    pygame.quit()

if __name__ == "__main__":
    main()
