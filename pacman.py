import pygame as pg
from character import Character
from constants import LEFT, RIGHT, DOWN, UP, FPS, GHOST_POINTS, SPACE_BLOCKS, BGCOLOR, EYES_SPEED
from math import fabs


class Pacman(Character):

    def __init__(self, coordinates, wall_size):
        super().__init__(coordinates, wall_size)
        none = pg.image.load('sprites/pacman/pacman0.png')
        left1 = pg.image.load('sprites/pacman/pacman_left1.png')
        left2 = pg.image.load('sprites/pacman/pacman_left2.png')
        right1 = pg.image.load('sprites/pacman/pacman_right1.png')
        right2 = pg.image.load('sprites/pacman/pacman_right2.png')
        down1 = pg.image.load('sprites/pacman/pacman_down1.png')
        down2 = pg.image.load('sprites/pacman/pacman_down2.png')
        up1 = pg.image.load('sprites/pacman/pacman_up1.png')
        up2 = pg.image.load('sprites/pacman/pacman_up2.png')
        self.sprite_matrix = [[none, left1, left2, left1, none], [none, right1, right2, right1, none],\
                              [none, up1, up2, up1, none], [none, down1, down2, down1, none]]
        for i in range(len(self.sprite_matrix)):
            for j in range(len(self.sprite_matrix[i])):
                self.sprite_matrix[i][j] = pg.transform.scale(self.sprite_matrix[i][j],\
                                            (int(wall_size + SPACE_BLOCKS * 2), int(wall_size + SPACE_BLOCKS * 2)))
        self.rect.width = self.rect.height = wall_size + SPACE_BLOCKS * 2
        death1 = pg.image.load('sprites/death/death1.png')
        death2 = pg.image.load('sprites/death/death2.png')
        death3 = pg.image.load('sprites/death/death3.png')
        death4 = pg.image.load('sprites/death/death4.png')
        death5 = pg.image.load('sprites/death/death5.png')
        death6 = pg.image.load('sprites/death/death6.png')
        death7 = pg.image.load('sprites/death/death7.png')
        death8 = pg.image.load('sprites/death/death8.png')
        death9 = pg.image.load('sprites/death/death9.png')
        death10 = pg.image.load('sprites/death/death10.png')
        death11 = pg.image.load('sprites/death/death11.png')
        self.death_sprites = [death1, death2, death3, death4, death5, death6, death7, death8, death9, death10, death11]
        for i in range(len(self.death_sprites)):
            self.death_sprites[i] = pg.transform.scale(self.death_sprites[i],\
                                            (int(wall_size + SPACE_BLOCKS * 2), int(wall_size + SPACE_BLOCKS * 2)))
        self.try_change_direction = -1
        self.not_dead = True

    def check_event(self, event, map):
        if event.type == pg.KEYDOWN:
            cur_direction = self.direction
            if event.key == pg.K_a:
                self.direction = LEFT
                self.try_change_direction = LEFT
            if event.key == pg.K_d:
                self.direction = RIGHT
                self.try_change_direction = RIGHT
            if event.key == pg.K_w:
                self.direction = UP
                self.try_change_direction = UP
            if event.key == pg.K_s:
                self.direction = DOWN
                self.try_change_direction = DOWN
            if not self.try_move(map):
                self.direction = cur_direction

    def logic(self, map, game):
        print(self.not_dead)
        for ghost in map.ghosts: # #possible problem that GHOST is passed not by reference
            if self.check_collision_with_ghost(ghost):
                if ghost.alive:
                    if (not game.fear or ghost.already_died) and self.not_dead:
                        self.not_dead = False
                        self.death_animation(game)
                        game.death_counter += 1
                        game.refresh()
                    else:
                        ghost.alive = False
                        game.point_counter += GHOST_POINTS
                        ghost.change_sprites('death')
                        ghost.speed = EYES_SPEED

        for seed in map.seeds:
            if self.check_collision_with_seed(seed):
                seed.make_effect(game)
        self.change_direction(map)
        self.move()
        if self.check_collision_with_walls(map.walls):
            self.move_back()
        self.teleport(map)

    def teleport(self, map):
        if self.rect.x < 0 and self.direction != RIGHT:
            self.rect.x = map.blocks_width - SPACE_BLOCKS
        if self.rect.x + self.rect.width > int(fabs(map.width)) and self.direction != LEFT:
            self.rect.x = -SPACE_BLOCKS
        if self.rect.y < map.top:
            self.rect.y = map.top + int(fabs(map.height)) - self.rect.height
        if self.rect.y + self.rect.height > int(fabs(map.height)) + map.top:
            self.rect.y = map.top

    def death_animation(self, game):
        for i in range(len(self.death_sprites)):
            sprite = self.death_sprites[i]
            game.screen.fill(BGCOLOR)
            game.screen.blit(sprite, self.rect)
            pg.time.wait(2000 // FPS)
            pg.display.flip()

    def try_move(self, map):
        self.move()
        if self.check_collision_with_walls(map.walls):
            self.move_back()
            return False
        self.move_back()
        return True

    def change_direction(self, map):
        if self.try_change_direction != -1:
            cur_direction = self.direction
            self.direction = self.try_change_direction
            if not self.try_move(map):
                self.direction = cur_direction
            else:
                self.try_change_direction = -1
