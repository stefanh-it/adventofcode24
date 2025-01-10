from enum import Enum


def main(data):
    score: int = 0
    line_strings = data.splitlines()
    score = convert_lines(line_strings)
    return score


def convert_lines(lines: list) -> int:
    score_sum: int = 0
    for _, line in enumerate(lines):
        int_line = line.split(" ")
        # print(int_line)
        int_line = list(map(int, int_line))
        # print(f"running line {i+1}")
        iteration_value = iterate_line(int_line)
        if iteration_value == -1:
            # verify direction integrity
            score_sum += 1
            print(f"round won  {int_line}")
        elif iteration_value >= 0:
            bad_line1 = create_bad_line(int_line, iteration_value)
            bad_line2 = create_bad_line(int_line, iteration_value + 1)
            if iterate_line(bad_line1) == -1:
                score_sum += 1
                print(f"round won converted: {int_line} to {bad_line1}")
            elif iterate_line(bad_line2) == -1:
                score_sum += 1
                print(f"round won: {int_line} to {bad_line2}")
            else:
                print(f"Round Lost {int_line}")
    return score_sum


def iterate_line(line: list[int]) -> int:
    i: int = 1
    direction_set = set()
    while i in range(1, len(line)):
        if not 0 < abs(line[i - 1] - line[i]) <= 3:
            return i
        if len(direction_set) > 1:
            return i
        direction = evaluate_direction(line[i - 1], line[i])
        if direction == Direction.EVEN:
            return i
        direction_set.add(direction)
        i += 1
    return -1


def create_bad_line(line: list[int], i: int) -> list:
    return line[:i] + line[i + 1:]


class Direction(Enum):
    DOWN = 0
    UP = 1
    EVEN = -1


def evaluate_direction(prev_int: int, next_int: int) -> Direction:
    if prev_int < next_int:
        return Direction.UP
    if prev_int > next_int:
        return Direction.DOWN
    return Direction.EVEN
