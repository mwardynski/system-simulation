class Obstacle:

    def __init__(self, x, y, size):
        self.x_center = x
        self.y_center = y
        self.size = size

    def get_center(self):
        return (self.x_center, self.y_center)

    def get_upper_left_corner(self):
        return (self.x_center - self.size/2, self.y_center - self.size/2)
    
    def get_size(self):
        return self.size
