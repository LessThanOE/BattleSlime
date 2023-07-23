import pygame
from setting import *


class Button(pygame.sprite.Sprite):
    def __init__(self, name, x):
        super().__init__()

        self.name = name
        self.cost = chara_data[name]["cost"]
        self.x = x

        image_path = button_data[name]
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
        self.rect = self.image.get_rect(center=(self.x, 610))

        pygame.draw.rect(
            self.image, "black", (0, 0, self.rect.width, self.rect.height), 3
        )


class TextButton:
    def __init__(self, text, x, y):
        self.font = pygame.font.Font("Font/monogram-extended.ttf", 64)
        self.color = "black"
        self.text = self.font.render(f"{text}", False, "black")
        self.textrect = self.text.get_rect(center=(x, y))

        self.rect = pygame.Rect(
            0, 0, self.textrect.width + 40, self.textrect.height + 20
        )
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self, canvas):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            self.color = BLUE
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        else:
            self.color = "black"

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button
        canvas.blit(self.text, self.textrect)
        pygame.draw.rect(canvas, self.color, self.rect, 3, 3)

        return action
