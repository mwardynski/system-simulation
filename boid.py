import random
import math
import pygame

VELOCITY_LIMIT = 5

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

    def update(self):
        self.scale_velocity()
        self.x += self.vx
        self.y += self.vy

        self.wrap_around_edges()

    def scale_velocity(self):
        velocity = math.sqrt(self.vx**2 + self.vy**2)
        if velocity > VELOCITY_LIMIT:
            scale = VELOCITY_LIMIT / velocity
            self.vx *= scale
            self.vy *= scale

    def wrap_around_edges(self):
        if self.x < 0:
            self.x = self.width
        elif self.x > self.width:
            self.x = 0
        if self.y < 0:
            self.y = self.height
        elif self.y > self.height:
            self.y = 0

    def calculate_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)