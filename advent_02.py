INPUT_FILE = "inputs/02-input.txt"


def part1(input_file: str) -> int:
    color_limits = {"red": 12, "green": 13, "blue": 14}

    def is_round_possible(round: str) -> bool:
        for color_count in round.split(", "):
            count, color = color_count.split()
            if int(count) > color_limits[color]:
                return False

        return True

    possible_game_id_sum = 0
    with open(input_file) as f:
        for i, line in enumerate(f):
            game_id = i + 1
            game = line.split(": ")[1]
            is_game_possible = True
            for game_round in game.split("; "):
                if not is_round_possible(game_round):
                    is_game_possible = False
                    break
            if is_game_possible:
                possible_game_id_sum += game_id
    return possible_game_id_sum


def part2(input_file: str) -> int:
    def merge_max(dicts) -> dict:
        out = {}
        for d in dicts:
            for k in d:
                if k in out:
                    out[k] = max(out[k], d[k])
                else:
                    out[k] = d[k]
        return out

    power_sum = 0
    with open(input_file) as f:
        for i, line in enumerate(f):
            game = line.split(": ")[1]
            round_dicts = [
                {
                    color: int(count)
                    for count, color in [
                        color_count.split() for color_count in game_round.split(", ")
                    ]
                }
                for game_round in game.split("; ")
            ]
            color_maxes = merge_max(round_dicts)
            power = 1
            for value in color_maxes.values():
                power *= value
            power_sum += power

    return power_sum


print("Part 1:", part1(INPUT_FILE))
print("Part 2:", part2(INPUT_FILE))
