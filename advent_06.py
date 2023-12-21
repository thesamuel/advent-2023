INPUT_FILE = "inputs/06-input.txt"


def part1(input_file: str) -> int:
    def read_ints(f) -> list[int]:
        return [int(x) for x in f.readline().split()[1:]]

    with open(input_file) as f:
        times = read_ints(f)
        distances = read_ints(f)
        assert len(times) == len(distances)

    total_wins = 1
    for time, distance in zip(times, distances):
        num_wins = 0
        for t in range(time):
            time_remaining = time - t
            t_distance = t * time_remaining
            # TODO: ties?
            if t_distance > distance:
                num_wins += 1

        total_wins *= num_wins

    return total_wins


print("Part 1:", part1(INPUT_FILE))
