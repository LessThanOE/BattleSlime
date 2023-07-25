import pygame
from setting import *


class CharaButton(pygame.sprite.Sprite):
    def __init__(self, name, x):
        super().__init__()

        self.name = name
        if name != "Unknown":
            self.cost = chara_data[name]["cost"]
        self.x = x

        image_path = button_data[name]
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
        self.rect = self.image.get_rect(center=(self.x, 610))

        pygame.draw.rect(
            self.image, "black", (0, 0, self.rect.width, self.rect.height), 3
        )


class TeamButton:
    def __init__(self, unlock, id):
        self.unlock = unlock
        self.select = False
        self.clicked = False

        self.color = "black"
        self.name = chara_list[id]
        self.id = id

        if self.unlock:
            image_path = button_data[self.name]
        else:
            image_path = button_data["Unknown"]

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
        self.rect = self.image.get_rect(center=(Team_button_pos[self.id]))

    def Unlock(self):
        self.unlock = True
        self.image = pygame.image.load(button_data[self.name]).convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
        self.rect = self.image.get_rect(center=(Team_button_pos[self.id]))
        return self.unlock

    def update(self, canvas, is_full):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if self.unlock:
                if is_full and self.select == False:
                    error_message = pygame.font.Font(
                        "Font/monogram-extended.ttf", 64
                    ).render("Team is Fulled", False, RED)
                    error_message_rect = error_message.get_rect(center=(640, 100))
                    canvas.blit(error_message, error_message_rect)
                    self.color = RED
                else:
                    self.color = BLUE
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        self.clicked = True
                        if self.select:
                            self.select = False
                        else:
                            self.select = True
            else:
                error_message = pygame.font.Font(
                    "Font/monogram-extended.ttf", 64
                ).render("Not Unlocked", False, RED)
                error_message_rect = error_message.get_rect(center=(640, 100))
                canvas.blit(error_message, error_message_rect)
                self.color = RED
        else:
            self.color = BLACK

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        if self.select:
            self.color = GREEN

        # draw button
        canvas.blit(self.image, self.rect)
        pygame.draw.rect(
            self.image, self.color, (0, 0, self.rect.width, self.rect.height), 3
        )

        return self.select


class ImageButton:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
        self.rect = self.image.get_rect(center=(x, y))
        self.clicked = False

    def draw(self, canvas):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button
        canvas.blit(self.image, self.rect)

        return action


class TextButton:
    def __init__(self, text, x, y):
        self.font = pygame.font.Font("Font/monogram-extended.ttf", 64)
        self.color = "white"
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
            self.color = "white"

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button
        canvas.blit(self.text, self.textrect)
        pygame.draw.rect(canvas, self.color, self.rect, 3, 3)

        return action
