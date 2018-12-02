from seed import Seed
from constants import BIG_SEED_SIZE, YELLOW
import pygame as pg


class BigSeed(Seed):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.width = self.height = BIG_SEED_SIZE
        self.x, self.y = coordinates

    def make_effect(self, game):
        if self.active:
            game.fear = True  # #позже надо будет сделать взаимодействие с таймером на карте
            self.active = False

    def draw(self, screen):
        pg.draw.circle(screen, YELLOW, (int(self.x), int(self.y)), BIG_SEED_SIZE)
