import random
import math
import pygame

VELOCITY_LIMIT = 5
INFLU_FACTOR = 1

class Boid:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

    def draw(self, board):
        pygame.draw.circle(board, self.color, (int(self.x), int(self.y)), 3)

    def applyInflus(self, influs):
        for influ in influs:
            self.vx += INFLU_FACTOR * influ[0]
            self.vy += INFLU_FACTOR * influ[1]

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
            self.x = max(0, min(self.x, self.width))
        if self.y < 0 or self.y > self.height:
            self.vy *= -1

    def calculate_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def avoid_obstacle(self, obstacle):
        obstacle_x, obstacle_y = obstacle.get_center()
        obstacle_size = obstacle.get_size()
        dx = obstacle_x - self.x
        dy = obstacle_y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        if distance < obstacle_size:
            avoid_force_x = self.x - obstacle_x
            avoid_force_y = self.y - obstacle_y
            return [avoid_force_x, avoid_force_y]
        return [0, 0]

    def avoid_other_boids(self, other):
        avoid_force_x, avoid_force_y = 0, 0
        distance = self.calculate_distance(other)
        if distance < 20:
            avoid_force_x = self.x - other.x
            avoid_force_y = self.y - other.y
        return [avoid_force_x, avoid_force_y]
