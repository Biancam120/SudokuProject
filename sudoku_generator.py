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
		# modified to check whole col, will do the same for col, box, and is valid
		return True

	def valid_in_col(self, col, num):
		for row in range(self.row_length):  # looks through 9 rows
			if self.board[row][col] == num:  # determines if num is in given col
				return False
		return True

	def valid_in_box(self, row_start, col_start, num):

		'''
		I was checking the code here and I don't think it'll check all boxes but rather cut off when it finds a true
		condition, but I'm not sure, therefore, I'll simply put the code I think works in this comment, and we can test
		it when we test run the full program '''

		for i in range(3):
			for j in range(3):
				if self.board[row_start + i][col_start + j] == num:
					return False
		return True

		# for i in range(row_start, row_start + 2): # runs through the 3 rows in the box
		# 	if self.board[row_start][i] == num:  # fixes row and checks each column
		# 		return False
		# 	else:
		# 		return True
		#
		# for i in range(col_start, col_start + 2): # runs through the 3 columns in the box
		# 	if self.board[i][col_start] == num: # fixes column and checks each row for number
		# 		return False
		# 	else:
		# 		return True

	def is_valid(self, row, col, num):  # determine if it is valid to enter num (checks row col and box)
		if self.board[row][col] == 0:  # means it is empty
			for i in range(row):  # checks row
				for j in range(col):
					if self.board[row][i] != num and self.board[j][col] != num:
						return True  # if all are valid then function is True
		return False

	def fill_box(self, row_start, col_start):
		for i in range(row_start, row_start + 2):  # defines 3x3 box
			if self.board[row_start][i] is self.valid_in_box:
				print(random.randint(0, 8))
		for i in range(col_start, col_start + 2):  # defines box
			if self.board[i][col_start] is self.valid_in_box:
				print(random.randint(0, 8))

	def fill_diagonal(self):  # fills boxes in diagonal
		# fill the top left box, middle box, then bottom right box (0 to 3 to 6)
		self.fill_box(0, 0)
		self.fill_box(3, 3)
		self.fill_box(6, 6)

	def fill_remaining(self, row, col):  # method was provided on Github, fills remaining cells of the board
		if col >= self.row_length and row < self.row_length - 1:
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

	def fill_values(self):  # method was provided, constructs solution by filling boxes
		self.fill_diagonal()
		self.fill_remaining(0, self.box_length)

	def remove_cells(self):  # sets values to zero, called after solution is constructed
		# doesn't remove cells that are already 0
		for i in range(self.removed_cells):  # removes amount defined by difficulty
			row = random.randint(0, 8)  # creates random row
			col = random.randint(0, 8)  # creates random col
			while self.board[row][col] == 0:
				row = random.randint(0, 8)
				col = random.randint(0, 8)
			self.board[row][col] = 0




def generate_sudoku(size, removed):  # function outside class, was provided
	# I removed the first instance of get board as it would simply make remove_cells do nothing
	sudoku = SudokuGenerator(size, removed) # created a SudokuGenerator
	sudoku.fill_values()  # fills values and saves it as the solved state
	sudoku.remove_cells()  # removes cells depending on difficulty
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

	def set_cell_value(self, value):  # setter for cell's value
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

	def update_value(self):
		# I'm adding this in to allow me to program update_board in the board class
		if self.value < 0:
			self.value *= -1


class Board:
	def __init__(self, width, height, screen, difficulty):
		self.width = width
		self.height = height
		self.screen = screen
		self.difficulty = difficulty
		# cells variables will be tracked to make coloring of cells and such easier
		self.cells = [[Cell(0, row, col, screen, width, height) for col in range(9)] for row in range(9)]
		self.selected_cell = None

	def draw(self):
		# create the outline of the grind and the cells, embolden the 3x3 boxes
		for row in range(9):
			if row % 3 == 0:
				print("+" + "-" * 23 + "+")
			for col in range(9):
				if col % 3 == 0:
					print("|", end=" ")
				cell_value = self.cells[row][col].value
				print(" " if cell_value == 0 else cell_value, end=" ")
			print("|")
		print("+" + "-" * 23 + "+")

	def select(self, row, col):
		self.selected_cell = self.cells[row][col]

	def click(self, x, y):
		# return tuple coordinates IF the cell has one
		row = y // (self.height // 9)
		col = x // (self.width // 9)
		if 0 <= row < 9 and 0 <= col < 9:
			return row, col
		else:
			return None

	def clear(self):
		# empty out the current cell, only if not a predetermined cell
		if self.selected_cell:
			if self.selected_cell.value == 0:
				self.selected_cell.set_cell_value(0)
				self.selected_cell.set_sketched_value(None)

	def sketch(self, value):
		# put in the sketched value
		if self.selected_cell:
			self.selected_cell.set_sketched_value(value)

	def place_number(self, value):
		if self.selected_cell:
			self.selected_cell.set_cell_value(value)

	def reset_to_original(self):
		# set all the cells back to original values
		for row in range(9):
			for col in range(9):
				if self.cells[row][col].value == 0:
					self.cells[row][col].set_cell_value(0)

	def is_full(self):
		for row in self.cells:  # indicates if board is full or not
			for cell in row:
				if cell.value == 0:		# I replaced cell with value to use to value command
					return False
		return True

	def update_board(self):
		for row in self.cells:
			for cell in row:
				cell.update_value()

	def find_empty(self):
		# find an empty and return its row and col
		for row in range(9):
			for col in range(9):
				if self.cells[row][col].value == 0:
					return row, col
		return None

	def check_board(self):
		# check if the Sudoku board is solved correctly
		for i in range(9):
			row_values = set()
			col_values = set()
			box_values = set()

			for j in range(9):
				if self.cells[i][j].value in row_values:
					return False
				row_values.add(self.cells[i][j].value)

				if self.cells[j][i].value in col_values:
					return False
				col_values.add(self.cells[j][i].value)

				box_row = 3 * (i // 3) + j // 3
				box_col = 3 * (i % 3) + j % 3
				if self.cells[box_row][box_col].value in box_values:
					return False
				box_values.add(self.cells[box_row][box_col].value)
		return True

