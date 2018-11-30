import pygame as pg
from constants import SCR_HEIGHT, SCR_WIDTH, FPS, BGCOLOR
from ghost import Ghost
from pacman import Pacman
from map import Map


class Game:
    def __init__(self):
        self.map = Map()
        self.size = SCR_WIDTH, SCR_HEIGHT
        #SHOULD BE GIVEN MAP SIZE
        #self.width = self.map.width  #Should add smth for scoreboard
        #self.height = self.map.height
        #self.size = (self.width, self.height)
        self.screen = pg.display.set_mode(self.size, pg.RESIZABLE)
        self.gameover = False
        self.map.init_matrix()
        self.map.init_walls()
        self.fear = False

    def main_loop(self):
        while not self.gameover:
            self.process_events()
            self.process_logic()
            self.process_drawing()
            pg.time.wait(1000 // FPS)

    def process_events(self):
         for event in pg.event.get():
            if event.type == pg.QUIT:
                self.gameover = True
            self.map.check_event(event)

    def process_drawing(self):
        self.screen.fill(BGCOLOR)
        #SHOULD BE METHOD MAP.DRAW RECEIVING THE SCREEN
        #self.map.draw(self.screen)
        pg.display.flip()


    def process_logic(self):
        pass

