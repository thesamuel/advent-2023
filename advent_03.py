# Day 3: Gear Ratios
import re
from typing import List

INPUT_FILE = "inputs/03-input.txt"
# INPUT_FILE = "inputs/03-sample-pt1.txt"


# TODO: use regex to speed this up
def has_adjacent_symbols(
    lines: List[str],
    center_y: int,
    start_x: int,
    end_x: int,
) -> bool:
    for y in range(center_y - 1, center_y + 2):
        for x in range(start_x - 1, end_x + 1):
            # Skip iterations that are out of range
            if y == center_y and x in range(start_x, end_x):
                continue
            elif y not in range(len(lines)) or x not in range(len(lines[0])):
                continue

            c = lines[y][x]
            if not c.isdigit() and c != ".":
                return True

    return False


def part1(input_file: str) -> int:
    with open(input_file) as f:
        lines = [line.rstrip() for line in f.readlines()]

    # print(lines)

    non_adjacent_sum = 0
    for y in range(len(lines)):
        line = lines[y]
        numbers = list(re.finditer("[0-9]+", line))
        # print(numbers)

        for number in numbers:
            if has_adjacent_symbols(lines, y, number.start(), number.end()):
                non_adjacent_sum += int(number.group())

    return non_adjacent_sum


print("Part 1:", part1(INPUT_FILE))
