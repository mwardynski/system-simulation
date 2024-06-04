import pygame
from flock import Flock

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

WIDTH = 800
HEIGHT = 600
WINDOW_TITLE = "School of Fish"

BOID_NUMBER = 30
TICK_DURATION = 50
OBSTACLE_X = 400
OBSTACLE_Y = 300
OBSTACLE_SIZE = 50
SMALL_OBSTACLE_SIZE = 20
BOUNCE_EDGES = False

def main():
    pygame.init()
    board = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    clock = pygame.time.Clock()
    running = True

    flock1 = Flock(WIDTH, HEIGHT, BOID_NUMBER, BLUE)
    flock2 = Flock(WIDTH, HEIGHT, BOID_NUMBER, RED)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        board.fill(WHITE)

        pygame.draw.rect(board, BLACK, (OBSTACLE_X - OBSTACLE_SIZE // 2, OBSTACLE_Y - OBSTACLE_SIZE // 2, OBSTACLE_SIZE, OBSTACLE_SIZE))

        offset = OBSTACLE_SIZE // 2 + SMALL_OBSTACLE_SIZE // 2 + 100
        small_obstacles = [
            (OBSTACLE_X - offset, OBSTACLE_Y - offset),
            (OBSTACLE_X + offset, OBSTACLE_Y - offset),
            (OBSTACLE_X - offset, OBSTACLE_Y + offset),
            (OBSTACLE_X + offset, OBSTACLE_Y + offset)
        ]
        for (ox, oy) in small_obstacles:
            pygame.draw.rect(board, BLACK, (ox - SMALL_OBSTACLE_SIZE // 2, oy - SMALL_OBSTACLE_SIZE // 2, SMALL_OBSTACLE_SIZE, SMALL_OBSTACLE_SIZE))

        flock1.update(BOUNCE_EDGES, flock2)
        flock2.update(BOUNCE_EDGES, flock1)
        flock1.draw(board)
        flock2.draw(board)

        pygame.display.flip()
        clock.tick(TICK_DURATION)

    pygame.quit()

if __name__ == "__main__":
    main()
