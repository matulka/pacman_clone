import pygame as pg
from constants import BLACK, WHITE, WIDTH_SCR, HEIGHT_SCR
from classes import Map


gameover = False
size = width_scr, height_scr = WIDTH_SCR, HEIGHT_SCR
screen = None

def init():
    global screen
    pg.init()
    screen = pg.display.set_mode(size)


def handle_events():
    global gameover
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameover = True


def init_map():
    map = Map()

def main():
    global gameover
    init()
    while not gameover:
        handle_events()
        screen.fill(BLACK)
        init_map()
        pg.display.flip()
        pg.time.wait(20)

main()