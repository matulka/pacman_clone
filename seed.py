import pygame
from constants import WHITE, SMALL_SEED_RADIUS


class Seed:
    def __init__(self, coordinates):
        self.x, self.y = coordinates
        self.radius = -1
        # #по сути это абстрактный класс, поэтому настоящее значение радиуса будет определено в дочерних классах
        self.active = True

    def draw(self, screen):
        if self.active:
            pygame.draw.circle(screen, WHITE, self.coordinates, self.radius, 0)