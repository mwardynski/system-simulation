from boid import Boid

COHESION_RADIUS = 100
ALIGNMENT_RADIUS = 50
SEPARATION_RADIUS = 15

class Flock:
    def __init__(self, width, height, size):
        self.boids = [Boid(width, height) for _ in range(size)]

    def draw(self, board):
        for boid in self.boids:
            boid.draw(board)
    
    def update(self):
        for boid in self.boids:
            self.update_by_cohesion(boid)
            self.update_by_alignment(boid)
            self.update_by_separation(boid)
            boid.update()

    def update_by_cohesion(self, boid):
        influ_vx, influ_vy = 0, 0
        count = 0
        for otherBoid in self.boids:
            if(boid == otherBoid):
                continue
            distance = boid.calculate_distance(otherBoid)
            if 0 < distance < COHESION_RADIUS:
                influ_vx += boid.vx
                influ_vy += boid.vy
                count += 1
        if count > 0:
            influ_vx /= count
            influ_vy /= count
        boid.vx += influ_vx
        boid.vy += influ_vy

    def update_by_alignment(self, boid):
        influ_vx, influ_vy = 0, 0
        count = 0
        for otherBoid in self.boids:
            if(boid == otherBoid):
                continue
            distance = boid.calculate_distance(otherBoid)
            if 0 < distance < ALIGNMENT_RADIUS:
                influ_vx += boid.vx
                influ_vy += boid.vy
                count += 1
        if count > 0:
            influ_vx /= count
            influ_vy /= count
        boid.vx += influ_vx
        boid.vy += influ_vy
    
    def update_by_separation(self, boid):
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
        boid.vx += influ_vx
        boid.vy += influ_vy