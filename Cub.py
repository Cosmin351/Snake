import pygame

class Patrat:
    def __init__(self, pos_x, pos_y, x_speed, y_speed, culoare):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.culoare = culoare
        self.x_speed = x_speed
        self.y_speed = y_speed
    def draw(self, ecran):
        pygame.draw.rect(ecran, self.culoare, [self.pos_x, self.pos_y, 10, 10])