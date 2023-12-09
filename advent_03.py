# Day 3: Gear Ratios
import re

INPUT_FILE = "inputs/03-input.txt"


# TODO: use regex to speed this up
def get_adjacent_symbols(
    lines: list[str],
    center_y: int,
    start_x: int,
    end_x: int,
) -> list[tuple[int, int]]:
    symbol_coordinates = []
    for y in range(center_y - 1, center_y + 2):
        for x in range(start_x - 1, end_x + 1):
            # Skip iterations that are out of range
            if y == center_y and x in range(start_x, end_x):
                continue
            elif y not in range(len(lines)) or x not in range(len(lines[0])):
                continue

            c = lines[y][x]
            if not c.isdigit() and c != ".":
                symbol_coordinates.append((x, y))

    return symbol_coordinates


def part1(input_file: str) -> int:
    with open(input_file) as f:
        lines = [line.rstrip() for line in f]

    non_adjacent_sum = 0
    for y in range(len(lines)):
        for number in re.finditer("[0-9]+", lines[y]):
            if get_adjacent_symbols(lines, y, number.start(), number.end()):
                non_adjacent_sum += int(number.group())

    return non_adjacent_sum


def part2(input_file: str) -> int:
    with open(input_file) as f:
        lines = [line.rstrip() for line in f]

    symbol_coordinates_to_numbers = {}
    for y in range(len(lines)):
        for number in re.finditer("[0-9]+", lines[y]):
            for adjacent_symbol in get_adjacent_symbols(
                lines, y, number.start(), number.end()
            ):
                symbol_coordinates_to_numbers.setdefault(adjacent_symbol, []).append(
                    int(number.group())
                )

    gear_ratio_sum = 0
    for _, numbers in symbol_coordinates_to_numbers.items():
        if len(numbers) != 2:
            continue
        num1, num2 = numbers
        gear_ratio_sum += num1 * num2

    return gear_ratio_sum


print("Part 1:", part1(INPUT_FILE))
print("Part 2:", part2(INPUT_FILE))
