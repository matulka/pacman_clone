import pygame as pg
from time import time
from character import Character
from constants import RIGHT, LEFT, DOWN, UP, BLUE_RELEASE_TIME, RED_RELEASE_TIME, ORANGE_RELEASE_TIME,\
                        PINK_RELEASE_TIME, DEATH_RELEASE_TIME, GSCALING_COEFFICIENT


class Ghost(Character):
    def __init__(self, coordinates, ghost_type, wall_size, teleport_coordinates):
        super().__init__(coordinates, wall_size)
        self.rect.width = self.rect.height = wall_size * GSCALING_COEFFICIENT
        self.teleport_coordinates = teleport_coordinates
        self.alive = True
        self.type = ghost_type  # #blue, red, orange, pink
        self.released = False
        self.is_it_start = True
        self.starting_time = None

        if self.type == 'blue':
            self.time_to_release = BLUE_RELEASE_TIME
        elif self.type == 'red':
            self.time_to_release = RED_RELEASE_TIME
        elif self.type == 'orange':
            self.time_to_release = ORANGE_RELEASE_TIME
        else:
            self.time_to_release = PINK_RELEASE_TIME

        path_part = 'ghost_' + self.type
        left1 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_left1.png')
        left2 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_left2.png')
        right1 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_right1.png')
        right2 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_right2.png')
        down1 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_down1.png')
        down2 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_down2.png')
        up1 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_up1.png')
        up2 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_up2.png')
        self.normal_sprites = [[left1, left2], [right1, right2], [up1, up2], [down1, down2]]
        for i in range(len(self.normal_sprites)):
            for j in range(len(self.normal_sprites[i])):
                self.normal_sprites[i][j] = pg.transform.scale(self.normal_sprites[i][j],\
                                        (int(wall_size * GSCALING_COEFFICIENT), int(wall_size * GSCALING_COEFFICIENT)))
        self.sprite_matrix = self.normal_sprites

        blue1 = pg.image.load('sprites/fear/fear_blue1.png')
        blue2 = pg.image.load('sprites/fear/fear_blue2.png')
        white1 = pg.image.load('sprites/fear/fear_white1.png')
        white2 = pg.image.load('sprites/fear/fear_white2.png')
        self.fear_sprites = [[blue1, blue2, white1, white2], [blue1, blue2, white1, white2],\
                        [blue1, blue2, white1, white2], [blue1, blue2, white1, white2]]
        for i in range(len(self.fear_sprites)):
            for j in range(len(self.fear_sprites[i])):
                self.fear_sprites[i][j] = pg.transform.scale(self.fear_sprites[i][j],\
                                        (int(wall_size * GSCALING_COEFFICIENT), int(wall_size * GSCALING_COEFFICIENT)))

        down = pg.image.load('sprites/eyes/eyes_down.png')
        right = pg.image.load('sprites/eyes/eyes_right.png')
        left = pg.image.load('sprites/eyes/eyes_left.png')
        up = pg.image.load('sprites/eyes/eyes_up.png')
        self.eyes_sprites = [[left], [right], [up], [down]]
        for i in range(len(self.eyes_sprites)):
            for j in range(len(self.eyes_sprites[i])):
                self.eyes_sprites[i][j] = pg.transform.scale(self.eyes_sprites[i][j],\
                                        (int(wall_size * GSCALING_COEFFICIENT), int(wall_size * GSCALING_COEFFICIENT)))

    def change_sprites(self, needed_condition): # # needed_condition = {fear, normal, death}
        self.current_sprite = 0
        if needed_condition == 'normal':
            self.sprite_matrix = self.normal_sprites
        elif needed_condition == 'fear':
            self.sprite_matrix = self.fear_sprites
        elif needed_condition == 'death':
            self.sprite_matrix = self.eyes_sprites

    def get_possible_directions(self, map):
        old_direction = self.direction

        possible_directions = []
        for direction in [LEFT, UP, RIGHT, DOWN]:
            self.direction = direction
            self.move()
            if not self.check_collision_with_walls(map.walls):
                possible_directions.append(direction)
            self.move_back()

        self.direction = old_direction
        return possible_directions

    def logic(self, pacman, game):
        if self.released:
            possible_directions = self.get_possible_directions(game.map)
            gh_x, gh_y = self.rect.x, self.rect.y
            needed_directions = []

            if self.alive:
                vector_x, vector_y = pacman.rect.x - gh_x, pacman.rect.y - gh_y
                if game.fear:
                    vector_x, vector_y = -1 * vector_x, -1 * vector_y
                elif self.sprite_matrix == self.fear_sprites:
                    self.change_sprites('alive')
            else:
                spawn_x, spawn_y = self.teleport_coordinates
                vector_x, vector_y = spawn_x - gh_x, spawn_y - gh_y

            if vector_x > 0:
                needed_directions.append(RIGHT)
            else:
                needed_directions.append(LEFT)
            if vector_y > 0:
                needed_directions.append(DOWN)
            else:
                needed_directions.append(UP)
            directions = [val for val in possible_directions if val in needed_directions]
            if len(directions) > 0:
                self.direction = directions[0]
            else:
                self.direction = possible_directions[0]

            if not self.alive and vector_x == 0 and vector_y == 0:
                self.rect.x, self.rect.y = self.starting_coordinates
                self.released = False
                self.time_to_release = DEATH_RELEASE_TIME
                self.direction = DOWN
                self.change_sprites('normal')

            else:
                self.move()
        else:
            if self.starting_time is None:
                self.starting_time = time()
            else:
                current_time = time()
                time_passed = current_time - self.starting_time
                if time_passed >= self.time_to_release:
                    self.released = True
                    self.time_to_release = 0
                    self.starting_time = None
                    self.rect.x, self.rect.y = self.teleport_coordinates