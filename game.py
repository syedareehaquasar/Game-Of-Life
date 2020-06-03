import random
import math
import pygame
import GameOfLife
pygame.init()
pygame.display.set_caption('Game of Life')


def draw_grid(win, grid, rows_showing_start, rows_showing_end, columns_showing_start, columns_showing_end, width_window):
    x, y = (0, 0)
    square_size = width_window//(rows_showing_end-rows_showing_start)
    for row in range(rows_showing_start, rows_showing_end+1):
        for column in range(columns_showing_start, columns_showing_end+1):
            if grid[row][column] == '1':
                pygame.draw.polygon(win, (0, 0, 255), ((x+square_size//2, y), (x, y+square_size//2),
                                                       (x+square_size//2, y+square_size), (x+square_size, y+square_size//2)))
            x += square_size
        x = 0
        y += square_size


def draw_window(win, grid, rows_showing_start, rows_showing_end, columns_showing_start, columns_showing_end, width_window):
    win.fill((0, 0, 0))
    draw_grid(win, grid, rows_showing_start, rows_showing_end,
              columns_showing_start, columns_showing_end, width_window)
    pygame.display.update()


def update_row_column_showing(rows_showing_start, rows_showing_end, columns_showing_start, columns_showing_end):
    return rows_showing_start+1, rows_showing_end+1, columns_showing_start+1, columns_showing_end+1


if __name__ == "__main__":
    width_window, height_window = (500, 500)
    win = pygame.display.set_mode((width_window, height_window))
    run_game = True
    space_bar_pressed = True
    clock = pygame.time.Clock()
    rows = 25
    grid = game_of_life.create_grid(rows)
    rows_showing_start, rows_showing_end, columns_showing_start, columns_showing_end = (
        1, rows, 1, rows)
    draw_window(win, grid, rows_showing_start, rows_showing_end,
                columns_showing_start, columns_showing_end, width_window)

    while run_game:

        pygame.time.delay(50)
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            space_bar_pressed = False if space_bar_pressed else True

        if keys[pygame.K_UP]:
            if rows_showing_end > rows_showing_start + 1:
                rows_showing_start += 1
                rows_showing_end -= 1
                columns_showing_start += 1
                columns_showing_end -= 1

        if keys[pygame.K_DOWN]:
            if rows_showing_end+2 >= rows or rows_showing_start-1 <= 0 or columns_showing_end+2 >= rows or columns_showing_start-1 <= 0:
                grid = game_of_life.add_blacks_around(
                    game_of_life.add_dead_cells_around(grid))
                rows += 2
                rows_showing_start, rows_showing_end, columns_showing_start, columns_showing_end = update_row_column_showing(
                    rows_showing_start, rows_showing_end, columns_showing_start, columns_showing_end)
            rows_showing_start -= 1
            columns_showing_start -= 1
            rows_showing_end += 1
            columns_showing_end += 1

        if keys[pygame.K_RIGHT]:
            if columns_showing_end+2 >= rows:
                grid = game_of_life.add_blacks_around(
                    game_of_life.add_dead_cells_around(grid))
                rows += 2
                rows_showing_start, rows_showing_end, columns_showing_start, columns_showing_end = update_row_column_showing(
                    rows_showing_start, rows_showing_end, columns_showing_start, columns_showing_end)
            columns_showing_end += 1
            columns_showing_start += 1

        if keys[pygame.K_LEFT]:
            if columns_showing_start-1 <= 0:
                grid = game_of_life.add_blacks_around(
                    game_of_life.add_dead_cells_around(grid))
                rows += 2
                rows_showing_start, rows_showing_end, columns_showing_start, columns_showing_end = update_row_column_showing(
                    rows_showing_start, rows_showing_end, columns_showing_start, columns_showing_end)
            columns_showing_end -= 1
            columns_showing_start -= 1

        if not space_bar_pressed:
            rows_before = rows
            grid, rows = game_of_life.update_grid(grid, rows)
            if rows_before < rows:
                rows_showing_start, rows_showing_end, columns_showing_start, columns_showing_end = update_row_column_showing(
                    rows_showing_start, rows_showing_end, columns_showing_start, columns_showing_end)

        draw_window(win, grid, rows_showing_start, rows_showing_end,
                    columns_showing_start, columns_showing_end, width_window)

    pygame.quit()