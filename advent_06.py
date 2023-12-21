import re
from math import sqrt, floor, ceil

INPUT_FILE = "inputs/06-input.txt"


def calculate_num_wins_bruteforce(time: int, distance: int) -> int:
    num_wins = 0
    for t in range(time):
        time_remaining = time - t
        t_distance = t * time_remaining
        if t_distance > distance:
            num_wins += 1

    return num_wins


def calculate_num_wins_fast(time: int, distance: int) -> int:
    """
    Let b = time, c = distance: c = bx - x^2
    Becomes: x^2 - bx + c = 0

    Using the quadratic formula, find the two x-intercepts to the parabolic equation.
    """
    a = 1  # Just here to make things easier to read
    b = -time
    c = distance

    determinant = b**2 - 4 * a * c
    x1 = (-b - sqrt(determinant)) / 2 * a
    x2 = (-b + sqrt(determinant)) / 2 * a

    # Return the distance between discrete "button hold" times
    return floor(x2) - ceil(x1) + 1


def part1(input_file: str) -> int:
    with open(input_file) as f:

        def read_ints() -> list[int]:
            return [int(x) for x in f.readline().split()[1:]]

        times = read_ints()
        distances = read_ints()
        assert len(times) == len(distances)

    total_wins = 1
    for time, distance in zip(times, distances):
        total_wins *= calculate_num_wins_fast(time, distance)

    return total_wins


def part2(input_file: str) -> int:
    with open(input_file) as f:

        def read_int() -> int:
            # Ignore "kerning" on the line and join all ints
            return int("".join(re.findall("[0-9]+", f.readline())))

        time = read_int()
        distance = read_int()

    return calculate_num_wins_fast(time, distance)


print("Part 1:", part1(INPUT_FILE))
print("Part 2:", part2(INPUT_FILE))
