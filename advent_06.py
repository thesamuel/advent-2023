import re

INPUT_FILE = "inputs/06-input.txt"


def calculate_num_wins_bruteforce(time: int, distance: int) -> int:
    # Bruteforce
    num_wins = 0
    for t in range(time):
        time_remaining = time - t
        t_distance = t * time_remaining
        if t_distance > distance:
            num_wins += 1

    return num_wins


def part1(input_file: str) -> int:
    with open(input_file) as f:

        def read_ints() -> list[int]:
            return [int(x) for x in f.readline().split()[1:]]

        times = read_ints()
        distances = read_ints()
        assert len(times) == len(distances)

    total_wins = 1
    for time, distance in zip(times, distances):
        total_wins *= calculate_num_wins_bruteforce(time, distance)

    return total_wins


def part2(input_file: str) -> int:
    with open(input_file) as f:

        def read_int() -> int:
            # Ignore "kerning" on the line and join all ints
            return int("".join(re.findall("[0-9]+", f.readline())))

        time = read_int()
        distance = read_int()

    # Bruteforce
    return calculate_num_wins_bruteforce(time, distance)


print("Part 1:", part1(INPUT_FILE))
print("Part 2:", part2(INPUT_FILE))
