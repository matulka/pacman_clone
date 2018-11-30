import pygame as pg
import sys

from mainloop import Game

def main():
    pg.init()
    #pg.font.init()
    g = Game()
    g.main_loop()
    sys.exit()  # Завершение программы


main()
