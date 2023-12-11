import math
from bisect import bisect_left, bisect_right
from typing import TextIO, Iterable

INPUT_FILE = "inputs/05-input.txt"


def read_seeds(f: TextIO) -> list[int]:
    first_line = f.readline()
    assert first_line.startswith("seeds:")
    return [int(seed) for seed in first_line.split(":")[1].split()]


def read_mappings(f: TextIO) -> Iterable[list[tuple[int, int, int]]]:
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

        yield mapping


def part_1(input_file: str) -> int:
    with open(input_file) as f:
        seeds = read_seeds(f)
        print("Seeds:", seeds)

        mappings = list(read_mappings(f))
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


def truncate_mapping(
    src: tuple[int, int],
    mapping: list[tuple[int, int, int]],
) -> list[tuple[int, int, int]]:
    src_start, src_end = src[0], src[0] + src[1]

    new_mapping = []
    for src_map_start, dest_start, length in mapping:
        if src_map_start < src_start:
            offset = src_start - src_map_start
            if offset >= length:
                # Skip this mapping instance, it's out of range
                continue
            src_map_start += offset
            dest_start += offset
            length -= offset

        src_map_end = src_map_start + length
        if src_map_end > src_end:
            offset = src_map_end - src_end
            if offset > length:
                continue
            length -= offset

        new_mapping.append((src_map_start, dest_start, length))

    return new_mapping


def fill_mapping(
    src: tuple[int, int],
    mapping: list[tuple[int, int, int]],
) -> list[tuple[int, int, int]]:
    if not mapping:
        return [(src[0], src[0], src[1])]

    mapping_filled = []

    # Fill gaps (first case)
    src_start = src[0]
    initial_mapping_start = mapping[0][0]
    if src_start < initial_mapping_start:
        mapping_filled.append((src_start, src_start, initial_mapping_start - src_start))

    # Fill gaps (general case)
    for i in range(len(mapping)):
        m1 = mapping[i]
        mapping_filled.append(m1)

        if i < len(mapping) - 1:
            fill_end, _, _ = mapping[i + 1]
        else:
            fill_end = src[0] + src[1]

        m1_end = m1[0] + m1[2]
        if m1_end < fill_end:
            mapping_filled.append((m1_end, m1_end, fill_end - m1_end))

    return mapping_filled


def get_dest_ranges(
    src: tuple[int, int],
    mapping: list[tuple[int, int, int]],
) -> list[tuple[int, int]]:
    mapping = truncate_mapping(src, mapping)
    mapping = fill_mapping(src, mapping)

    # Return destination map
    return [(m[1], m[2]) for m in mapping]


def part_2(input_file: str) -> int:
    with open(input_file) as f:
        seeds = read_seeds(f)
        seeds = list(zip(seeds[0::2], seeds[1::2]))
        print("Seeds:", seeds)

        mappings = list(read_mappings(f))
        print("Mappings:", mappings)

    print("Navigating ranges...")
    min_location = math.inf
    for seed in seeds:
        print("Processing seed:", seed)
        srcs = [seed]
        for mapping in mappings:
            print("Processing mapping:", mapping)
            new_srcs = []
            for src in srcs:
                new_srcs.extend(get_dest_ranges(src, mapping))
                print("----> Extending new srcs:", new_srcs)
            srcs = new_srcs
            print("--> Finished processing mapping:", srcs)

        # Take the min of the location ranges
        min_location_for_seed = min(srcs, key=lambda x: x[0], default=math.inf)[0]
        print(f"Min location for seed {seed}:", min_location_for_seed)
        min_location = min(min_location, min_location_for_seed)

        print("---------------------------------")

    return min_location


print("Part 1:", part_1(INPUT_FILE))
print()
print("Part 2:", part_2(INPUT_FILE))
