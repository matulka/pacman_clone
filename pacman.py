import pygame
from math import radians
from character import Character
from constants import CHARACTER_SPEED, CHARACTER_HEIGHT, CHARACTER_WIDTH, LEFT,\
    RIGHT, DOWN, UP, PACMAN_RADIUS, YELLOW, BGCOLOR

class Pacman(Character):
    color = YELLOW

    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.radius = PACMAN_RADIUS
        self.mouth_closed = True #SHOULD REWORK

    def draw(self, screen):
        if self.mouth_closed:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        else:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
            if self.direction == RIGHT:
                pygame.draw.arc(screen, BGCOLOR,
                            (self.x - self.width / 2, self.y - self.height / 2,
                             self.width, self.height),
                            radians(-45), radians(45),
                            self.radius)
            if self.direction == UP:
                pygame.draw.arc(screen, BGCOLOR,
                                (self.x - self.width / 2, self.y - self.height / 2,
                                 self.width, self.height),
                                radians(45), radians(135),
                                self.radius)
            if self.direction == DOWN:
                pygame.draw.arc(screen, BGCOLOR,
                                (self.x - self.width / 2, self.y - self.height / 2,
                                 self.width, self.height),
                                radians(225), radians(315),
                                self.radius)
            if self.direction == LEFT:
                pygame.draw.arc(screen, BGCOLOR,
                                (self.x - self.width / 2, self.y - self.height / 2,
                                 self.width, self.height),
                                radians(135), radians(225),
                                self.radius)


    def check_event(self, event):
        #Should check collisions with map
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.direction = LEFT
            if event.key == pygame.K_d:
                self.direction = RIGHT
            if event.key == pygame.K_w:
                self.direction = UP
            if event.key == pygame.K_s:
                self.direction = DOWN

    def check_collision_with_map(self, map):
        pass

    def check_collision_with_seed(self, seed):
        pass

    def check_collision_with_ghost(self, ghost):
        pass

    def logic(self, map, seeds, ghosts):
        for ghost in ghosts:
            if self.check_collision_with_ghost(ghost):
                pass
        for seed in seeds:
            if self.check_collision_with_ghost(seed):
                pass
                #seed.make_effect()
        if self.check_collision_with_map(map):
            pass
        else:
            self.move()
            self.mouth_closed = not self.mouth_closed #REWORK
