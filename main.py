import pygame
import sys
from game import Game
from setting import *
from character import Character
from button import CharaButton, TextButton, CharaButton2
from tower import Tower, HealthBar
from random import randint, choice


class Main:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption("Colorful War")
        self.clock = pygame.time.Clock()
        self.textfont = pygame.font.Font("Font/monogram-extended.ttf", 48)
        self.captionfont = pygame.font.Font("Font/monogram-extended.ttf", 144)

        self.view = "menu"

        # text display settings
        self.caption_surf = self.captionfont.render("Colorful War", False, "black")
        self.caption_rect = self.caption_surf.get_rect(center=(640, 150))

        self.highscore = 0
        self.highscore_surf = self.textfont.render(
            f"High Score: {self.highscore}", False, "black"
        )
        self.highscore_rect = self.highscore_surf.get_rect(center=(640, 300))

        # button settings
        self.startbutton = TextButton("START", 640, 400)
        self.profilebutton = TextButton("PROFILE", 640, 500)

        # player settings
        self.button_list = ("Slime", "Block", "Takai", "Unicorn", "Maru")

        # profile settings
        self.charabutton = {}
        self.charalist = (
            "Slime",
            "Unknown",
            "Unknown",
            "Unknown",
            "Unknown",
            "Unknown",
            "Unknown",
            "Unknown",
            "Unknown",
        )
        for i in range(0, 9):
            print(profile_button_pos[i])
            self.charabutton[i] = CharaButton2(self.charalist[i], i)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("white")
            if self.view == "menu":
                # Menu display
                pygame.draw.line(
                    self.screen,
                    "gray",
                    (0, horizon_y + 100),
                    (WIDTH, horizon_y + 100),
                    3,
                )
                self.screen.blit(self.highscore_surf, self.highscore_rect)
                self.screen.blit(self.caption_surf, self.caption_rect)

                if self.startbutton.draw(self.screen):
                    game = Game(self.button_list)
                    gamescore = game.run()
                    if gamescore > self.highscore:
                        self.highscore = gamescore
                    self.highscore_surf = self.textfont.render(
                        f"High Score: {self.highscore}", False, "black"
                    )
                    self.highscore_rect = self.highscore_surf.get_rect(
                        center=(640, 300)
                    )

                if self.profilebutton.draw(self.screen):
                    self.view = "profile"

            elif self.view == "profile":
                for i in range(0, 9):
                    self.charabutton[i].draw(self.screen)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    main = Main()
    main.run()
