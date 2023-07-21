import pygame
import sys
from setting import *
from character import Character
from button import Button
from tower import Tower, HealthBar
from random import randint, choice


class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption("Colorful War")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("Font/monogram-extended.ttf", 48)

        # initial player status
        self.score = 0
        self.level = 0
        self.money = 10
        self.money_color = "black"

        # set character groups
        self.chara = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()

        # set button
        self.button = pygame.sprite.Group()
        self.button_data = ["Slime", "Block", "Maru", "Tobu", "Bomb"]
        for i in range(0, 5):
            self.button.add(Button(self.button_data[i], button_x_pos[i]))

        # set tower
        self.tower = Tower()
        self.healthbar = HealthBar(self.screen)

        # timer
        self.enemy_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.enemy_timer, 1000)

        self.money_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.money_timer, 500)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # generate player character
                    for button in self.button.sprites():
                        if button.rect.collidepoint(pygame.mouse.get_pos()):
                            if self.money >= button.cost:
                                self.money -= button.cost
                                button.rect.centery = 612
                                self.chara.add(
                                    Character(button.name, "player", self.tower)
                                )
                            else:
                                self.money_color = "red"

                if event.type == pygame.MOUSEBUTTONUP:
                    for button in self.button.sprites():
                        button.rect.centery = 610

                if event.type == self.enemy_timer:
                    # generate enemy character
                    enemy_name = enemy_list[randint(0, self.level)]
                    self.enemy.add(Character(enemy_name, "enemy", self.tower))
                    pygame.time.set_timer(
                        self.enemy_timer, randint(1000, (10 - self.level) * 1000)
                    )

                if event.type == self.money_timer:
                    self.money += 1
                    self.money_color = "black"

            # draw background
            self.screen.fill("white")
            pygame.draw.line(
                self.screen, "black", (0, horizon_y), (WIDTH, horizon_y), 3
            )

            self.button.draw(self.screen)
            button_list = self.button.sprites()
            for i in range(0, 5):
                cost_surf = self.font.render(f"{button_list[i].cost}", False, "black")
                cost_rect = cost_surf.get_rect(center=(button_x_pos[i], 675))
                self.screen.blit(cost_surf, cost_rect)

            # tower
            self.tower.draw(self.screen)
            self.tower.update()
            self.healthbar.update(self.tower.health / self.tower.max_health)

            self.enemy.draw(self.screen)
            self.enemy.update(self.chara.sprites(), self)

            self.chara.draw(self.screen)
            self.chara.update(self.enemy.sprites(), self)

            # score system
            self.score = int(pygame.time.get_ticks() / 1000)
            score_surf = self.font.render(f"Score: {self.score}", False, "black")
            score_rect = score_surf.get_rect(center=(900, 50))
            self.screen.blit(score_surf, score_rect)

            # level system
            self.level = int(self.score / 10)
            if self.level >= 8:
                self.level = 8

            # money system
            money_surf = self.font.render(
                f"Money: {self.money}", False, self.money_color
            )
            money_rect = money_surf.get_rect(center=(1100, 50))
            self.screen.blit(money_surf, money_rect)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
