import random
import math
import pygame

VELOCITY_LIMIT = 5
OBSTACLE_X = 400
OBSTACLE_Y = 300
OBSTACLE_SIZE = 50

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

    def applyInflus(self, influs):
        for influ in influs:
            self.vx += influ[0]
            self.vy += influ[1]

    def update(self, bounce_edges):
        self.scale_velocity()
        self.x += self.vx
        self.y += self.vy

        if bounce_edges:
            self.bounce_off_edges()
        else:
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

    def bounce_off_edges(self):
        if self.x < 0 or self.x > self.width:
            self.vx *= -1
            self.x = max(0, min(self.x, self.width))  # Ensure boid stays within bounds
        if self.y < 0 or self.y > self.height:
            self.vy *= -1
            self.y = max(0, min(self.y, self.height))  # Ensure boid stays within bounds

    def calculate_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def avoid_obstacle(self, obstacle_x, obstacle_y, obstacle_size):
        dx = obstacle_x - self.x
        dy = obstacle_y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        if distance < obstacle_size:
            avoid_force_x = self.x - obstacle_x
            avoid_force_y = self.y - obstacle_y
            return [avoid_force_x, avoid_force_y]
        return [0, 0]
