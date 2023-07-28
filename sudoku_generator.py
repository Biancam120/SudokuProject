import random

class SudokuGenerator:
	def __init__(self, row_length, removed_cells):
		self.row_length = 9  # always 9
		self.removed_cells = removed_cells  # depending on difficulty (easy = 30, med = 40, hard = 50)
		self.board = [[0 for i in range(row_length)] for j in range(row_length)] # prints 0 in each box in board
		self.box_length = 3 # square root of the row

	def get_board(self):  # returns 2D list of num which represents the board
		return self.board

	def print_board(self):
		return self.board  # displays board to the console

	def valid_in_row(self, row, num):
		for col in range(self.row_length):  # looks through 9 col
			if self.board[row][col] == num:  # determines if num is in given row of the board
				return False
			else:
				return True

	def valid_in_col(self, col, num):
		for row in range(self.row_length):  # looks through 9 rows
			if self.board[row][col] == num: # determines if num is in given col
				return False
			else:
				return True

	def valid_in_box(self, row_start, col_start, num):
		# for row in range(row_start, row_start + 2):
		# 	if self.board[row][col_start] == num: # when you fix the row you look at all the columns
		# 		return False
		# 	else:
		# 		return True
		# for col in range(col_start, col_start + 2):
		# 	if self.board[row_start][col] == num:
		# 		return False
		# 	else:
		# 		return True

		for i in range(row_start, row_start + 2): # runs through the 3 rows in the box
			if self.board[row_start][i] == num:  # fixes row and checks each column
				return False
			else:
				return True

		for i in range(col_start, col_start + 2): # runs through the 3 columns in the box
			if self.board[i][col_start] == num: # fixes column and checks each row for number
				return False
			else:
				return True


	def is_valid(self, row, col, num):  # determine if it is valid to enter num (checks row col and box)
		if self.valid_in_box and self.valid_in_row and self.valid_in_col == True:
			return True # if all are valid then function is True
		else:
			return False

	def fill_box(self, row_start, col_start):
		for i in range(row_start, row_start + 2): # defines 3x3 box
			if self.board[row_start][i] is self.valid_in_box:
				print(random.randint(1,9))
		for i in range(col_start, col_start + 2): # defines box
			if self.board[i][col_start] is self.valid_in_box:
				print(random.randint(1,9))

	def fill_diagonal(self):  # fills boxes in diagonal
		pass

	def fill_remaining(self, row, col):  # method was provided on Github, fills remaining cells of the board
		if (col >= self.row_length and row < self.row_length - 1):
			row += 1
			col = 0
		if row >= self.row_length and col >= self.row_length:
			return True
		if row < self.box_length:
			if col < self.box_length:
				col = self.box_length
		elif row < self.row_length - self.box_length:
			if col == int(row // self.box_length * self.box_length):
				col += self.box_length
		else:
			if col == self.row_length - self.box_length:
				row += 1
				col = 0
				if row >= self.row_length:
					return True

		for num in range(1, self.row_length + 1):
			if self.is_valid(row, col, num):
				self.board[row][col] = num
				if self.fill_remaining(row, col + 1):
					return True
				self.board[row][col] = 0
		return False  # True if board could be solved

	def fill_values(self):  # method was provided, constructs solution bby filling boxes
		self.fill_diagonal()
		self.fill_remaining(0, self.box_length)

	def remove_cells(self):  # sets values to zero, called after solution is constructed
		self.removed_cells = 0


def generate_sudoku(size, removed):  # function outside class, was provided
	sudoku = SudokuGenerator(size, removed) # created a SudokuGenerator
	sudoku.fill_values() # fills values and saves it as the solved state
	board = sudoku.get_board()
	sudoku.remove_cells() # removes cells depending on difficulty
	board = sudoku.get_board()
	return board  # returns 2D lists to make board with its solution


class Cell:
	def __init__(self, value, row, col, screen, width, height):  # 81 cells as building block of sudoku board
		self.value = value  # number in cell
		self.row = row  # index
		self.col = col  # index
		self.screen = screen
		self.width = width  # 100 for each cell
		self.height = height # 100 for each cell


	def set_cell_value(self, value): # setter for cell's value
		self.value = value

	def set_sketched_value(self, value): # setter for sketeched value
		self.value = value

	def draw(self, screen): # draws the cell and value inside of it
		square_size = 100
		# enter value inside cell
		if self.value != 0: # zero means empty cell
			num_val = self.value  # specifies location
			num_cell = num_val.get_rect(center=(self.col * square_size + square_size // 2, self.row * square_size + square_size // 2))
			screen.blit(num_val, num_cell)  # adds number onto screen





class Board:
	def __init__(self, width, height, screen, difficulty):
		self.width = width
		self.height = height
		self.screen = screen
		self.difficulty = difficulty
		self.board = SudokuGenerator.get_board # gets board, 2D list



	def draw(self):
		pass

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
		for row in self.board:  # indicates if board is full or not
			for value in row:
				if value == 0:
					return False
		return True

	def update_board(self):
		pass

	def find_empty(self):
		pass

	def check_board(self):
		pass

