import pygame
from setting import *
from math import sqrt

class Character(pygame.sprite.Sprite):
    def __init__(self, name, type):
        super().__init__()

        self.name = name
        self.type = type

        if type == 'player':
            init_x = 1200
            self.image = pygame.image.load(chara_img[name]['image_player']).convert_alpha()
        else:
            init_x = 0
            self.image = pygame.image.load(chara_img[name]['image_enemy']).convert_alpha()

        if chara_data[name]['flyable']:
            init_y = 400
        else:
            init_y = horizon_y

        self.image = pygame.transform.rotozoom(self.image, 0, 0.3)
        self.rect = self.image.get_rect(midbottom = (init_x, init_y))

        self.health = chara_data[name]['health']
        self.atk = chara_data[name]['atk']
        self.atk_range = chara_data[name]['atk_range']
        self.speed = chara_data[name]['speed']
        self.AOE = chara_data[name]['AOE']

        self.target = None

        self.status = 'moving'


    def move(self):
        # player chara move left, enemy chara move right
        if self.type == 'player':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


    def collide(self, chara_list):
        if self.AOE:
            pass

        else:
            # find the closest character (if in atk_range) and attack
            min_distance = 100000
            for chara in chara_list:
                chara_x = chara.rect.centerx
                chara_y = chara.rect.centery
                distance = int(sqrt((chara_x - self.rect.centerx)**2 + (chara_y - self.rect.centery)**2))

                if distance < min_distance and distance <= self.atk_range:
                    min_distance = distance
                    self.target = chara

            if self.target:
                self.status = 'attacking'
            else:
                self.status = 'moving'


    def attack(self):
        self.target.health -= self.atk
        if self.target.health <= 0:
            self.target = None


    def update(self, chara_list):

        if self.target is  None:
            self.collide(chara_list)

        if self.status == 'moving':
            self.move()

        if self.status == 'attacking':
            self.attack()

        if self.health <= 0:
            self.kill()
