import numpy as np


class Grid():
    def __init__(self, lines: list[str]) -> None:
        grid = np.array([], dtype=str)
        for line in lines:
            grid = np.append(grid, list(line))
        grid = np.reshape(grid, (len(lines), len(lines[0])))
        self.grid = grid
        self.direction: int = 0
        self.start = None
        self.routeset = set()

    def change_direction(self) -> None:
        if self.direction == 3:
            self.direction = 0
        else:
            self.direction += 1

    def find_start(self) -> None:
        self.start = np.argwhere(self.grid == '^')[0]
        self.position = (self.start[0], self.start[1])

    def walk(self) -> None:
        y = self.position[0]
        x = self.position[1]
        self.routeset.add(self.position)
        # print(f"Visiting y: {y}, x: {x}")
        match self.direction:
            case 0:
                self.position = y - 1, x
            case 1:
                self.position = y, x + 1
            case 2:
                self.position = y + 1, x
            case 3:
                self.position = y, x - 1
        # Check bad case
        if self.grid[self.position] == '#':
            self.change_direction()
            self.position = y, x


def main(data):
    score = 0
    lines = data.splitlines()
    grid = Grid(lines)
    grid.find_start()
    walking = True
    while walking:
        try:
            grid.walk()
        except IndexError:
            score = len(grid.routeset)
            walking = False
    return score
