import re
from itertools import cycle

INPUT_FILE = "inputs/08-input.txt"
SAMPLE_1_FILE = "inputs/08-sample-1.txt"
SAMPLE_2_FILE = "inputs/08-sample-2.txt"


def read_map(input_file: str) -> tuple[str, dict[str, tuple[str, str]]]:
    with open(input_file) as f:
        instructions = f.readline().rstrip()

        network = {}
        for line in f:
            match = re.match(r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)", line)
            if not match:
                continue

            node, left, right = match.groups()
            network[node] = (left, right)

    return instructions, network


def part1(input_file: str) -> int:
    instructions, network = read_map(input_file)

    curr = "AAA"
    for i, inst in enumerate(cycle(instructions)):
        if curr == "ZZZ":
            return i

        next_nodes = network[curr]
        if inst == "L":
            curr = next_nodes[0]
        else:
            assert inst == "R"
            curr = next_nodes[1]

    return -1


def test_part1_sample1():
    assert part1(SAMPLE_1_FILE) == 2


def test_part1_sample2():
    assert part1(SAMPLE_2_FILE) == 6


def test_part1_input():
    assert part1(INPUT_FILE) == 18023


if __name__ == "__main__":
    print("Part 1:", part1(INPUT_FILE))
