import random
import pygame

class Boid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

    def draw(self, board):
        pygame.draw.circle(board, "blue", (int(self.x), int(self.y)), 3)

    def update(self, flock):
        self.x += self.vx
        self.y += self.vy

        self.wrap_around_edges()


    def wrap_around_edges(self):
        if self.x < 0:
            self.x = self.width
        elif self.x > self.width:
            self.x = 0
        if self.y < 0:
            self.y = self.height
        elif self.y > self.height:
            self.y = 0