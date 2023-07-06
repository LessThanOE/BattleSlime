import pygame
from setting import *

class Button(pygame.sprite.Sprite):
    def __init__(self, name, x):
        super().__init__()

        self.name = name

        image_path = button_data[name]
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
        self.rect = self.image.get_rect(center = (x, 610))

        pygame.draw.rect(self.image, 'black', (0, 0, self.rect.width, self.rect.height), 3)



