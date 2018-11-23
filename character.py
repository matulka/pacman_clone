import pygame as pg
from constants import CHARACTER_SPEED, CHARACTER_HEIGHT, CHARACTER_WIDTH, LEFT, RIGHT, DOWN, UP

class Character:
    def __init__(self, coordinates):
        self.x, self.y = coordinates
        self.speed = CHARACTER_SPEED
        self.width = CHARACTER_WIDTH
        self.height = CHARACTER_HEIGHT
        self.direction = -1 #Направление движения, значения в константах

    def move(self):
        if (self.direction == LEFT):
            self.x -= self.speed
        if (self.direction == RIGHT):
            self.x += self.speed
        if (self.direction == UP):
            self.y -= self.speed
        if (self.direction == DOWN):
            self.y += self.speed


