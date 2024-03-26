import random
import pygame

class Boid:
    def __init__(self, width, height):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)

    def draw(self, board):
        pygame.draw.circle(board, "blue", (int(self.x), int(self.y)), 3)