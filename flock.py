import random
import math
from boid import Boid

COHESION_RADIUS = 100
ALIGNMENT_RADIUS = 50
SEPARATION_RADIUS = 85

FORMED_MAX_DISTANCE = 100

class Flock:
    def __init__(self, width, height, size, color):
        self.boids = [Boid(width, height, color) for _ in range(size)]
        self.color = color
        self.formed = False

    def draw(self, board):
        for boid in self.boids:
            boid.draw(board)

    def check_if_flock_formed(self):
        to_check = [self.boids[0]]
        included = [False for _ in range(len(self.boids))]
        included[0] = True
        included_counter = 1

        while len(to_check) > 0:
            selected_boid = to_check.pop()
            for i, boid in enumerate(self.boids):
                if boid is selected_boid or included[i]:
                    continue
                distance = math.sqrt((selected_boid.x - boid.x)**2 + (selected_boid.y - boid.y)**2)
                if distance <= FORMED_MAX_DISTANCE:
                    to_check.append(boid)
                    included[i] = True
                    included_counter += 1
                if len(self.boids) == included_counter:
                    return True
        
        return len(self.boids) == included_counter

    def update(self, bounce_edges, other_flock, obstacles):
        for boid in self.boids:
            influs = []
            influs.append(self.calc_influ_by_cohesion(boid))
            influs.append(self.calc_influ_by_alignment(boid))
            influs.append(self.calc_influ_by_separation(boid))
            # influs.append(boid.avoid_obstacle(OBSTACLE_X, OBSTACLE_Y, OBSTACLE_SIZE))
            for obstacle in obstacles:
                influs.append(boid.avoid_obstacle(obstacle))
            influs.extend(self.handle_inter_flock_collisions(boid, other_flock))
            boid.applyInflus(influs)
            boid.update(bounce_edges)

    def calc_influ_by_cohesion(self, boid):
        influ_vx, influ_vy = 0, 0
        count = 0
        for otherBoid in self.boids:
            if boid == otherBoid:
                continue
            distance = boid.calculate_distance(otherBoid)
            if 0 < distance < COHESION_RADIUS:
                influ_vx += otherBoid.x
                influ_vy += otherBoid.y
                count += 1
        if count > 0:
            influ_vx /= count
            influ_vx -= boid.x
            influ_vy /= count
            influ_vy -= boid.y
        return [influ_vx, influ_vy]

    def calc_influ_by_alignment(self, boid):
        influ_vx, influ_vy = 0, 0
        count = 0
        for otherBoid in self.boids:
            if boid == otherBoid:
                continue
            distance = boid.calculate_distance(otherBoid)
            if 0 < distance < ALIGNMENT_RADIUS:
                influ_vx += otherBoid.vx
                influ_vy += otherBoid.vy
                count += 1
        if count > 0:
            influ_vx /= count
            influ_vy /= count

        self.formed = self.check_if_flock_formed()
        noise_scale = 1.5 if self.formed else 0.5
        noise_vx = random.uniform(-noise_scale, noise_scale)
        noise_vy = random.uniform(-noise_scale, noise_scale)

        influ_vx += noise_vx
        influ_vy += noise_vy

        return [influ_vx, influ_vy]
    
    def calc_influ_by_separation(self, boid):
        influ_vx, influ_vy = 0, 0
        count = 0
        for otherBoid in self.boids:
            if boid == otherBoid:
                continue
            distance = boid.calculate_distance(otherBoid)
            if 0 < distance < SEPARATION_RADIUS:
                influ_vx += boid.x - otherBoid.x
                influ_vy += boid.y - otherBoid.y
                count += 1
        if count > 0:
            influ_vx /= count
            influ_vy /= count
        return [influ_vx, influ_vy]

    def handle_inter_flock_collisions(self, boid, other_flock):
        influs = []
        for otherBoid in other_flock.boids:
            influs.append(boid.avoid_other_boids(otherBoid))
        return influs

    def additional_obstacles(self):
        offset = OBSTACLE_SIZE // 2 + SMALL_OBSTACLE_SIZE // 2 + 10
        return [
            (OBSTACLE_X - offset, OBSTACLE_Y - offset, SMALL_OBSTACLE_SIZE),
            (OBSTACLE_X + offset, OBSTACLE_Y - offset, SMALL_OBSTACLE_SIZE),
            (OBSTACLE_X - offset, OBSTACLE_Y + offset, SMALL_OBSTACLE_SIZE),
            (OBSTACLE_X + offset, OBSTACLE_Y + offset, SMALL_OBSTACLE_SIZE)
        ]
