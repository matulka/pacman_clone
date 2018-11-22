from constants import SMALL_SEED_RADIUS, SMALL_SEED_POINTS
from seed import Seed


class SmallSeed(Seed):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.radius = SMALL_SEED_RADIUS

    def make_effect(self, map):
        if self.active:
            map.point_counter += SMALL_SEED_POINTS
            self.active = False
