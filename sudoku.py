import pygame, sys
import copy  # thank you chat GPT. lets me use copy.deepcopy() to store the original sudoku board to reset it
from sudoku_generator import *

pygame.init()  # pygame is only used in this file

width = 900
height = 1000
BG_COLOR = (191, 239, 255)
square_size = 700 / 9
line_width = 5
row_length = 9
col_length = 9
screen = pygame.display.set_mode((width, height))  # creates black pop-up window
line_color = (0, 0, 0)
NUM_FONT = 100
number_font = pygame.font.Font(None, NUM_FONT)
number_color = (0, 0, 0)
RED = (255, 0, 0)


def draw_menu_screen():
    pygame.display.set_caption("Sudoku Menu")
    text_color = (0, 0, 0)
    title_font = pygame.font.Font(None, 100)
    select_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 50)
    button_color = (231, 223, 176)
    screen.fill(BG_COLOR)

    # welcome message code below
    welcome_text = "Welcome to Sudoku"
    welcome_surf = title_font.render(welcome_text, 0, text_color)
    welcome_rect = welcome_surf.get_rect(center=(width // 2, height // 4 - 50))
    screen.blit(welcome_surf, welcome_rect)

    # game mode selection message below
    mode_text = "Select a Game Mode:"
    mode_surf = select_font.render(mode_text, 0, text_color)
    mode_rect = mode_surf.get_rect(center=(width // 2, height - 400))
    screen.blit(mode_surf, mode_rect)

    # display the mark toggle option
    toggle_text = "Press Shift to Toggle Marker Mode"
    toggle_surf = select_font.render(toggle_text, 0, text_color)
    toggle_rect = toggle_surf.get_rect(center=(width // 2, height - 600))
    screen.blit(toggle_surf, toggle_rect)

    # easy button code
    easy_text = button_font.render("EASY", 0, text_color)
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[
        1] + 20))  # creates surface that is 20 pixels larger all around the text
    easy_surface.fill(button_color)
    easy_surface.blit(easy_text, (10, 10))  # blits at (10, 10) so its in the middle of the surface box
    easy_rectangle = easy_surface.get_rect(center=(width // 2 - 250, height - 200))
    screen.blit(easy_surface, easy_rectangle)

    # medium button code
    medium_text = button_font.render("MEDIUM", 0, text_color)
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(button_color)
    medium_surface.blit(medium_text, (10, 10))
    medium_rectangle = medium_surface.get_rect(center=(width // 2, height - 200))
    screen.blit(medium_surface, medium_rectangle)

    # hard button code
    hard_text = button_font.render("HARD", 0, text_color)
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(button_color)
    hard_surface.blit(hard_text, (10, 10))
    hard_rectangle = hard_surface.get_rect(center=(width // 2 + 250, height - 200))
    screen.blit(hard_surface, hard_rectangle)

    while True:  # this keeps the user on this screen until they choose a difficulty, then returns to the main function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    # set easy difficulty code here
                    return 30
                elif medium_rectangle.collidepoint(event.pos):
                    # set medium difficulty code here
                    return 40
                elif hard_rectangle.collidepoint(event.pos):
                    # hard difficulty code here
                    return 50
        pygame.display.update()


def draw_lines():
    for i in range(0, row_length + 1):  # draws 8 horizontal lines, 9 rows
        if i % 3 == 0:  # if statement to make every 3rd line thicker for visual purposes
            pygame.draw.line(screen, line_color, (100, (i * square_size) + 100), (width - 100, (i * square_size) + 100),
                             line_width + 4)  # assuming screen 900 x 900
        else:
            pygame.draw.line(screen, line_color, (100, (i * square_size) + 100), (width - 100, (i * square_size) + 100),
                             line_width)

    for i in range(0, col_length + 1):  # draws 8 vertical lines
        if i % 3 == 0:  # if statement to make every 3rd line thicker for visual purposes
            pygame.draw.line(screen, line_color, ((i * square_size) + 100, 100),
                             ((i * square_size) + 100, height - 200), line_width + 4)
        else:
            pygame.draw.line(screen, line_color, ((i * square_size) + 100, 100),
                             ((i * square_size) + 100, height - 200), line_width)


def display_values(board):
    # offset to fit numbers in boxes
    offset = 110
    for i in range(0, 9):
        for j in range(0, 9):
            output = board[i][j]
            # checks if the box is filled
            if output > 0:
                n_text = number_font.render(str(output), True, pygame.Color('black'))
                screen.blit(n_text, pygame.Vector2((j * square_size) + offset, (i * square_size) + offset))


def buttonmaker(name, width, height):
    exit_text = pygame.font.Font(None, 50).render(name, 0, (0, 0, 0))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[
        1] + 20))  # creates surface that is 20 pixels larger all around the text
    exit_surface.fill((231, 223, 176))
    exit_surface.blit(exit_text, (10, 10))  # blits at (10, 10) so its in the middle of the surface box
    exit_rectangle = exit_surface.get_rect(center=(width, height))
    screen.blit(exit_surface, exit_rectangle)
    return exit_rectangle


def userinput(screen, pos, board):
    # Makes the position into two variables
    x, y = int(pos[1] // square_size), int(pos[0] // square_size)
    while True:
        for event in pygame.event.get():
            # Check to see if the program has ended
            if event == pygame.QUIT:
                return
            # Check to see if a button is pressed
            if event.type == pygame.KEYDOWN:
                # If the position is taken, don't do anything
                if board[x - 1][y - 1] != 0:
                    return board
                # Makes sure the key press is 1-9
                if 48 < event.key <= (48 + 9):
                    pygame.draw.rect(screen, BG_COLOR, (
                        pos[0] * square_size + 5, pos[1] * square_size + 5, square_size - 5, square_size - 5))
                    value = number_font.render(str(event.key - 48), True, 'red')
                    screen.blit(value, (pos[0] * square_size + 15, pos[1] * square_size))
                    pygame.display.update()
                    board[x - 1][y - 1] = event.key - 48
                    return board


def check_if_full(board):
    # goes through each digit in the board and checks if it is 0. if it is, then return false
    for row in board:
        for digit in row:
            if digit == 0:
                return False
    return True


def check_each_row(board):  # half of the code used to check a solved sudoku board
    row_count = 0  # keep track of how many correct rows there are
    run_count = 0  # keep track of how many iterations
    for i in range(0, 9):  # for the entire board, iterate through each row
        row = board[i]  # set a variable equal to the ith row
        sudoku_row = set(row)  # turn the list into a set
        valid_row = set(range(1, 10))  # make a set that contains the digits 1-9
        if sudoku_row == valid_row:  # checks to see if the current row is a valid row
            row_count += 1  # if it is, increase row and run count by 1
            run_count += 1
        else:
            run_count += 1  # else, only increase the run
        if run_count == 9 and row_count == 9:  # if both run and row count are 9, return true
            return True
        elif run_count == 9 and row_count < 9:
            return False


def check_each_column(board):  # the other half of code to check a winning board
    column = []  # empty list to store sliced list
    j = 0  # j is used to indicate the jth index of the sliced board list
    col_count = 0
    run_count = 0
    while 0 <= j <= 8:  # runs 9 times for 9 rows
        for i in range(0, 9): # this entire for loop makes one giant list of the columns with 81 digits from top down, left to right
            j = j  # used to increment j without having to mess up j = 0 above
            row = board[i]  # sets a variable to store the ith row of the board
            column.append(row[j])  # appends the jth index of that row
        j += 1  # increases j by 1, essentially moving right a column

    column_sublist = [column[j:j + 9] for j in range(0, len(column), 9)]
    # takes the giant list of 81 digits and makes it into 9 different sublist representing each column of 9 digits

    for i in range(0, 9):  # works the same function as check_horizontal
        col = column_sublist[i]
        sudoku_col = set(col)
        valid_col = set(range(1, 10))
        if sudoku_col == valid_col:
            col_count += 1
            run_count += 1
        else:
            run_count += 1
        if run_count == 9 and col_count == 9:
            return True
        elif run_count == 9 and col_count < 9:
            return False


def main():  # contains code to create different screens of project
    difficulty = draw_menu_screen()
    pygame.display.set_caption("Sudoku Game")
    screen.fill(BG_COLOR)  # changes background color
    draw_lines()
    sudoku_board = generate_sudoku(9, difficulty)  # generates the sudoku board
    original_board = copy.deepcopy(sudoku_board)  # set original_board to the first un-edited list so the reset button calls this variable
    updated_sudoku = sudoku_board  # this variable is to keep track of the user inputs
    display_values(updated_sudoku)

    while True:
        reset_var = buttonmaker('RESET', width // 2 - 250, height - 150)
        restart_var = buttonmaker('RESTART', width // 2, height - 150)
        exit_var = buttonmaker('EXIT', width // 2 + 250, height - 150)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # can close window
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # might need to add and not is_full
                if reset_var.collidepoint(event.pos):
                    screen.fill(BG_COLOR)  # changes background color
                    draw_lines()
                    display_values(original_board)  # reverts the board to initial value
                    updated_sudoku = copy.deepcopy(original_board)  # this is to reset updated_sudoku
                    continue
                elif restart_var.collidepoint(event.pos):
                    main()
                    break
                elif exit_var.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif event.button == 1:
                    pos = pygame.mouse.get_pos()
                    updated_sudoku = userinput(screen, pos, updated_sudoku)  # input the number user chooses
                    display_values(updated_sudoku)
                    # print(["u"] + updated_sudoku)  <- degubbing purposes, please leave this here for me if you work on it
                    if check_if_full(updated_sudoku):  # checks if board is full
                        if check_each_row(updated_sudoku) and check_each_column(updated_sudoku):
                            # if both horizontal and vertical conditions are satisfied, player has won
                            print("won")
                        else:
                            print("lost")
                    else:
                        continue

        pygame.display.update()


if __name__ == '__main__':
    main()
