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

        self.target = []

        self.status = 'moving'


    def move(self):
        print(self.name + ':move')
        # player chara move left, enemy chara move right
        if self.type == 'player':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


    def collide(self, chara_list):
        print(self.name + ':collide')
        if self.AOE:
            if self.name == 'Bomb':
                # explode once collide with enemy
                for chara in chara_list:
                    chara_x = chara.rect.centerx
                    chara_y = chara.rect.centery
                    distance = int(sqrt((chara_x - self.rect.centerx)**2 + (chara_y - self.rect.centery)**2))

                    if distance <= self.atk_range:
                        chara.health -= self.atk

                self.kill()

        else:
            if not self.target:
                # if not AOE and no target
                # find the closest character (if in atk_range) and attack
                min_distance = 100000
                for chara in chara_list:
                    chara_x = chara.rect.centerx
                    chara_y = chara.rect.centery
                    distance = int(sqrt((chara_x - self.rect.centerx)**2 + (chara_y - self.rect.centery)**2))

                    if distance < min_distance and distance <= self.atk_range:
                        min_distance = distance
                        if self.target: self.target.clear()
                        self.target.append(chara)

                if self.target:
                    self.status = 'attacking'
                else:
                    self.status = 'moving'


    def attack(self):
        print(self.name + ':attack')
        for chara in self.target:
            chara.health -= self.atk

            #if chara.type == 'player': chara.rect.x += 1
            #else: chara.rect.x -= 1

            if chara.health <= 0:
                self.target.remove(chara)


    def update(self, chara_list):

        self.collide(chara_list)

        if self.status == 'moving':
            self.move()

        if self.status == 'attacking':
            self.attack()

        if self.health <= 0:
            self.kill()
