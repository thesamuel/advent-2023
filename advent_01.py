# Day 1: Trebuchet?!

import re
from typing import Iterable

INPUT_FILE = "inputs/01-input.txt"


def read_digits(input_path: str, digit_regex: str) -> Iterable[int]:
    start_regex = f"({digit_regex})"
    end_regex = f".*({digit_regex}).*$"
    with open(input_path) as f:
        for line in f:
            start = re.search(start_regex, line).group(1)
            end = re.search(end_regex, line).group(1)
            # Uncomment to print debug lines:
            # print(line.rstrip(), "->", start, end)
            yield start, end


def part1(input_path: str) -> int:
    return sum(int(start + end) for start, end in read_digits(input_path, r"[0-9]"))


def part2(input_path: str) -> int:
    number_words = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    def convert_to_int(s: str) -> int:
        return number_words.get(s) or int(s)

    digit_regex = "|".join(number_words) + "|[0-9]"
    return sum(
        convert_to_int(start) * 10 + convert_to_int(end)
        for start, end in read_digits(input_path, digit_regex)
    )


print("Part 1:", part1(INPUT_FILE))
print("Part 2:", part2(INPUT_FILE))
