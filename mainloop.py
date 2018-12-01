import pygame as pg
from constants import SCR_HEIGHT, SCR_WIDTH, FPS, BGCOLOR, WHITE
from map import Map
from constants import SCR_HEIGHT, SCR_WIDTH


class Game:
    def __init__(self):
        self.map = Map()
        self.size = SCR_WIDTH, SCR_HEIGHT
        #SHOULD BE GIVEN MAP SIZE
        self.width = SCR_WIDTH  #Should add smth for scoreboard
        self.height = SCR_HEIGHT
        self.size = (self.width, self.height)
        self.screen = pg.display.set_mode(self.size, pg.RESIZABLE)
        self.gameover = False
        self.fear = False
        self.point_counter = 0
        self.high_score = 0
        self.font_size = (self.height - self.map.height) // 8
        self.font = pg.font.SysFont('Comic Sans MS', self.font_size)

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
            #self.map.check_event(event)

    def process_drawing(self):
        self.screen.fill(BGCOLOR)
        #SHOULD BE METHOD MAP.DRAW RECEIVING THE SCREEN
        self.map.draw(self.screen)
        self.draw_score()
        pg.display.flip()

    def draw_score(self):
        cur_score_surface = self.font.render("CURRENT SCORE", True, WHITE)
        self.screen.blit(cur_score_surface, (self.width // 10, self.font_size))
        cur_points = str(self.point_counter)
        if '9' >= cur_points >= '0':
            cur_points = '0' + cur_points
        number_surface = self.font.render(cur_points, True, WHITE)
        self.screen.blit(number_surface, (self.width // 10 + cur_score_surface.get_width() -
                                          number_surface.get_width(), 2 * self.font_size))
        high_score_surface = self.font.render("HIGH SCORE", True, WHITE)
        self.screen.blit(high_score_surface, (self.width // 5 + cur_score_surface.get_width(),
                                              self.font_size))
        high_points = str(self.high_score)
        if '9' >= high_points >= '0':
            high_points = '0' + high_points
        number_surface = self.font.render(high_points, True, WHITE)
        self.screen.blit(number_surface, (self.width // 5 + cur_score_surface.get_width() +
                                          high_score_surface.get_width() -
                                          number_surface.get_width(), 2 * self.font_size))


    def process_logic(self):
        pass


