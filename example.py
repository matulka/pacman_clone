import pygame
import sys

from menu import Menu


def hello():
    pygame.init()  # Инициализация библиотеки
    #xpygame.font.init()
    Menu().main_loop()
    sys.exit()  # Завершение программы


if __name__ == "__main__":
    hello()
