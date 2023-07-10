import pygame, sys
from setting import *
from character import Character
from button import Button
from random import randint, choice


class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('BattleSlime')
		self.clock = pygame.time.Clock()
		self.font = pygame.font.Font('Python/BattleSlime/Font/monogram-extended.ttf', 48)

		self.score = 0
		self.level = 0

		# set character groups
		self.chara = pygame.sprite.Group()
		self.enemy = pygame.sprite.Group()

		# set button
		self.button = pygame.sprite.Group()
		self.button_data = ['Slime', 'Block', 'Maru', 'Tobu', 'Bomb']
		for i in range(0,5):
			self.button.add(Button(self.button_data[i], button_x_pos[i]))

		# timer
		self.enemy_timer = pygame.USEREVENT + 1
		pygame.time.set_timer(self.enemy_timer, 1000)

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
							button.rect.centery = 612
							self.chara.add(Character(button.name, 'player'))
				if event.type == pygame.MOUSEBUTTONUP:
					for button in self.button.sprites():
						button.rect.centery = 610

				if event.type == self.enemy_timer:
					# generate enemy character
					enemy_name = enemy_list[randint(0, self.level)]
					self.enemy.add(Character(enemy_name, 'enemy'))
					pygame.time.set_timer(self.enemy_timer, randint(1000, (10-self.level)*1000))

			# draw background
			self.screen.fill('white')
			pygame.draw.line(self.screen, 'black', (0, 500), (WIDTH, 500), 3)

			self.button.draw(self.screen)

			self.enemy.draw(self.screen)
			self.enemy.update(self.chara.sprites())

			self.chara.draw(self.screen)
			self.chara.update(self.enemy.sprites())


			# score system
			self.score = int(pygame.time.get_ticks() / 1000)
			score_surf = self.font.render(f'Score: {self.score}', False, 'black')
			score_rect = score_surf.get_rect(center = (1000,50))
			self.screen.blit(score_surf,score_rect)

			# level system
			self.level = int(self.score / 10)
			if self.level >= 8:
				self.level = 8

			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()

