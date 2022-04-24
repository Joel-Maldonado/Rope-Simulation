import pygame
import numpy as np

class Point:
    def __init__(self, position, radius=5):
        self.pos = position
        self.pos_prev = None
        self.radius = radius
        self.locked = False

    def draw(self, WIN):
        pygame.draw.circle(WIN, [255] * 3 if not self.locked else [255, 0, 0], self.pos, self.radius)
    
    def update(self, gravity):
        if not self.locked:
            pos_before_update = self.pos.copy()
            if self.pos_prev is not None:
                self.pos += self.pos - self.pos_prev
            self.pos += np.array([0, gravity])
            self.pos_prev = pos_before_update
    
    def is_clicked(self, pos):
        return np.linalg.norm(pos - self.pos) <= self.radius * 1.5