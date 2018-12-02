import pygame as pg
from character import Character
from constants import RIGHT, LEFT, DOWN, UP


class Ghost(Character):
    def __init__(self, coordinates, ghost_type, wall_size):
        super().__init__(coordinates, wall_size)
        self.type = ghost_type  # #blue, red, orange, pink
        path_part = 'ghost_' + self.type
        left1 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_left1.png')
        left2 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_left2.png')
        right1 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_right1.png')
        right2 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_right2.png')
        down1 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_down1.png')
        down2 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_down2.png')
        up1 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_up1.png')
        up2 = pg.image.load('sprites/ghost/' + self.type + '/' + path_part + '_up2.png')
        self.sprite_matrix = [[left1, left2], [right1, right2], [up1, up2], [down1, down2]]
        for i in range(len(self.sprite_matrix)):
            for j in range(len(self.sprite_matrix[i])):
                self.sprite_matrix[i][j] = pg.transform.scale(self.sprite_matrix[i][j], (int(wall_size*1.5),
                                                                                         int(wall_size*1.5)))

        blue1 = pg.image.load('sprites/fear/fear_blue1.png')
        blue2 = pg.image.load('sprites/fear/fear_blue2.png')
        white1 = pg.image.load('sprites/fear/fear_white1.png')
        white2 = pg.image.load('sprites/fear/fear_white2.png')
        self.fear_sprites = [blue1, blue2, white1, white2]
        for i in range(len(self.fear_sprites)):
            self.fear_sprites[i] = pg.transform.scale(self.fear_sprites[i], (int(wall_size*1.5),
                                                                             int(wall_size*1.5)))

        down = pg.image.load('sprites/eyes/eyes_down.png')
        right = pg.image.load('sprites/eyes/eyes_right.png')
        left = pg.image.load('sprites/eyes/eyes_left.png')
        up = pg.image.load('sprites/eyes/eyes_up.png')
        self.eyes_sprites = [left, right, up, down]
        for i in range(len(self.eyes_sprites)):
            self.eyes_sprites[i] = pg.transform.scale(self.eyes_sprites[i], (int(wall_size*1.5),
                                                                             int(wall_size*1.5)))

    def logic(self, pacman):
        possible_directions = map.check_directions(self.coordinates)  # #этот метод вернет возможные направления
        pac_x, pac_y = pacman.coordinates
        gh_x, gh_y = self.coordinates
        needed_directions = []
        vector_x, vector_y = pac_x - gh_x, pac_y - gh_y
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
