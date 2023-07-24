import pygame
import sys
from setting import *
from character import Character
from button import CharaButton, ImageButton
from tower import Tower, HealthBar
from random import randint, choice


class Game:
    def __init__(self, button_list):
        # general setup
        pygame.init()
        self.status = "stoping"
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption("Colorful War")
        self.clock = pygame.time.Clock()
        self.textfont = pygame.font.Font("Font/monogram-extended.ttf", 48)
        self.captionfont = pygame.font.Font("Font/monogram-extended.ttf", 144)

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
        for i in range(0, 5):
            self.button.add(CharaButton(button_list[i], button_x_pos[i]))

        self.pausebutton = ImageButton("Button/Pause.PNG", 50, 50)

        # set tower
        self.tower = Tower()
        self.healthbar = HealthBar(self.screen)

        # timer
        self.enemy_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.enemy_timer, 1000)

        self.score_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.score_timer, 1000)

        self.money_timer = pygame.USEREVENT + 3
        pygame.time.set_timer(self.money_timer, 500)

    def run(self):
        self.status = "running"

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.status == "running":
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

                    if event.type == self.score_timer:
                        self.score += 1

                    if event.type == self.money_timer:
                        self.money += 1
                        self.money_color = "black"

                elif self.status == "paused":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.status = "running"

                elif self.status == "end":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        return self.score

            if self.status == "running":
                # draw background
                self.screen.fill("white")
                pygame.draw.line(
                    self.screen, "black", (0, horizon_y), (WIDTH, horizon_y), 3
                )

                self.button.draw(self.screen)
                button_list = self.button.sprites()
                for i in range(0, 5):
                    cost_surf = self.textfont.render(
                        f"{button_list[i].cost}", False, "black"
                    )
                    cost_rect = cost_surf.get_rect(center=(button_x_pos[i], 675))
                    self.screen.blit(cost_surf, cost_rect)

                if self.pausebutton.draw(self.screen):
                    self.status = "paused"

                # tower
                self.tower.draw(self.screen)
                self.tower.update()
                self.healthbar.update(self.tower.health / self.tower.max_health)

                if self.tower.health < 0:
                    self.status = "end"

                self.enemy.draw(self.screen)
                self.enemy.update(self.chara.sprites(), self)

                self.chara.draw(self.screen)
                self.chara.update(self.enemy.sprites(), self)

                # score system
                score_surf = self.textfont.render(
                    f"Score: {self.score}", False, "black"
                )
                score_rect = score_surf.get_rect(center=(900, 50))
                self.screen.blit(score_surf, score_rect)

                # level system
                self.level = int(self.score / 10)
                if self.level >= 8:
                    self.level = 8

                # money system
                money_surf = self.textfont.render(
                    f"Money: {self.money}", False, self.money_color
                )
                money_rect = money_surf.get_rect(center=(1100, 50))
                self.screen.blit(money_surf, money_rect)

            elif self.status == "paused":
                pause1_surf = self.captionfont.render("Pause", False, BLUE)
                pause1_rect = pause1_surf.get_rect(center=(640, 250))
                pause2_surf = self.textfont.render(
                    "click and back to game", False, BLUE
                )
                pause2_rect = pause2_surf.get_rect(center=(640, 350))
                self.screen.blit(pause1_surf, pause1_rect)
                self.screen.blit(pause2_surf, pause2_rect)

            elif self.status == "end":
                end1_surf = self.captionfont.render("You Lose", False, "black")
                end1_rect = end1_surf.get_rect(center=(640, 200))
                end2_surf = self.textfont.render(
                    "click and back to menu", False, "black"
                )
                end2_rect = end2_surf.get_rect(center=(640, 300))
                self.screen.blit(end1_surf, end1_rect)
                self.screen.blit(end2_surf, end2_rect)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
