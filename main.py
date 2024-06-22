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
    # obstacles = []
    
    flocks = [Flock(WIDTH, HEIGHT, BOID_NUMBER, BLUE), Flock(WIDTH, HEIGHT, BOID_NUMBER, RED)]
    # flocks = [Flock(WIDTH, HEIGHT, BOID_NUMBER, BLUE)]

    round_counter = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        board.fill(WHITE)

        for obstacle in obstacles:
            obstacle_ul = obstacle.get_upper_left_corner()
            obstacle_size = obstacle.get_size()
            pygame.draw.rect(board, BLACK, (obstacle_ul[0], obstacle_ul[1], obstacle_size, obstacle_size))

        round_start_formed = list(map(lambda f: f.formed, flocks))        
        # flocks[0].update(BOUNCE_EDGES, None, obstacles)
        flocks[0].update(BOUNCE_EDGES, flocks[1], obstacles)
        flocks[1].update(BOUNCE_EDGES, flocks[0], obstacles)
        [flock.draw(board) for flock in flocks]

        pygame.display.flip()
        clock.tick(TICK_DURATION)

        for i, flock in enumerate(flocks):
            if flock.formed is True and round_start_formed[i] is False:
                print(f'Flock {i+1} formed in round {round_counter}')
            elif flock.formed is False and round_start_formed[i] is True:
                print(f'Flock {i+1} fell apart in round {round_counter}') 
        round_counter += 1


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
