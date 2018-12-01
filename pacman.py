import pygame as pg
from character import Character
from constants import CHARACTER_SPEED, CHARACTER_HEIGHT, CHARACTER_WIDTH, LEFT,\
    RIGHT, DOWN, UP, PACMAN_RADIUS, YELLOW, BGCOLOR, FPS


class Pacman(Character):

    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.death_sprites = [] #SHOULD ADD SPRITES

    def check_event(self, event, map):
        if event.type == pg.KEYDOWN:
            cur_direction = self.direction
            if event.key == pg.K_a:
                self.direction = LEFT
            if event.key == pg.K_d:
                self.direction = RIGHT
            if event.key == pg.K_w:
                self.direction = UP
            if event.key == pg.K_s:
                self.direction = DOWN
            if not self.try_move(map):
                self.direction = cur_direction

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

    def logic(self, map, game):
        for ghost in map.ghosts:
            if self.check_collision_with_ghost(ghost):
                self.death_animation(game.screen)
                game.death_counter += 1
                map.refresh() #SHOULD ADD MAP METHOD
        for seed in map.seeds:
            if self.check_collision_with_seed(seed):
                seed.make_effect()
        self.move()
        if self.check_collision_with_walls(map.walls):
            self.move_back()
        if self.x < 0:
            self.x = map.width - self.rect.width
        if self.x + self.rect.width > map.width:
            self.x = 0
        if self.y < 0:
            self.y = map.height - self.rect.height
        if self.y + self.rect.height > map.height:
            self.y = 0

    def death_animation(self, screen):
        for i in range(len(self.death_sprites)):
            sprite = self.death_sprites[i]
            screen.blit(sprite, self.rect)
            pg.time.wait(2000 // FPS)

    def try_move(self, map):
        self.move()
        if self.check_collision_with_walls(map.walls):
            self.move_back()
            return False
        self.move_back()
        return True
