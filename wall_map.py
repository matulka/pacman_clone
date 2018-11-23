import pygame
from constants import Black, White
size = width_scr, height_scr = 700, 700
screen = pygame.display.set_mode(size)


class Wall:
    def __init__(self, left, top, width_, height_):
        self.coords = (left, top)
        self.width, self.height = width_, height_
        self.rect = pygame.Rect(self.coords[0], self.coords[1], self.width, self.height)

    def draw(self):
        pygame.draw.rect(screen, White, self.rect, 0)


class Map:
    def __init__(self):
        self.game_map = []

    def add_ell(self, element):
        self.game_map.append(element)

    def clear(self):
        self.game_map.clear()

    def draw(self):
        for i in range(len(self.game_map)):
            self.game_map[i].draw()