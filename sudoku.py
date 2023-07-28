import pygame
from sudoku_generator import *
import pygame

pygame.init()

width = 900
height = 900  # each square will be 100
BG_COLOR = (191, 239, 255)
square_size = 300
line_width = 5
row_length = 9
col_length = 9
screen = pygame.display.set_mode((width, height))
line_color = (0, 0, 0)
NUM_FONT = 100
number_font = pygame.font.Font(None, NUM_FONT)
number_color = (0, 0, 0)


def main():  # contains code to create different screens of project
	pygame.init()
	pygame.display.set_caption("")
	screen = pygame.display.set_mode((width, height))  # created black pop-up window
	screen.fill(BG_COLOR)  # changes background color

	for i in range(1, row_length):  # draws 8 horizonatal lines, 9 rows
		pygame.draw.line(screen, line_color, (0, i * square_size), (width, i * square_size), line_width)  # assuming screen 900 x 900

	for i in range(1, col_length): # draws 8 vertical lines
		pygame.draw.line(screen, line_color, (i * square_size, 0), (i * square_size), height)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()  # can close window
				sys.exit()
			if event.type ==pygame.MOUSEBUTTONDOWN:  # for selecting square?
				x, y = event.pos
				row, col = y // square_size, x // square_size


if __name__ == '__main__':
	main()