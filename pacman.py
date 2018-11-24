import pygame as pg
from character import Character
from constants import LEFT, RIGHT, DOWN, UP


class Pacman(Character):

    def __init__(self, coordinates):
        super().__init__(coordinates)

    def check_event(self, event):
        #Should check collisions with map
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                self.direction = LEFT
            if event.key == pg.K_d:
                self.direction = RIGHT
            if event.key == pg.K_w:
                self.direction = UP
            if event.key == pg.K_s:
                self.direction = DOWN

    def logic(self, game):
        for ghost in game.map.ghosts:
            if self.check_collision_with_ghost(ghost):
                game.gameover = True
        for seed in game.map.seeds:
            if self.check_collision_with_seed(seed):
                seed.make_effect()
        self.move()
        if self.check_collision_with_walls(map.walls):
            self.move_back()
