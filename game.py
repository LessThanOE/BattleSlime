import pygame
import sys
from setting import *
from character import Character
from button import CharaButton, ImageButton, TextButton
from tower import Tower, HealthBar
from random import randint, choice


class Game:
    def __init__(self, button_list):
        # general setup
        pygame.init()
        self.status = "stoping"
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption(GAME_NAME)
        self.clock = pygame.time.Clock()
        self.textfont = pygame.font.Font("Font/monogram-extended.ttf", 48)
        self.captionfont = pygame.font.Font("Font/monogram-extended.ttf", 144)

        # music
        pygame.mixer.init()
        self.runbgm = False
        self.shopbgm = False

        self.button_sound = pygame.mixer.Sound("click-button.mp3")
        pygame.mixer.music.set_volume(1)

        # initial player status
        self.score = 0
        self.level = 0
        self.money = 10
        self.money_color = BLACK

        # set character groups
        self.chara = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.enemy_list = ["Slime"]

        # set button
        self.button = pygame.sprite.Group()
        for i in range(0, 5):
            self.button.add(CharaButton(button_list[i], button_x_pos[i]))

        self.pausebutton = ImageButton("Button/Pause.PNG", 50, 50, 0.2)

        self.shopbutton = TextButton("Shop", 250, 50)
        self.towerup = ImageButton("Button/tower_health_up.PNG", 300, 275, 0.4)
        self.enemydown = ImageButton("Button/enemy_health_down.PNG", 550, 275, 0.4)
        self.enemydown_effect = False
        self.effect_time = 0
        self.moneyup = ImageButton("Button/money_up.PNG", 800, 275, 0.4)
        self.shopkeeper = ImageButton("Entity/shopkeeper.jpg", 1100, 350, 1)
        self.speak_time = 0

        # set tower
        self.tower = Tower()
        self.healthbar = HealthBar(self.screen)

        # timer
        self.enemy_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.enemy_timer, 1000)
        self.enemy_cooldown_bound = 8000

        self.score_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.score_timer, 1000)

        self.money_timer = pygame.USEREVENT + 3
        self.money_spd = 700
        pygame.time.set_timer(self.money_timer, self.money_spd)

    def run(self):
        self.status = "running"

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.status == "running":
                    # generate player character
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for button in self.button.sprites():
                            if (
                                button.rect.collidepoint(pygame.mouse.get_pos())
                                and button.name != "Unknown"
                            ):
                                if self.money >= button.cost:
                                    self.button_sound.play()
                                    self.money -= button.cost
                                    button.rect.centery = 612
                                    self.chara.add(
                                        Character(button.name, "player", self.tower)
                                    )
                                else:
                                    self.money_color = RED

                    # button animated
                    if event.type == pygame.MOUSEBUTTONUP:
                        for button in self.button.sprites():
                            button.rect.centery = 610

                    # generate enemy character
                    if event.type == self.enemy_timer:
                        enemy_name = choice(self.enemy_list)
                        self.enemy.add(Character(enemy_name, "enemy", self.tower))
                        pygame.time.set_timer(
                            self.enemy_timer, randint(1000, self.enemy_cooldown_bound)
                        )

                    # score count
                    if event.type == self.score_timer:
                        self.score += 1

                    # money count
                    if event.type == self.money_timer:
                        self.money += 1
                        self.money_color = BLACK

                elif self.status == "shopping":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.button_sound.play()
                            self.status = "running"

                elif self.status == "paused":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.status = "running"
                            self.button_sound.play()
                        elif event.button == 3:
                            self.button_sound.play()
                            return self.score

                elif self.status == "end":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.button_sound.play()
                        return self.score

            if self.status == "running":
                if self.runbgm == False:
                    self.runbgm = True
                    self.shopbgm = False
                    pygame.mixer.init()
                    pygame.mixer.music.load("BGM1.mp3")
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.unpause()

                # background
                self.screen.fill("white")
                pygame.draw.line(
                    self.screen, BLACK, (0, horizon_y), (WIDTH, horizon_y), 3
                )

                # buttons
                self.button.draw(self.screen)
                button_list = self.button.sprites()
                for i in range(0, 5):
                    if button_list[i].name != "Unknown":
                        cost_surf = self.textfont.render(
                            f"{button_list[i].cost}", False, BLACK
                        )
                        cost_rect = cost_surf.get_rect(center=(button_x_pos[i], 675))
                        self.screen.blit(cost_surf, cost_rect)

                if self.pausebutton.draw(self.screen):
                    self.button_sound.play()
                    self.status = "paused"

                if self.shopbutton.draw(self.screen):
                    self.button_sound.play()
                    self.status = "shopping"

                # tower
                self.tower.draw(self.screen)
                self.tower.update()
                self.healthbar.update(self.tower.health / self.tower.max_health)

                if self.tower.health < 0:
                    self.status = "end"

                # enemy and player chara
                self.enemy.draw(self.screen)
                self.enemy.update(self.chara.sprites(), self)

                self.chara.draw(self.screen)
                self.chara.update(self.enemy.sprites(), self)

                if pygame.time.get_ticks() - self.effect_time >= 10000:
                    self.enemydown_effect = False

                if self.enemydown_effect:
                    effect_surf = self.textfont.render("enemy atk down", False, BLACK)
                    effect_rect = effect_surf.get_rect(center=(640, 300))
                    self.screen.blit(effect_surf, effect_rect)
                    for x in self.enemy:
                        x.atk = x.atk - 3
                else:
                    for x in self.enemy:
                        x.atk = x.oatk

                # score
                score_surf = self.textfont.render(f"Score: {self.score}", False, BLACK)
                score_rect = score_surf.get_rect(center=(900, 50))
                self.screen.blit(score_surf, score_rect)

                # level
                if self.score % 30 == 0:
                    self.level = int(self.score / 30)
                    if self.level % 2 == 0:
                        self.enemy_cooldown_bound = 8000
                        if self.level <= 16:
                            self.enemy_list.append(chara_list[int(self.level / 2)])
                        else:
                            self.enemy_list.append(chara_list[randint(0, 8)])

                    else:
                        self.enemy_cooldown_bound = 4000

                # money
                money_surf = self.textfont.render(
                    f"Money: {self.money}", False, self.money_color
                )
                money_rect = money_surf.get_rect(center=(1100, 50))
                self.screen.blit(money_surf, money_rect)

            elif self.status == "shopping":
                if self.shopbgm == False:
                    self.shopbgm = True
                    self.runbgm = False
                    pygame.mixer.init()
                    pygame.mixer.music.load("Elevator-Music.mp3")
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.unpause()

                self.screen.fill("white")

                pause1_surf = self.captionfont.render("Shop", False, BLUE)
                pause1_rect = pause1_surf.get_rect(center=(640, 100))
                pause2_surf = self.textfont.render("ESC to leave shop", False, BLACK)
                pause2_rect = pause2_surf.get_rect(center=(640, 450))
                self.screen.blit(pause1_surf, pause1_rect)
                self.screen.blit(pause2_surf, pause2_rect)

                if self.towerup.draw(self.screen):
                    self.towerup.rect.y += 5
                    if self.money >= 20:
                        self.tower.health += 10
                        self.money -= 20
                else:
                    self.towerup.rect.centery = 275

                if self.enemydown.draw(self.screen) and self.enemydown_effect == False:
                    self.enemydown.rect.y += 5
                    if self.money >= 100:
                        self.effect_time = pygame.time.get_ticks()
                        self.enemydown_effect = True
                        self.money -= 100
                else:
                    self.enemydown.rect.centery = 275

                # money up
                if self.moneyup.draw(self.screen):
                    self.moneyup.rect.y += 5
                    if self.money >= 500:
                        self.money_spd -= 200
                        pygame.time.set_timer(self.money_timer, self.money_spd)
                        self.money -= 500
                else:
                    self.moneyup.rect.centery = 275

                # shopkeeper speak
                if self.shopkeeper.draw(self.screen):
                    self.speak_time = pygame.time.get_ticks()
                    speak = "Give me your money, you idiot!!"

                if pygame.time.get_ticks() - self.speak_time >= 1000:
                    speak = ""

                speak_surf = self.textfont.render(f"{speak}", False, RED)
                speak_rect = speak_surf.get_rect(center=(700, 550))
                self.screen.blit(speak_surf, speak_rect)

                self.healthbar.update(self.tower.health / self.tower.max_health)

                # money display
                money_surf = self.textfont.render(
                    f"Money: {self.money}", False, self.money_color
                )
                money_rect = money_surf.get_rect(center=(1100, 50))
                self.screen.blit(money_surf, money_rect)

            elif self.status == "paused":
                pygame.mixer.music.pause()

                pause1_surf = self.captionfont.render("Pause", False, BLUE)
                pause1_rect = pause1_surf.get_rect(center=(640, 200))
                pause2_surf = self.textfont.render("LEFT CLICK  continue", False, BLACK)
                pause2_rect = pause2_surf.get_rect(center=(640, 300))
                pause3_surf = self.textfont.render(
                    "RIGHT CLICK  back to menu", False, BLACK
                )
                pause3_rect = pause3_surf.get_rect(center=(640, 350))
                self.screen.blit(pause1_surf, pause1_rect)
                self.screen.blit(pause2_surf, pause2_rect)
                self.screen.blit(pause3_surf, pause3_rect)

            elif self.status == "end":
                end1_surf = self.captionfont.render("You Lose", False, RED)
                end1_rect = end1_surf.get_rect(center=(640, 200))
                end2_surf = self.textfont.render("CLICK  back to menu", False, BLACK)
                end2_rect = end2_surf.get_rect(center=(640, 300))
                self.screen.blit(end1_surf, end1_rect)
                self.screen.blit(end2_surf, end2_rect)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
