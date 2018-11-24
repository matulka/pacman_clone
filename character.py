
from constants import CHARACTER_SPEED, LEFT, RIGHT, DOWN, UP


class Character:
    sprite_matrix = [[]]

    def __init__(self, coordinates):
        self.x, self.y = coordinates
        self.speed = CHARACTER_SPEED
        self.direction = -1  # #Направление движения, значения в константах
        self.rect = self.sprite_matrix[0][0].get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.current_sprite = 0

    def move(self):
        if self.direction == LEFT:
            self.x -= self.speed
        if self.direction == RIGHT:
            self.x += self.speed
        if self.direction == UP:
            self.y -= self.speed
        if self.direction == DOWN:
            self.y += self.speed

    def move_back(self):
        if self.direction == LEFT:
            self.x += self.speed
        if self.direction == RIGHT:
            self.x -= self.speed
        if self.direction == UP:
            self.y += self.speed
        if self.direction == DOWN:
            self.y -= self.speed

    def draw(self, screen):
        sprite = self.sprite_matrix[self.direction][self.current_sprite]
        screen.blit(sprite, self.rect)
        self.current_sprite += 1
        self.current_sprite %= len(self.sprite_matrix[0])

