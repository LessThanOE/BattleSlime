import pygame
from setting import *

class Character(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        super().__init__()

        self.name = name
        self.health = chara_data[name]['health']
        self.max_health = chara_data[name]['max_health']
        self.atk = chara_data[name]['atk']
        self.speed = chara_data[name]['speed']

        image_path = chara_data[name]['image']
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.3)

        self.rect = self.image.get_rect(midbottom = (x, y))

        self.status = 'moving'

    def move(self):
        # move left
        self.rect.x -= self.speed

    def collide(self, hit_group):
        self.hit_list = pygame.sprite.spritecollide(self, hit_group, False)
        if self.hit_list:
            self.status = 'attacking'
        else:
            self.status = 'moving'

    def attack(self):
        for sprite in self.hit_list:
            sprite.health -= self.atk

    def death(self):
        if self.health <= 0:
            self.kill()

    def update(self, hit_group):
        self.collide(hit_group)

        if self.status == 'moving':
            self.move()

        if self.status == 'attacking':
            self.attack()
            self.death()
