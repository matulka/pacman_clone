import pygame as pg
from character import Character

class Ghost(Character):
    def __init__(self, coordinates, color):
        super().__init__(coordinates)
        self.color = color
        

    def logic(self):
        pass
