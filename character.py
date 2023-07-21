import pygame
from setting import *
from math import sqrt


class Character(pygame.sprite.Sprite):
    def __init__(self, name, type, tower):
        super().__init__()

        self.name = name
        self.type = type

        if type == "player":
            init_x = 1150
            self.image = pygame.image.load(
                chara_img[name]["image_player"]
            ).convert_alpha()
        else:
            init_x = -20
            self.image = pygame.image.load(
                chara_img[name]["image_enemy"]
            ).convert_alpha()

        if chara_data[name]["flyable"]:
            init_y = 400
        else:
            init_y = horizon_y

        self.image = pygame.transform.rotozoom(self.image, 0, 0.3)
        self.rect = self.image.get_rect(midbottom=(init_x, init_y))

        self.cost = chara_data[name]["cost"]
        self.add_money = chara_data[name]["add_money"]
        self.health = chara_data[name]["health"]
        self.speed = chara_data[name]["speed"]

        self.atk = chara_data[name]["atk"]
        self.atk_range = chara_data[name]["atk_range"]
        self.knock_distance = chara_data[name]["knock_distance"]

        self.last_atk_time = 0
        self.cooldown = 700
        self.can_attack = True

        self.target = []
        self.tower = tower

        self.status = "moving"

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_atk_time > self.cooldown:
            self.can_attack = True
        else:
            self.can_attack = False

    def move(self):
        # player chara move left, enemy chara move right
        if self.type == "player":
            self.rect.x -= self.speed
            if self.rect.centerx < left_border:
                self.rect.centerx = left_border
        else:
            self.rect.x += self.speed
            if self.rect.centerx > right_border:
                self.rect.centerx = right_border

    def get_status(self, chara_list):
        # get character status and get target list
        if self.type == "enemy" and pygame.sprite.collide_rect(self, self.tower):
            self.target.clear()
            self.target.append(self.tower)

        else:
            if self.name == "Bomb":
                # explode once collide with enemy
                for chara in chara_list:
                    chara_x = chara.rect.centerx
                    chara_y = chara.rect.centery
                    distance = int(
                        sqrt(
                            (chara_x - self.rect.centerx) ** 2
                            + (chara_y - self.rect.centery) ** 2
                        )
                    )

                    if distance <= self.atk_range:
                        self.target.append(chara)

            elif self.name == "Unicorn":
                # attak all character no matter distance
                self.target = chara_list

            else:
                if not self.target:
                    # if current has no target
                    # find the closest character (if in atk_range) and attack
                    min_distance = 100000
                    for chara in chara_list:
                        chara_x = chara.rect.centerx
                        chara_y = chara.rect.centery
                        distance = int(
                            sqrt(
                                (chara_x - self.rect.centerx) ** 2
                                + (chara_y - self.rect.centery) ** 2
                            )
                        )

                        if distance < min_distance and distance <= self.atk_range:
                            min_distance = distance
                            if self.target:
                                self.target.clear()
                            self.target.append(chara)

        if self.target:
            self.status = "attacking"
        else:
            self.status = "moving"

    def attack(self):
        self.last_atk_time = pygame.time.get_ticks()
        for chara in self.target:
            if chara == self.tower:
                # tower being attack
                self.tower.health -= self.atk
                self.tower.rect.x += 5

            else:
                chara.health -= self.atk

                if chara.type == "player":
                    chara.rect.x += self.knock_distance
                    if chara.rect.centerx < left_border:
                        self.rect.centerx = left_border
                else:
                    chara.rect.x -= self.knock_distance
                    if chara.rect.centerx > right_border:
                        self.rect.centerx = right_border

            self.target.remove(chara)

        if self.name == "Bomb":
            self.health = 0

    def update(self, chara_list, player):
        self.get_status(chara_list)

        if self.status == "moving":
            self.move()
        elif self.status == "attacking":
            self.cooldowns()
            if self.can_attack:
                self.attack()

        if self.health <= 0:
            if self.type == "enemy":
                player.money += self.add_money
            self.kill()
