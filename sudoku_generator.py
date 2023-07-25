class SudokuGenerator:
	def __init__(self, row_length, removed_cells):
		pass

	def get_board(self):
		pass

	def print_board(self):
		pass

	def valid_in_row(self, row, num):
		pass

	def valid_in_col(self, col, num):
		pass

	def valid_in_box(self, row_start, col_start, num):
		pass

	def is_valid(self, row, col, num):
		pass

	def fill_box(self, row_start, col_start):
		pass

	def fill_diagonal(self):
		pass

	def fill_remaining(self, row, col):
		pass

	def fill_values(self):
		pass

	def remove_cells(self):
		pass

	def generate_sudoku(size, removed):
		pass


class Cell:
	def __init__(self, value, row, col, screen):
		pass


	def set_cell_value(self, value):
		pass

	def set_sketched_value(self, value):
		pass

	def draw(self):
		pass


class Board:
	def __init__(self, width, height, screen, difficulty):
		pass

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
		pass

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


if __name__ == '__main__':
	main()
