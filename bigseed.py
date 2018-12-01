from seed import Seed
from constants import BIG_SEED_SIZE
import pygame as pg


class BigSeed(Seed):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.width = self.height = BIG_SEED_SIZE
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def make_effect(self, game):
        if self.active:
            game.fear = True  # #позже надо будет сделать взаимодействие с таймером на карте
            self.active = False
