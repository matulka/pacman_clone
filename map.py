import pygame as pg
from constants import Black, White, width__scr, height__scr
from classes import Map


gameover = False
size = width_scr, height_scr = width__scr, height__scr
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
    map.init_matrix()
    map.init_walls()
    map.draw()

def main():
    global gameover
    init()
    while not gameover:
        handle_events()
        screen.fill(Black)
        init_map()
        pg.display.flip()
        pg.time.wait(20)

main()