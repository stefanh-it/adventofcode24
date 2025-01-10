import numpy as np


class Grid():
    def __init__(self, lines: list[str]) -> None:
        grid = np.array([], dtype=str)
        for line in lines:
            grid = np.append(grid, list(line))
        grid = np.reshape(grid, (len(lines), len(lines[0])))
        self.grid = grid
        self.counter: int = 0

    def loop_inner(self):
        rows, cols = np.shape(self.grid)
        for y in range(1, cols - 1):
            for x in range(1, rows - 1):
                char = self.grid[y, x]
                compare_set = {'S', 'A', 'M'}
                if char == 'A':
                    charlist_1 = {
                        self.grid[y - 1, x - 1],
                        char,
                        self.grid[y + 1, x + 1]}
                    charlist_2 = {
                        self.grid[y - 1, x + 1],
                        char,
                        self.grid[y + 1, x - 1]}

                    if compare_set == charlist_1 and compare_set == charlist_2:
                        self.counter += 1


def main(data):
    lines = data.splitlines()
    # grid = Grid(lines)
    grid = Grid(lines)
    grid.loop_inner()
    return grid.counter
