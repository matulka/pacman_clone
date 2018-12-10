from seed import Seed
from constants import BIG_SEED_SIZE, YELLOW
import pygame as pg
from time import time


class BigSeed(Seed):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.width = self.height = BIG_SEED_SIZE
        self.x, self.y = coordinates
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def make_effect(self, game):
        if self.active:
            game.fear = True  # #позже надо будет сделать взаимодействие с таймером на карте
            for ghost in game.map.ghosts: # #может быть проблема, что призраки передаются не по ссылке
                ghost.change_sprites('fear')
            game.time_of_fear_start = time()
            self.active = False

    def draw(self, screen):
        if self.active:
            pg.draw.circle(screen, YELLOW, (int(self.x), int(self.y)), BIG_SEED_SIZE)
