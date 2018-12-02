import pygame as pg
from character import Character
from constants import CHARACTER_SPEED, CHARACTER_HEIGHT, CHARACTER_WIDTH, LEFT,\
    RIGHT, DOWN, UP, PACMAN_RADIUS, YELLOW, BGCOLOR, FPS


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
        self.sprite_matrix = [[none, left1, left2], [none, right1, right2], [none, up1, up2], [none, down1, down2]]
        for i in len(self.sprite_matrix):
            for j in len(self.sprite_matrix[i]):
                self.sprite_matrix[i][j] = pg.transform.scale(self.sprite_matrix[i][j], (wall_size, wall_size))

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
        for i in len(self.death_sprites):
            self.death_sprites[i] = pg.transform.scale(self.death_sprites[i], (wall_size, wall_size))

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
