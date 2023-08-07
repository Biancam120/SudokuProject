"""
Notes from Santiago Roa:

Sometimes if you click near the border of the board and press anything, a bug
happens where it'll give you an error that says:


                        if board[x - 1][y - 1] != 0:
                           ~~~~~^^^^^^^
                    IndexError: list index out of range


The same principle applies to cells. when you click on/ near the edge of a cell
it might input a digit to the cell adjacent to it.

I did not code lines 218 - 233 of user_input, but I did use these lines (which I think are the problem)
to use in most of the functions I created:


            x, y = int(pos[1] // square_size), int(pos[0] // square_size)
                                         and
            if board[x - 1][y - 1] != 0:


I wrote most of the functions of this code around/alongside this bug because it didn't completely break
the program if you knew where to click (near the center of each cell)

Also, if you mistakenly click a cell to delete it instead of hovering over, you have to press backspace twice.
Same thing with confirming a digit, if you click instead of hover, you have to press enter/return twice

If you clicked a cell, the game won't let you do anything else until you have inputted a digit

Finally, you cannot delete a confirmed cell in our version of sudoku.
"""


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
SKETCH_FONT = 60
sketch_font = pygame.font.Font(None, SKETCH_FONT)
number_color = (0, 0, 0)
RED = (255, 0, 0)


def draw_menu_screen():
    pygame.display.set_caption("Sudoku Menu")
    text_color = (0, 0, 0)
    title_font = pygame.font.Font(None, 100)
    select_font = pygame.font.Font(None, 75)
    message_font = pygame.font.Font(None, 55)
    button_font = pygame.font.Font(None, 50)
    button_color = (231, 223, 176)
    screen.fill(BG_COLOR)

    # welcome message code below
    welcome_text = "Welcome to Sudoku"
    welcome_surf = title_font.render(welcome_text, 0, text_color)
    welcome_rect = welcome_surf.get_rect(center=(width // 2, height // 4 - 50))
    screen.blit(welcome_surf, welcome_rect)

    # displays message to player
    toggle_text = "CLICK on a cell to sketch a digit"
    toggle_surf = message_font.render(toggle_text, 0, text_color)
    toggle_rect = toggle_surf.get_rect(center=(width // 2, height - 650))
    screen.blit(toggle_surf, toggle_rect)

    # continues message
    toggle_text = "HOVER over a cell and press BACKSPACE"
    toggle_surf = message_font.render(toggle_text, 0, text_color)
    toggle_rect = toggle_surf.get_rect(center=(width // 2, height - 550))
    screen.blit(toggle_surf, toggle_rect)

    # continues message
    toggle_text = "or ENTER/RETURN to delete or confirm number"
    toggle_surf = message_font.render(toggle_text, 0, text_color)
    toggle_rect = toggle_surf.get_rect(center=(width // 2, height - 500))
    screen.blit(toggle_surf, toggle_rect)

    # game mode selection message below
    mode_text = "Select a Game Mode:"
    mode_surf = select_font.render(mode_text, 0, text_color)
    mode_rect = mode_surf.get_rect(center=(width // 2, height - 300))
    screen.blit(mode_surf, mode_rect)

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
                # returns the amount of cells to remove
                if easy_rectangle.collidepoint(event.pos):
                    return 30
                elif medium_rectangle.collidepoint(event.pos):
                    return 40
                elif hard_rectangle.collidepoint(event.pos):
                    return 50
        pygame.display.update()


def draw_game_won_screen():
    pygame.display.set_caption("You Won!")
    text_color = (0, 0, 0)
    select_font = pygame.font.Font(None, 75)

    screen.fill(BG_COLOR)

    win_text = "Game Won!"  # creates the game won text
    win_surf = select_font.render(win_text, 0, text_color)
    win_rect = win_surf.get_rect(center=(width // 2, height - 600))
    screen.blit(win_surf, win_rect)

    exit_var = button_maker('EXIT', width // 2, height - 200)

    while True:  # this keeps the user on this screen until they press exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_var.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()


def draw_game_over_screen():
    pygame.display.set_caption("You Lost")
    text_color = (0, 0, 0)
    select_font = pygame.font.Font(None, 75)
    screen.fill(BG_COLOR)

    over_text = "Game Over :("  # creates the game over text
    over_surf = select_font.render(over_text, 0, text_color)
    over_rect = over_surf.get_rect(center=(width // 2, height - 600))
    screen.blit(over_surf, over_rect)

    restart_var = button_maker('RESTART', width // 2, height - 200)

    while True:  # this keeps the user on this screen until they press restart
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_var.collidepoint(event.pos):
                    main()
        pygame.display.update()


def draw_lines():
    for i in range(0, row_length + 1):  # draws 8 horizontal lines, 9 rows
        if i % 3 == 0:  # if statement to make every 3rd line thicker for visual purposes
            pygame.draw.line(screen, line_color, (100, (i * square_size) + 100), (width - 100, (i * square_size) + 100),
                             line_width + 4)
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


def button_maker(name, width, height):
    text = pygame.font.Font(None, 50).render(name, 0, (0, 0, 0))
    surface = pygame.Surface((text.get_size()[0] + 20, text.get_size()[
        1] + 20))  # creates surface that is 20 pixels larger all around the text
    surface.fill((231, 223, 176))
    surface.blit(text, (10, 10))  # blits at (10, 10) so its in the middle of the surface box
    rectangle = surface.get_rect(center=(width, height))
    screen.blit(surface, rectangle)
    return rectangle


def display_values(board):
    # offset to fit numbers in boxes
    offset = 110
    for i in range(0, 9):
        for j in range(0, 9):
            # for every number in the original board, blit the number at its respective row and col index
            output = board[i][j]
            # checks if the box is filled
            if output > 0:
                color = 'black'
                n_text = number_font.render(str(output), True, pygame.Color(color))
                screen.blit(n_text, pygame.Vector2((j * square_size) + offset, (i * square_size) + offset))


def userinput(screen, pos, board):
    # Makes the position on the grid into two variables
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
                # Makes sure the key press is 1-9 (since event.key of 48 and 57 is ASCII for 0 and 9)
                if 48 < event.key <= (48 + 9):
                    board[x - 1][y - 1] = event.key - 48
                    # sets the value of the cell to whatever digit was inputted

                    output = board[x - 1][y - 1]
                    # sets output to the value of the board at the clicked cell

                    if output > 0:
                        # prints the number as a gray sketch offset to the top left corner of the cell
                        offset = 30
                        color = (128, 128, 128)
                        n_text = sketch_font.render(str(output), True, color)
                        screen.blit(n_text,
                                    pygame.Vector2((y * square_size) + offset, (x * square_size) + offset))
                    return board


def finalize_input_of_cell(pos, sketch_board, final_sudoku):
    # ingrains the cell that was just confirmed from sketched_sudoku into final_sudoku list
    x, y = int(pos[1] // square_size), int(pos[0] // square_size)
    final_sudoku[x - 1][y - 1] = sketch_board[x - 1][y - 1]
    return final_sudoku


def confirm_input(screen, pos, og_board, sketch_board):
    x, y = int(pos[1] // square_size), int(pos[0] // square_size)
    if og_board[x - 1][y - 1] == 0:
        # If the position is blank, don't do anything
        if sketch_board[x - 1][y - 1] != 0:
            offset = 30
            output = sketch_board[x - 1][y - 1]
            if output > 0:
                cover_sketch(screen, pos, og_board, sketch_board)
                # cover the sketch with this function so that the value in the sketched_sudoku list is not removed
                # so as to not create a bug where you can input a digit over a confirmed digit
                color = (0, 0, 0)
                n_text = number_font.render(str(output), True, color)
                screen.blit(n_text,
                            pygame.Vector2((y * square_size) + offset, (x * square_size) + offset))
                # after the digit is covered, print the digit normally with black font and regular size
            return sketch_board
    else:
        return og_board


def delete_sketch(screen, pos, og_board, sketch_board, final_sudoku):
    delete = " "  # sets empty message to then create a box over
    offset = 30
    x, y = int(pos[1] // square_size), int(pos[0] // square_size)
    if og_board[x - 1][y - 1] == 0 and final_sudoku[x - 1][y - 1] == 0:  # 2nd part of if statement is to not delete confirmed digits
        if sketch_board[x - 1][y - 1] != 0:
            # this code creates a blue rectangle to cover sketched digit
            blue_text = number_font.render(delete, 0, BG_COLOR)
            blue_surface = pygame.Surface((blue_text.get_size()[0] + 15, blue_text.get_size()[1] - 5))
            blue_surface.fill(BG_COLOR)
            blue_surface.blit(blue_text, (10, 10))  # blits at (10, 10) so its in the middle of the surface box
            screen.blit(blue_surface, ((y * square_size) + offset, (x * square_size) + offset))
        sketch_board[x - 1][y - 1] = 0  # sets the value of the clicked cell back to 0
        # print(sketch_board[x - 1][y - 1])  <- used to debug


def cover_sketch(screen, pos, og_board, sketch_board):
    # creates a blue square to cover the sketched digit without replacing the value of the cell
    delete = " "
    offset = 30
    x, y = int(pos[1] // square_size), int(pos[0] // square_size)
    if og_board[x - 1][y - 1] == 0:
        if sketch_board[x - 1][y - 1] != 0:
            blue_text = number_font.render(delete, 0, BG_COLOR)
            blue_surface = pygame.Surface((blue_text.get_size()[0] + 15, blue_text.get_size()[1] - 5))
            blue_surface.fill(BG_COLOR)
            blue_surface.blit(blue_text, (10, 10))  # blits at (10, 10) so its in the middle of the surface box
            screen.blit(blue_surface, ((y * square_size) + offset, (x * square_size) + offset))
        # print(sketch_board[x - 1][y - 1])  <- for debug


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
        row = board[i]  # set a list equal to the ith row of the board
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
        for i in range(0, 9):  # this entire for loop makes one giant list of the columns with 81 digits from top down, left to right
            j = j  # used to increment j without having to mess up j = 0 above
            row = board[i]  # set a list equal to the ith row of the board
            column.append(row[j])  # appends the jth index of that row (starting at 0, increasing each iteration until j = 8)
        j += 1  # increases j by 1, essentially moving right a column and then going down every row to append the value of the jth index of the row

    column_sublist = [column[j:j + 9] for j in range(0, len(column), 9)]
    # takes the giant list of 81 digits and makes it into 9 different sublist representing each column of 9 digits

    for i in range(0, 9):  # works the same function as check_each_row
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
    sketched_sudoku = copy.deepcopy(sudoku_board)  # used to display user sketched digits. digits can be deleted
    final_sudoku = sudoku_board  # this variable is to keep track of the user confirmed inputs. digits cannot be deleted
    display_values(original_board)  # displays the initial board

    while True:
        reset_var = button_maker('RESET', width // 2 - 250, height - 150)
        restart_var = button_maker('RESTART', width // 2, height - 150)
        exit_var = button_maker('EXIT', width // 2 + 250, height - 150)
        # displays the buttons below the board
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # can close window
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_var.collidepoint(event.pos):
                    screen.fill(BG_COLOR)  # changes background color
                    draw_lines()
                    display_values(original_board)  # reverts the board to initial value
                    sketched_sudoku = copy.deepcopy(original_board)  # this is to reset sketched_sudoku
                    final_sudoku = copy.deepcopy(original_board)  # this is to reset final_sudoku
                    # print("reset")  <- used to debug
                    continue
                elif restart_var.collidepoint(event.pos):
                    main()
                    break
                elif exit_var.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif event.button == 1:  # means "if left mouse click is pressed"
                    pos = pygame.mouse.get_pos()
                    sketched_sudoku = userinput(screen, pos, sketched_sudoku)  # input the number user chooses to sketch
                    # print(["f"] + final_sudoku)  <- for debugging
                    # print(["s"] + sketched_sudoku)  <- for debugging
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    # print("pressed backspace")  <- used to debug
                    pos = pygame.mouse.get_pos()
                    delete_sketch(screen, pos, original_board, sketched_sudoku, final_sudoku)
                    # print(["d"] + sketched_sudoku)  <- used to debug
                else:
                    pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    # print("pressed enter")  <- used to debug
                    pos = pygame.mouse.get_pos()
                    # print(pos)  <- used to debug
                    confirm_input(screen, pos, original_board, sketched_sudoku)
                    final_sudoku = finalize_input_of_cell(pos, sketched_sudoku, final_sudoku)
                    # print(["f"] + final_sudoku)  <- used to debug
                    if check_if_full(final_sudoku):  # checks if board is full
                        if check_each_row(final_sudoku) and check_each_column(final_sudoku):
                            # if both conditions are satisfied, player has won
                            draw_game_won_screen()
                        else:
                            # else, they've lost
                            draw_game_over_screen()
                    else:
                        continue
            else:
                continue

        pygame.display.update()


if __name__ == '__main__':
    main()
