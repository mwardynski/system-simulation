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
    
    def update(self):
        for boid in self.boids:
            influ_vx = 0
            influ_vy = 0
            count_cohesion = 0
            count_alignment = 0
            count_separation = 0

            for otherBoid in self.boids:
                if boid == otherBoid:
                    continue
                
                distance = boid.calculate_distance(otherBoid)

                # Cohesion
                if 0 < distance < COHESION_RADIUS:
                    influ_vx += otherBoid.x
                    influ_vy += otherBoid.y
                    count_cohesion += 1

                # Alignment
                if 0 < distance < ALIGNMENT_RADIUS:
                    influ_vx += otherBoid.vx
                    influ_vy += otherBoid.vy
                    count_alignment += 1

                # Separation
                if 0 < distance < SEPARATION_RADIUS:
                    influ_vx += boid.x - otherBoid.x
                    influ_vy += boid.y - otherBoid.y
                    count_separation += 1
            
            # Apply influences, scaling to avoid excessive clustering or dispersal
            if count_cohesion > 0:
                influ_vx /= count_cohesion
                influ_vy /= count_cohesion
                influ_vx *= 0.15  # Scale down the influence
                influ_vy *= 0.15

            if count_alignment > 0:
                influ_vx /= count_alignment
                influ_vy /= count_alignment
                influ_vx *= 0.5  # Scale down the influence
                influ_vy *= 0.5

            if count_separation > 0:
                influ_vx /= count_separation
                influ_vy /= count_separation
                influ_vx *= 0.2  # Scale down the influence
                influ_vy *= 0.2

            boid.applyInflus(influ_vx, influ_vy)
            boid.update()
