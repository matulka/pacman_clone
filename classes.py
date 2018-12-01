import pygame as pg
from constants import BLACK, WHITE, MAP_PATH, WIDTH_SCR, HEIGHT_SCR, SPACE_BLOCKS

gameover = False
size = width_scr, height_scr = WIDTH_SCR, HEIGHT_SCR
screen = pg.display.set_mode(size)

class Wall:
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.rect = pg.Rect(x, y, self.width, self.height)

    def draw(self, screen):
        pg.draw.rect(screen, WHITE, self.rect, 0)

class Map:
    def __init__(self):
        self.height, self.width, self.top, self.bottom = None, None, None, None
        self.width_block, self.height_block = None, None
        self.walls = []
        self.seeds = []
        self.ghosts = []
        self.matrix = []
        self.init_matrix()
        self.init_constants()
        self.init_walls()
        self.get_width_height()
        self.draw()

    def init_constants(self):
        n = len(self.matrix[0])
        self.width_block = self.height_block = ((width_scr+SPACE_BLOCKS)/n)-SPACE_BLOCKS
        print(self.width_block, self.height_block)

    def get_width_height(self):
        self.width = width_scr
        self.height = self.walls[0].y-self.walls[-1].y
        self.top, self.bottom = self.walls[0].y, self.walls[-1].y+self.height_block

    def init_matrix(self):
        file = open(MAP_PATH, 'r')
        data = file.readlines()
        file.close()
        for i in range(len(data)):
            prom_data = list(data[i])
            data_local = list(map(int, prom_data[0:len(prom_data) - 1]))
            self.matrix.append(data_local)

    def init_walls(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 1:
                    wall_local = Wall(j * (self.width_block + SPACE_BLOCKS),
                                      i * (self.height_block + SPACE_BLOCKS)+width_scr//10,
                                      self.width_block, self.height_block)
                    self.walls.append(wall_local)

    def draw(self):
        for i in range(len(self.walls)):
            self.walls[i].draw(screen)

        for i in range(len(self.seeds)):
            self.seeds[i].draw(screen)

        for i in range(len(self.ghosts)):
            self.ghosts[i].draw(screen)

    def check_event(self):
        pass

