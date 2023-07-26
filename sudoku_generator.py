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

class SudokuGenerator:
	def __init__(self, row_length, removed_cells):
		self.row_length = row_length  # always 9
		self.removed_cells = removed_cells  # varies depending on difficulty (easy = 30, med = 40, hard = 50)

	def get_board(self):  # returns 2D list of num which represents the board
		pass

	def print_board(self):
		pass

	def valid_in_row(self, row, num):
		if self.row == num:  # determines if num is in given row of the board
			return True
		else:
			return False

	def valid_in_col(self, col, num):
		if self.col == num:
			return True
		else:
			return False

	def valid_in_box(self, row_start, col_start, num):
		pass

	def is_valid(self, row, col, num):
		pass

	def fill_box(self, row_start, col_start):
		pass

	def fill_diagonal(self):
		pass

	def fill_remaining(self, row, col):  # method is provided
		pass

	def fill_values(self):  # method is provided
		pass

	def remove_cells(self):
		pass


def generate_sudoku(size, removed):  # function outside class
	pass


class Cell:
	def __init__(self, value, row, col, screen):
		self.value = value
		self.row = row
		self.col = col
		self.screen = screen


	def set_cell_value(self, value): # setter for cell's value
		pass

	def set_sketched_value(self, value): # setter for sketeched value
		pass

	def draw(self):
		pass


class Board:
	def __init__(self, width, height, screen, difficulty):
		self.width = width
		self.height = height
		self.screen = screen
		self.difficulty = difficulty
		# screen = pygame.display.set_mode((width, height)) # displays pop up screen

	def draw(self):
		for i in range(1, row_length):  # 8 horizonatal lines, 9 rows
			pygame.draw.line(screen, line_color, (0, i * square_size), (width, i * square_size), line_width)  # assuming screen 900 x 900

		for i in range(1, col_length):
			pygame.draw.line(screen, line_color, (i * square_size, 0), (i * square_size), height)

	def select(self, row, col):
		pass

	def click(self, x, y):
		pass

	def clear(self):
		pass

	def sketch(self, value):
		pass

	def place_number(self, value):
		num_placed = number_font.render(num_inputted_variable, 0, number_color)
		num_location = num_placed.get_rect(# selected box)
		# use screen.blit() to place num of screen

	def reset_to_original(self):
		pass

	def is_full(self):
		pass

	def update_board(self):
		pass

	def find_empty(self):
		pass

	def check_board(self):
		pass

