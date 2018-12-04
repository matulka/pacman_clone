import pygame as pg
import sys

from mainloop import Game


def hello():
    pg.init()
    pg.font.init()
    g = Game()
    g.main_loop()
    sys.exit()


if __name__ == '__main__':
    hello()
