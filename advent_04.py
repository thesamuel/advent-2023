# Day 4: Scratchcards

INPUT_FILE = "inputs/04-input.txt"


def calculate_num_winning(winning: list[int], have: list[int]) -> int:
    winning = set(winning)
    return sum(1 for x in have if x in winning)


def parse_ints(s: str) -> list[int]:
    return [int(x) for x in s.split()]


def part1(input_file: str) -> int:
    points_sum = 0
    with open(input_file) as f:
        for line in f:
            winning, have = line.rstrip().split(":")[1].split("|")
            # print("Winning:", winning, "Have:", have)
            num_winning = calculate_num_winning(parse_ints(winning), parse_ints(have))
            points = (2 ** (num_winning - 1)) if num_winning else 0
            # print("Num winning:", num_winning, "Points:", points)
            points_sum += points

    return points_sum


print("Part 1:", part1(INPUT_FILE))
