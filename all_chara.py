import pygame
from setting import *
from character import Character

class Slime(Character):
    def __init__(self, type):
        super().__init__(type)

        self.health = 100
        self.atk = 100