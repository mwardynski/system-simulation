import pygame
from flock import Flock

WHITE = (255, 255, 255)

WIDTH = 800
HEIGHT = 600
WINDOW_TITLE = "School of Fish"

BOID_NUMBER = 100
TICK_DURATION = 50

def main():
    pygame.init()
    board = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    clock = pygame.time.Clock()
    running = True

    flock = Flock(WIDTH, HEIGHT, BOID_NUMBER)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        board.fill(WHITE)

        flock.update()
        flock.draw(board)

        pygame.display.flip()
        clock.tick(TICK_DURATION)

    pygame.quit()

if __name__ == "__main__":
    main()