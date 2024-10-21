import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((288, 512))
main_font = pygame.font.SysFont("cambria", 50)

class Button():
	def __init__(self, image, x_pos, y_pos):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			import main1
			exec(open("main1.py").read())

class Button2():
	def __init__(self, image, x_pos, y_pos):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			import main2
			exec(open("main2.py").read())

class Button3():
	def __init__(self, image, x_pos, y_pos):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			pygame.quit()

button_surface = pygame.image.load("1player.png")
button_surface = pygame.transform.scale(button_surface, (149, 41))

button = Button(button_surface, 145, 140)

button_surface2 = pygame.image.load("2player.png")
button_surface2 = pygame.transform.scale(button_surface2, (149, 41))

button2 = Button2(button_surface2, 145, 260)

button_surface3 = pygame.image.load("exitgame.png")
button_surface3 = pygame.transform.scale(button_surface3, (149, 41))

button3 = Button3(button_surface3, 145, 380)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			button.checkForInput(pygame.mouse.get_pos())
			button2.checkForInput(pygame.mouse.get_pos())
			button3.checkForInput(pygame.mouse.get_pos())

	screen.fill('white')

	button.update()
	button2.update()
	button3.update()

	pygame.display.update()