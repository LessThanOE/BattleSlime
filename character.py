import pygame
from setting import *

class Character(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        super().__init__()

        self.health = 1
        self.max_health = 1
        self.atk = 1
        self.speed = 1

        image_path = chara_data[name]['image'] 
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.3)
        
        self.rect = self.image.get_rect(midbottom = (x, y))

    def move(self):
        self.rect.x -= self.speed
    
    def collide(self, x, y):
        # return if position collide with character
        return False

    def attack(self):
        # character attack
        pass

    def hit(self):
        # character being hit
        pass

    def update(self):
        self.move()
