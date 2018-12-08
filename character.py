import pygame as pg
from constants import CHARACTER_SPEED, LEFT, RIGHT, DOWN, UP, PSCALING_COEFFICIENT


class Character:

    def __init__(self, coordinates, wall_size):
        self.starting_coordinates = coordinates
        self.x, self.y = coordinates
        self.speed = 6 #НУЖНО ДОБАВИТЬ НОРМАЛЬНОЕ ЗНАЧЕНИЕ
        self.direction = -1  # #Направление движения, значения в константах
        self.rect = pg.Rect(coordinates, (PSCALING_COEFFICIENT * wall_size, PSCALING_COEFFICIENT * wall_size))
        self.width = self.rect.width
        self.height = self.rect.height
        self.current_sprite = 0

    def move(self):
        if self.direction == LEFT:
            self.rect = self.rect.move(-1 * self.speed, 0)
        if self.direction == RIGHT:
            self.rect = self.rect.move(self.speed, 0)
        if self.direction == UP:
            self.rect = self.rect.move(0, -1 * self.speed)
        if self.direction == DOWN:
            self.rect = self.rect.move(0, self.speed)

    def move_back(self):
        if self.direction == LEFT:
            self.rect = self.rect.move(self.speed, 0)
        if self.direction == RIGHT:
            self.rect = self.rect.move(-1 * self.speed, 0)
        if self.direction == UP:
            self.rect = self.rect.move(0, self.speed)
        if self.direction == DOWN:
            self.rect = self.rect.move(0, -1 * self.speed)

    def draw(self, screen):
        sprite = self.sprite_matrix[self.direction][self.current_sprite]
        screen.blit(sprite, self.rect)
        self.current_sprite += 1
        self.current_sprite %= len(self.sprite_matrix[self.direction])

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

    def return_coordinates(self):
        return self.rect.x, self.rect.y


