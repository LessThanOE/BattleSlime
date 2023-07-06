import pygame, sys
from setting import *
from character import Character
from button import Button


class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('BattleField')
		self.clock = pygame.time.Clock()
		
		self.player_chara = pygame.sprite.Group()
		
		self.button = pygame.sprite.Group()
		self.button_data = ['Slime', 'Block', 'Maru', 'Unicorn', 'Takai']
		for i in range(0,5):
			self.button.add(Button(self.button_data[i], button_x_pos[i]))
	
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
					
				if event.type == pygame.MOUSEBUTTONDOWN:
					# check if button has been pressed
					for button in self.button.sprites():
						if button.rect.collidepoint(pygame.mouse.get_pos()):
							button.rect.centery = 612
							self.player_chara.add(Character(button.name, 1200, 500))
				else:
					for button in self.button.sprites():
						button.rect.centery = 610

			self.screen.fill('white')
			pygame.draw.line(self.screen, 'black', (0, 500), (WIDTH, 500), 3)
			
			self.button.draw(self.screen)
			
			self.player_chara.draw(self.screen)
			self.player_chara.update()

			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()

