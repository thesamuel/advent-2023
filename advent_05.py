import math
from bisect import bisect_left, bisect_right
from typing import TextIO

INPUT_FILE = "inputs/05-input.txt"


# From: https://docs.python.org/3.11/library/bisect.html#searching-sorted-lists
def find_range(a: list[tuple[int]], x, key):
    """Find leftmost item greater than or equal to x"""
    i = bisect_left(a, x, key=key)
    if i != len(a):
        return a[i]
    raise ValueError


def parse_seeds(f: TextIO) -> list[int]:
    first_line = f.readline()
    assert first_line.startswith("seeds:")
    return [int(seed) for seed in first_line.split(":")[1].split()]


def parse_mappings(f: TextIO) -> list[list[tuple[int, int, int]]]:
    mappings = []

    # Read until EOF, building mappings
    while line := f.readline():
        line = line.rstrip()
        if not line:
            continue

        assert "map" in line
        # print(f"Processing mapping for {line}")

        # Process mapping
        mapping = []
        while line := f.readline().rstrip():
            # Note that we swap the src and dest to make it easier to understand
            dest, src, length = [int(num) for num in line.split()]
            mapping.append((src, dest, length))

        # Sort mapping by src
        mapping.sort(key=lambda x: x[0])
        # print(mapping)

        mappings.append(mapping)

    return mappings


def part1(input_file: str) -> int:
    with open(input_file) as f:
        seeds = parse_seeds(f)
        print("Seeds:", seeds)

        mappings = parse_mappings(f)
        print("Mappings:", mappings)

    min_location = math.inf
    for seed in seeds:
        path = [seed]
        src = seed
        for mapping in mappings:
            # TODO: Bisect to the correct mapping (associated to src) and update src to dst
            # TODO: use the destination as the next source

            i = bisect_right(mapping, src, key=lambda x: x[0])
            if not i:
                path.append(src)
                continue

            src_start, dest_start, length = mapping[i - 1]
            if src >= src_start + length:
                path.append(src)
                continue

            offset = src - src_start
            src = dest_start + offset
            path.append(src)

        min_location = min(src, min_location)
        print(f"Path from seed {seed} to location {src}:", path)

    return min_location


print("Part 1:", part1(INPUT_FILE))
