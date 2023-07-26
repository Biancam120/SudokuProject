import pygame
from sudoku_generator import *

# width = 900
# height = 900  # each square will be 100
# BG_COLOR =
# square_size = 300
# line_width = 5

def main():  # contains code to create different screens of project
	pygame.init()
	pygame.display.set_caption("")
	screen = pygame.display.set_mode((width, height))  # created black pop-up window
	screen.fill(BG_COLOR)  # changes background color
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()  # can close window
				sys.exit()




if __name__ == '__main__':
	main()