from itertools import combinations
import string
import numpy as np


class Grid():
    def __init__(self, lines: list[str]) -> None:
        grid = np.array([], dtype=str)
        for line in lines:
            grid = np.append(grid, list(line))
        grid = np.reshape(grid, (len(lines), len(lines[0])))
        self.grid = grid
        self.antinode_set = set()

    def find_pairs(self, value='a'):
        pair_list = []
        coords = np.argwhere(self.grid == value)
        if coords.size == 0:
            return
        pair_list = list(combinations(coords, 2))
        self.create_vectors(pair_list)

    def check_bounds(self, y, x):
        if x > self.grid.shape[1] - 1:
            return False
        if y > self.grid.shape[0] - 1:
            return False
        if x < 0 or y < 0:
            return False
        return True

    def log_nodes(self, *args):
        for node in args:
            y, x = node
            if self.check_bounds(y, x):
                self.antinode_set.add((y, x))

    def create_vectors(self, pair_list):
        for pair in pair_list:
            vector = np.array([pair[1][0] - pair[0][0], pair[1][1] - pair[0][1]])
            reverse_vector = np.array([vector[0] * -1, vector[1] * -1])
            antinode_a = pair[0] + reverse_vector
            antinode_b = pair[1] + vector
            a_y, a_x = antinode_a
            b_y, b_x = antinode_b
            # if (a_y, a_x) == (11, 9) or (b_y, b_x) == (11, 9):
            if b_y == 11 or a_y == 11:
                print(antinode_a, antinode_b)
            if a_x == 9 or b_x == 9:
                print(antinode_a, antinode_b)
            #     breakpoint()
            self.log_nodes(antinode_a, antinode_b)

    def print_result(self):
        # print(self.grid)
        for y, x in self.antinode_set:
            self.grid[y, x] = '#'
        start: str = ''
        for i in range(self.grid.shape[1]):
            if i == 0 or i >= 10:
                start = start + ' ' * 2 + str(i)
            else:
                start = start + ' ' * 3 + str(i)
        print(start)
        for index, row in enumerate(self.grid):
            print(f"{row}  {index}")


def main(data):
    lines = data.splitlines()
    grid = Grid(lines)
    chars = list(string.ascii_letters) + list(string.digits)
    for char in chars:
        grid.find_pairs(value=char)
    grid.print_result()
    return print(len(grid.antinode_set))
