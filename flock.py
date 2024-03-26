from boid import Boid

class Flock:
    def __init__(self, width, height, size):
        self.boids = [Boid(width, height) for _ in range(size)]

    def draw(self, board):
        for boid in self.boids:
            boid.draw(board)
    
    def update(self):
        for boid in self.boids:
            boid.update(self.boids)