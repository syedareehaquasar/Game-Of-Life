from collections import namedtuple, defaultdict
import time
import os

Cell = namedtuple('Cell', ['x', 'y'])


def getNeighbours(cell):
    for x in range(cell.x - 1, cell.x + 2):
        for y in range(cell.y - 1, cell.y + 2):
            if (x, y) != (cell.x, cell.y):
                yield Cell(x, y)


def getNeighbourCount(grid):
    neighbour_counts = defaultdict(int)
    for cell in grid:
        for neighbour in getNeighbours(cell):
            neighbour_counts[neighbour] += 1
    return neighbour_counts


def modified_grid(grid):
    new_grid = set()
    for cell, count in getNeighbourCount(grid).items():
        if count == 3 or (cell in grid and count == 2):
            new_grid.add(cell)
    return new_grid


def generategrid(input_grid):
    grid = set()
    for row, line in enumerate(input_grid.split("\n")):
        for col, elem in enumerate(line):
            if elem == '1':
                grid.add(Cell(int(col), int(row)))
    return grid


def gridToString(grid, padding=0):
    grid_str = ""
    xs = [x for (x, y) in grid]
    ys = [y for (x, y) in grid]
    for y in range(min(ys) - padding, max(ys) + 1 + padding):
        for x in range(min(xs) - padding, max(xs) + 1 + padding):
            grid_str += '1' if Cell(x, y) in grid else '0'
        grid_str += '\n'
    return grid_str.strip()


if __name__ == '__main__':
    grid = generategrid("00000010\n11000000\n01000111")
    for _ in range(100):
        grid = modified_grid(grid)
        os.system("clear")
        print(gridToString(grid, 2))
        time.sleep(0.5)
