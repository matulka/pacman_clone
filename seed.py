import pygame as pg
from constants import YELLOW


class Seed:
    def __init__(self, coordinates):
        self.x, self.y = coordinates
        self.active = True

    def draw(self, screen):
        if self.active:
            pg.draw.rect(screen, YELLOW, self.rect, 0)