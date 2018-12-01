import pygame as pg
from constants import WHITE


class Seed:
    def __init__(self, coordinates):
        self.x, self.y = coordinates
        self.active = True

    def draw(self, screen):
        if self.active:
            pg.draw.rect(screen, WHITE, self.rect, 0)