from seed import Seed


class BigSeed(Seed):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.sprite = 0 # #позже здесь будет изображение большого зерна

    def make_effect(self, game):
        if self.active:
            game.fear = True # #позже надо будет сделать взаимодействие с таймером на карте
            self.active = False
