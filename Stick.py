import pygame
import numpy as np

class Stick:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b
        self.length = np.linalg.norm(self.point_a.pos - self.point_b.pos)
        self.max_iterations = 100
    
    def update(self):
        for _ in range(self.max_iterations):
            center = (self.point_a.pos + self.point_b.pos) / 2
            dir = (self.point_a.pos - self.point_b.pos)
            dir = dir / np.linalg.norm(dir)
            if not self.point_a.locked:
                self.point_a.pos = center + dir * self.length / 2
            if not self.point_b.locked:
                self.point_b.pos = center - dir * self.length / 2
    
    def draw(self, WIN):
        pygame.draw.line(WIN, [255] * 3, self.point_a.pos, self.point_b.pos)