import pygame
import numpy as np
from Point import Point
from Stick import Stick


# Display
SIZE = (1000, 950)
WIN = pygame.display.set_mode(SIZE)

# Constants
GRAVITY = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

def simulate(points, sticks):
    for point in points:
        point.update(GRAVITY)
    
    for stick in sticks:
        stick.update()

def main():
    paused = True

    points = []
    sticks = []

    clock = pygame.time.Clock()
    running = True
    while running:
        WIN.fill([0, 0, 0])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and paused:
                mouse_pos = np.array(pygame.mouse.get_pos())
                clicked_point = False

                for point in points:
                    if point.is_clicked(mouse_pos):
                        point.locked = not point.locked
                        clicked_point = True

                if not clicked_point:
                    points.append(Point(mouse_pos))
                    if len(points) > 1:
                        sticks.append(Stick(points[-2], points[-1]))
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False

        if not paused:
            simulate(points, sticks)
        
        for stick in sticks:
            stick.draw(WIN)

        for point in points:
            point.draw(WIN)
        

        pygame.display.set_caption(f"FPS: {clock.get_fps()}")
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()