import numpy as np
import random
from IPython.display import clear_output, display_html
import time

ROWS = 30
COLS = 30

new_life = np.array( [ [0 for k in range(COLS)] for row in range(ROWS) ] )

# setup game with random living/dead cell arrangement
def setup():
    life = np.array( [ [random.getrandbits(1) for k in range(COLS)] for row in range(ROWS) ] )
    return life

#get total no. of live neighbour around the cell
def get_live_neighbors(row, col,life1):

    life_sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):

            if not (i == 0 and j == 0):
                life_sum += life1[((row + i) % ROWS)][((col + j) % COLS)]

    return life_sum

# create board of next life
def create_next_life(life1, next_life1):

    for row in range(ROWS):
        for col in range(COLS):

            live_neighbors = get_live_neighbors(row, col,life1)

            # Isolation or Overcrowding
            if live_neighbors < 2 or live_neighbors > 3:
                next_life1[row][col] = 0

            # Birth
            elif live_neighbors == 3 and life1[row][col] == 0:
                next_life1[row][col] = 1

            # Survival
            else:
                next_life1[row][col] = life1[row][col]

    return next_life1

#show board using html
def show_board(board):
    clear_output()
    nx, ny = board.shape
    table = '<table style="border-color: white; border-width: 8px;">\n'
    for y in range(ny-1, -1, -1):
        table += '<tr>'
        for x in range(0, nx):
            if board[x, y]:
                table += '<td style="background: black; border-color: white;"></td>'
            else:
                table += '<td style="border-color: white;"></td>'
        table += '</tr>\n'
    table += '</table>'
    display_html(table, raw=True)
    time.sleep(0.5)

# final function that call all other functions and take no. of generations as input 
def run_game_of_life(gens):
    life = setup()
    next_life = new_life
    show_board(life)
    #print(life)
    for _ in range(gens):
        next_gen = create_next_life(life, next_life)

        life, next_life = next_gen, new_life
        show_board(life)
