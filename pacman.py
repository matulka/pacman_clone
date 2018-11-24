import pygame as pg
from character import Character
from constants import CHARACTER_SPEED, CHARACTER_HEIGHT, CHARACTER_WIDTH, LEFT,\
    RIGHT, DOWN, UP, PACMAN_RADIUS, YELLOW, BGCOLOR, GAMEOVER


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

    def check_collision_with_walls(self, walls):
        collided = False
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                collided = True
        return collided

    def check_collision_with_seed(self, seed):
        if self.rect.colliderect(seed.rect):
            return True
        else:
            return False

    def check_collision_with_ghost(self, ghost):
        if self.rect.colliderect(ghost.rect):
            return True
        else:
            return False

    def logic(self, map):
        for ghost in map.ghosts:
            if self.check_collision_with_ghost(ghost):
                GAMEOVER = True
        for seed in map.seeds:
            if self.check_collision_with_seed(seed):
                seed.make_effect()
        self.move()
        if self.check_collision_with_walls(map.walls):
            self.move_back()
>>>>>>> 3c80029356aec5b8a65c4d7e6e01336b5d7103c3
