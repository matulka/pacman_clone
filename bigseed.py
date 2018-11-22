from constants import BIG_SEED_RADIUS
from seed import Seed


class BigSeed(Seed):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.radius = BIG_SEED_RADIUS

    def make_effect(self, game_map):
        if self.active:
            game_map.fear = True # #позже надо будет сделать взаимодействие с таймером на карте
            self.active = False
