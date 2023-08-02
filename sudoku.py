import pygame, sys
from sudoku_generator import *

pygame.init()  # pygame is only used in this file

width = 900
height = 900  # each square will be 100
BG_COLOR = (191, 239, 255)
square_size = 100  # 900 / 9 squares
line_width = 5
row_length = 9
col_length = 9
screen = pygame.display.set_mode((width, height))  # creates black pop-up window
line_color = (0, 0, 0)
NUM_FONT = 100
number_font = pygame.font.Font(None, NUM_FONT)
number_color = (0, 0, 0)


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

    # easy button code
    easy_text = button_font.render("EASY", 0, text_color)
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))  # creates surface that is 20 pixels larger all around the text
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
                    return
                elif medium_rectangle.collidepoint(event.pos):
                    # set medium difficulty code here
                    return
                elif hard_rectangle.collidepoint(event.pos):
                    # hard difficulty code here
                    return
        pygame.display.update()


def draw_lines():
    for i in range(1, row_length):  # draws 8 horizontal lines, 9 rows
        if i % 3 == 0:  # if statement to make every 3rd line thicker for visual purposes
            pygame.draw.line(screen, line_color, (0, i * square_size), (width, i * square_size),
                             line_width + 4)  # assuming screen 900 x 900
        else:
            pygame.draw.line(screen, line_color, (0, i * square_size), (width, i * square_size), line_width)

    for i in range(1, col_length):  # draws 8 vertical lines
        if i % 3 == 0:  # if statement to make every 3rd line thicker for visual purposes
            pygame.draw.line(screen, line_color, (i * square_size, 0), (i * square_size, height), line_width + 4)
        else:
            pygame.draw.line(screen, line_color, (i * square_size, 0), (i * square_size, height), line_width)


def main():  # contains code to create different screens of project
    draw_menu_screen()
    pygame.display.set_caption("Sudoku Game")
    screen.fill(BG_COLOR)  # changes background color
    draw_lines()
    generate_sudoku(9, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # can close window
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # for selecting square?
                x, y = event.pos
                row, col = y // square_size, x // square_size

        pygame.display.update()


if __name__ == '__main__':
    main()
