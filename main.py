import pygame
from flock import Flock
from obstacle import Obstacle

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

    obstacles = generateObstacles()
    flock1 = Flock(WIDTH, HEIGHT, BOID_NUMBER, BLUE)
    flock2 = Flock(WIDTH, HEIGHT, BOID_NUMBER, RED)
    

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        board.fill(WHITE)

        for obstacle in obstacles:
            obstacle_ul = obstacle.get_upper_left_corner()
            obstacle_size = obstacle.get_size()
            pygame.draw.rect(board, BLACK, (obstacle_ul[0], obstacle_ul[1], obstacle_size, obstacle_size))

        flock1.update(BOUNCE_EDGES, flock2, obstacles)
        flock2.update(BOUNCE_EDGES, flock1, obstacles)
        flock1.draw(board)
        flock2.draw(board)

        pygame.display.flip()
        clock.tick(TICK_DURATION)

    pygame.quit()

def generateObstacles():
    offset = OBSTACLE_SIZE // 2 + SMALL_OBSTACLE_SIZE // 2 + 100
    obstacles = [
        Obstacle(OBSTACLE_X, OBSTACLE_Y, OBSTACLE_SIZE),
        Obstacle(OBSTACLE_X - offset, OBSTACLE_Y - offset, SMALL_OBSTACLE_SIZE),
        Obstacle(OBSTACLE_X + offset, OBSTACLE_Y - offset, SMALL_OBSTACLE_SIZE),
        Obstacle(OBSTACLE_X - offset, OBSTACLE_Y + offset, SMALL_OBSTACLE_SIZE),
        Obstacle(OBSTACLE_X + offset, OBSTACLE_Y + offset, SMALL_OBSTACLE_SIZE)
    ]
    return obstacles
        


if __name__ == "__main__":
    main()
