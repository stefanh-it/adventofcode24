from itertools import combinations
import string
import time
import numpy as np


class Grid():
    def __init__(self, lines: list[str]) -> None:
        grid = np.array([], dtype=str)
        for line in lines:
            grid = np.append(grid, list(line))
        grid = np.reshape(grid, (len(lines), len(lines[0])))
        self.grid = grid
        self.antinode_set = set()
        self.counter = 0

    def find_pairs(self, value='a') -> None:
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

    def log_nodes(self, y, x):
        if self.check_bounds(y, x):
            self.antinode_set.add((y, x))
            self.counter += 1
            return True
        return False

    def create_vectors(self, pair_list):
        for pair in pair_list:
            vector = np.array([pair[1][0] - pair[0][0], pair[1][1] - pair[0][1]])
            reverse_vector = np.array([vector[0] * -1, vector[1] * -1])
            a_y, a_x = pair[0] + reverse_vector
            b_y, b_x = pair[1] + vector
            a_true, b_true = True, True
            # print(f"evaluating {pair}")
            while a_true or b_true:
                if self.log_nodes(a_y, a_x) and a_true:
                    new_ay, new_ax = np.array([a_y, a_x]) + reverse_vector
                    a_y, a_x = new_ay, new_ax
                    # self.print_result()
                else:
                    a_true = False
                if self.log_nodes(b_y, b_x) and b_true:
                    new_by, new_bx = np.array([b_y, b_x]) + vector
                    b_y, b_x = new_by, new_bx
                    # self.print_result()
                else:
                    b_true = False
            self.antinode_set.add((pair[0][0], pair[0][1]))
            self.antinode_set.add((pair[1][0], pair[1][1]))
            # self.print_result(highlight=pair)

    def print_result(self, highlight: tuple | None = None, test=False):
        gridcopy = self.grid.copy()
        p1, p2 = None, None
        p1_y, p1_x, p2_y, p2_x = None, None, None, None
        if highlight:
            p1, p2 = highlight
            p1_y, p1_x = p1
            p2_y, p2_x = p2

        for y, x in self.antinode_set:
            if gridcopy[y, x] == '.':
                gridcopy[y, x] = '#'
        start: str = ''
        for i in range(self.grid.shape[1]):
            if i == 0:
                start = str(i)
            elif 0 < i < 10:
                start = start + ' ' * 2 + str(i)
            else:
                start = start + ' ' + str(i)

        print(start)
        for y, row in enumerate(gridcopy):
            print_row = []
            for x, char in enumerate(row):
                if y == p1_y and x == p1_x:
                    print_row.append("\033[91m" + char + "\033[00m")
                elif y == p2_y and x == p2_x:
                    print_row.append("\033[91m" + char + "\033[00m")
                else:
                    print_row.append(char)
            print(f'{"  ".join(print_row)}     {y}')
        y = 0
        if test:
            for _, row in enumerate(gridcopy):
                print(f'{"".join(row)}')


def main(data):
    start = time.perf_counter()
    lines = data.splitlines()
    grid = Grid(lines)
    chars = list(string.ascii_letters) + list(string.digits)
    for char in chars:
        grid.find_pairs(value=char)
    grid.print_result(test=False)
    elapsed = time.perf_counter() - start
    print(f"Time Elapsed: {elapsed:4f}s")
    return len(grid.antinode_set)

