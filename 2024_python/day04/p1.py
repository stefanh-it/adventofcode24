import numpy as np


class Grid():
    def __init__(self, lines: list[str]) -> None:
        grid = np.array([], dtype=str)
        for line in lines:
            grid = np.append(grid, list(line))
        grid = np.reshape(grid, (len(lines), len(lines[0])))
        self.grid = grid
        self.diagonals = []
        self.rotated = np.rot90(self.grid)
        self.counter = 0

    def get_diago(self):
        rows, cols = self.grid.shape
        flipped = np.fliplr(self.grid)
        for k in range(-(rows - 1), cols):
            self.diagonals.append(self.grid.diagonal(offset=k).tolist())
            self.diagonals.append(flipped.diagonal(offset=k).tolist())

    def search(self):
        for row, column in zip(self.grid, self.rotated):
            row = "".join(row)
            column = "".join(column)
            self.counter += row.count('XMAS') + row.count('SAMX') \
                + column.count('XMAS') + column.count('SAMX')

        for row in self.diagonals:
            row = "".join(row)
            self.counter += row.count('XMAS') + row.count('SAMX')


def main(data):
    lines = data.splitlines()
    # grid = Grid(lines)
    grid = Grid(lines)
    grid.get_diago()
    grid.search()
    return grid.counter
