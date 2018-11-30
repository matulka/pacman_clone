import pygame as pg
from character import Character

class Ghost(Character):
    def __init__(self, coordinates, color):
        super().__init__(coordinates)
        self.color = color
        

    def logic(self):
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
