from constants import SMALL_SEED_POINTS
from seed import Seed


class SmallSeed(Seed):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.sprite = 0 # #позже здесь будет изображение большого зерна

    def make_effect(self, game):
        if self.active:
            game.point_counter += SMALL_SEED_POINTS
            self.active = False
