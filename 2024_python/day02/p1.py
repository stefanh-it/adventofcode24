from enum import Enum


def main(data):
    score: int = 0
    line_strings = data.splitlines()
    score = convert_lines(line_strings)
    return score


def convert_lines(lines: list) -> int:
    score_sum: int = 0
    for line in lines:
        int_line = line.split(" ")
        # print(int_line)
        int_line = list(map(int, int_line))
        if check_direction(int_line):
            score_sum += 1
    return score_sum


def check_direction(line: list[int]) -> bool:
    direction_set = set()
    i: int = 1
    while i in range(1, len(line)):
        if line[i - 1] - line[i] in [-3, -2, -1, 1, 2, 3]:
            direction = evaluate_direction(line[i - 1], line[i])
            direction_set.add(direction)
        else:
            return False
        if len(direction_set) > 1:
            return False
        i += 1
    return True


class Direction(Enum):
    DOWN = 0
    UP = 1


def evaluate_direction(prev_int: int, next_int: int) -> Direction:
    if prev_int < next_int:
        return Direction.UP
    return Direction.DOWN
