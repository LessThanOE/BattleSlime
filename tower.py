import pygame
from setting import *


class Tower:
    def __init__(self, screen):
        self.pygame = pygame
        self.canvas = screen

        self.width = 100
        self.height = 300
        self.x = 1100
        self.y = horizon_y - self.height
        self.health = 1000

        self.rect = self.pygame.draw.rect(
            self.canvas, "black", (self.x, self.y, self.width, self.height), 3
        )

    def update(self):
        self.rect = self.pygame.draw.rect(
            self.canvas, "black", (self.x, self.y, self.width, self.height), 3
        )
        print(self.health)
