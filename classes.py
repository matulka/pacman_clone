import pygame as pg
from constants import Black, White, map_path, width__scr, height__scr, width_block, height_block

gameover = False
size = width_scr, height_scr = width__scr, height__scr
screen = pg.display.set_mode(size)

class Wall:
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.rect = pg.Rect(x, y, self.width, self.height)

    def draw(self):
        pg.draw.rect(screen, White, self.rect, 0)

class Map:
    def __init__(self):
        self.walls = []
        self.seeds = []
        self.ghosts = []
        self.matrix = []

    def init_matrix(self):
        file = open(map_path, 'r')
        data = file.readlines()
        file.close()
        for i in range(len(data)):
            prom_data = list(data[i])
            data_local = list(map(int, prom_data[0:len(prom_data) - 1]))
            self.matrix.append(data_local)

    def init_walls(self):
        x_del = len(self.matrix[0])
        y_del = len(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 1:
                    wall_local = Wall(j * (height_scr / x_del), i * (height_scr / y_del), width_block, height_block)
                    self.walls.append(wall_local)


    def check_event(self):
        pass

    def draw(self):
        for i in range(len(self.walls)):
            self.walls[i].draw()

        for i in range(len(self.seeds)):
            self.seeds[i].draw()

        for i in range(len(self.ghosts)):
            self.ghosts[i].draw()

