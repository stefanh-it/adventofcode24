import re

def main(data):
    score: int = 0
    line_string = data.strip()
    score = convert_line(line_string)
    return score


def convert_line(line: str) -> int:
    score_sum: int = 0
    match = re.compile(r'mul\(\d+\,\d+\)')
    matches = match.findall(line)
    for match in matches:
        digits = re.findall(r'\d+', match)
        digits = list(map(int, digits))
        score_sum += digits[0] * digits[1]
    return score_sum
