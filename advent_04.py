# Day 4: Scratchcards
from collections import deque

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


def part2(input_file: str) -> int:
    card_winnings = []
    with open(input_file) as f:
        for line in f:
            winning, have = line.rstrip().split(":")[1].split("|")
            num_winning = calculate_num_winning(parse_ints(winning), parse_ints(have))
            card_winnings.append(num_winning)

    q = deque(list(range(len(card_winnings))))

    total_cards = 0
    while q:
        i = q.popleft()
        num_winning = card_winnings[i]
        if num_winning:
            added_cards = list(range(i + 1, i + num_winning + 1))
            q.extend(added_cards)
        total_cards += 1

    return total_cards


print("Part 1:", part1(INPUT_FILE))
print("Part 2:", part2(INPUT_FILE))
