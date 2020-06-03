from itertools import product


alive = '1'
dead = '0'


def add_sentinels(grid):
    size = len(grid[0])
    new_grid = [dead + row + dead for row in grid]
    new_grid.append((size + 2) * dead)
    new_grid.insert(0, (size + 2) * dead)
    return new_grid


def update_grid(grid, rows, columns):
    all_neighbours = [neighbour for neighbour in product(
        [-1, 0, 1], repeat=2) if not neighbour == (0, 0)]

    def count_living_neighbours(row, column):
        return len([1 for row_neighbour, column_neighbour in all_neighbours if grid[row + row_neighbour][column + column_neighbour] == '1'])

    new_grid = grid.copy()

    for row in range(1, rows+1):
        for column in range(1, columns+1):
            living_neighbours = count_living_neighbours(row, column)
            if living_neighbours in (2, 3):
                if grid[row][column] == '0' and living_neighbours == 3:
                    new_grid[row] = new_grid[row][:column] + '1' + new_grid[row][column + 1:]
            else:
                new_grid[row] = new_grid[row][:column] + '0' + new_grid[row][column + 1:]
    return new_grid


def next_generation(gol_file):
    input_grid = [line.strip() for line in gol_file]
    grid = add_sentinels(input_grid)
    rows, columns = len(input_grid[0]), len(input_grid)
    new_grid = update_grid(grid, rows, columns)
    return "\n".join(line for line in new_grid)


print(next_generation(open("data.txt")))
