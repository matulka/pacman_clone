import pygame as pg
from constants import BLACK, WHITE, MAP_PATH, SCR_HEIGHT, SCR_WIDTH, SPACE_BLOCKS, BIG_SEED_SIZE, BLUE
from smallseed import SmallSeed
from bigseed import BigSeed
from ghost import Ghost
from pacman import Pacman

gameover = False
size = width_scr, height_scr = SCR_HEIGHT, SCR_WIDTH
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
        self.ghosts_teleport = None
        self.pacman = None
        self.walls = []
        self.seeds = []
        self.ghosts = []
        self.matrix = []
        self.init_matrix()
        self.init_constants()
        self.init_walls()
        self.get_width_height()
        self.init_ghosts_teleport()
        self.init_pacman()
        self.init_seeds()
        self.init_ghosts()
        self.draw(screen)

    def init_pacman(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 5:
                    coords = (j * (self.width_block + SPACE_BLOCKS)-self.width_block//2.5,
                              i * (self.height_block + SPACE_BLOCKS) + SCR_HEIGHT // 11)
                    self.pacman = Pacman(coords, self.width_block)

    def init_seeds(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 6:
                    coords = (j * (self.width_block + SPACE_BLOCKS) + self.width_block//3,
                              i * (self.height_block + SPACE_BLOCKS) + SCR_HEIGHT // 9)
                    small_seed_local = SmallSeed(coords)
                    self.seeds.append(small_seed_local)
                if self.matrix[i][j] == 7:
                    coords = (j * (self.width_block + SPACE_BLOCKS)+BIG_SEED_SIZE//1.1,
                              i * (self.height_block + SPACE_BLOCKS) + SCR_HEIGHT // 8.9)
                    big_seed_local = BigSeed(coords)
                    self.seeds.append(big_seed_local)

    def init_ghosts(self):
        colors = ['blue', 'red', 'orange', 'pink']
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 1 or self.matrix[i][j] == 2 or self.matrix[i][j] == 3\
                        or self.matrix[i][j] == 4:
                    coords = (j * (self.width_block + SPACE_BLOCKS) - self.width_block//2.5,
                                   i * (self.height_block + SPACE_BLOCKS) + SCR_HEIGHT // 11)
                    ghost_local = Ghost(coords, colors[self.matrix[i][j]-1], self.width_block, self.ghosts_teleport)
                    self.ghosts.append(ghost_local)

    def init_ghosts_teleport(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 9:
                    self.ghosts_teleport = (j * (self.width_block + SPACE_BLOCKS) - self.width_block//3,
                                   i * (self.height_block + SPACE_BLOCKS) + SCR_HEIGHT // 10)

    def refresh(self):
        self.init_pacman()
        self.init_seeds()
        self.init_ghosts()


    def init_constants(self):
        n = len(self.matrix[0])
        self.width_block = self.height_block = ((width_scr+SPACE_BLOCKS)/n)-SPACE_BLOCKS

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
                if self.matrix[i][j] == 8:
                    wall_local = Wall(j * (self.width_block + SPACE_BLOCKS),
                                      i * (self.height_block + SPACE_BLOCKS)+width_scr//10,
                                      self.width_block, self.height_block)
                    self.walls.append(wall_local)

    def draw(self, screen):
        for i in range(len(self.walls)):
            self.walls[i].draw(screen)

        for i in range(len(self.seeds)):
            self.seeds[i].draw(screen)

        for i in range(len(self.ghosts)):
            self.ghosts[i].draw(screen)

        self.pacman.draw(screen)

    def check_event(self, event):
        pass
