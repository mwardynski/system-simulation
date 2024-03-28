import random
from boid import Boid

COHESION_RADIUS = 100
ALIGNMENT_RADIUS = 50
SEPARATION_RADIUS = 85

class Flock:
    def __init__(self, width, height, size):
        self.boids = [Boid(width, height) for _ in range(size)]

    def draw(self, board):
        for boid in self.boids:
            boid.draw(board)

    def check_if_flock_formed(self):
        # we will check if distance between boids is less than than some value, if yes then flock is formed
        for i in range(len(self.boids)):
            for j in range(i+1, len(self.boids)):
                if self.boids[i].calculate_distance(self.boids[j]) > 100:
                    return False
        return True
    
    def update(self):
        for boid in self.boids:
            influs = []
            influs.append(self.calc_influ_by_cohesion(boid))
            influs.append(self.calc_influ_by_alignment(boid))
            influs.append(self.calc_influ_by_separation(boid))
            boid.applyInflus(influs)
            boid.update()

    def calc_influ_by_cohesion(self, boid):
        influ_vx, influ_vy = 0, 0
        count = 0
        for otherBoid in self.boids:
            if(boid == otherBoid):
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
            if(boid == otherBoid):
                continue
            distance = boid.calculate_distance(otherBoid)
            if 0 < distance < ALIGNMENT_RADIUS:
                influ_vx += otherBoid.vx
                influ_vy += otherBoid.vy
                count += 1
        if count > 0:
            influ_vx /= count
            influ_vy /= count
    
        if self.check_if_flock_formed():
            noise_scale = 1.5
            noise_vx = random.uniform(-noise_scale, noise_scale)
            noise_vy = random.uniform(-noise_scale, noise_scale)

            influ_vx += noise_vx
            influ_vy += noise_vy

        return [influ_vx, influ_vy]
    
    def calc_influ_by_separation(self, boid):
        influ_vx, influ_vy = 0, 0
        count = 0
        for otherBoid in self.boids:
            if(boid == otherBoid):
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