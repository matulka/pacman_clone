from constants import SMALL_SEED_POINTS, SMALL_SEED_SIZE
from seed import Seed
import pygame as pg


class SmallSeed(Seed):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.width = self.height = SMALL_SEED_SIZE
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def make_effect(self, game):
        if self.active:
            game.point_counter += SMALL_SEED_POINTS
            self.active = False

