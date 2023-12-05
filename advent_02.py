color_limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

INPUT_FILE = "inputs/02-input.txt"


def is_round_possible(round: str) -> bool:
    for color_count in round.split(", "):
        count, color = color_count.split()
        if int(count) > color_limits[color]:
            return False

    return True


def part1(input_file: str) -> int:
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


print("Part 1:", part1(INPUT_FILE))
