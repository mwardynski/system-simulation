import pygame
from flock import Flock

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 600
WINDOW_TITLE = "School of Fish"

BOID_NUMBER = 30
TICK_DURATION = 50
OBSTACLE_X = 400
OBSTACLE_Y = 300
OBSTACLE_SIZE = 50

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

        # Draw the obstacle
        pygame.draw.rect(board, BLACK, (OBSTACLE_X - OBSTACLE_SIZE // 2, OBSTACLE_Y - OBSTACLE_SIZE // 2, OBSTACLE_SIZE, OBSTACLE_SIZE))

        flock.update()
        flock.draw(board)

        pygame.display.flip()
        clock.tick(TICK_DURATION)

    pygame.quit()

if __name__ == "__main__":
    main()
