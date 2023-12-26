from collections import Counter
from typing import Iterable

INPUT_FILE = "inputs/07-input.txt"
CARDS_RANKED = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def card_to_int(s: str) -> int:
    return CARDS_RANKED.index(s)


def get_rank(hand: str) -> int:
    counts = Counter(hand)
    card_strengths = [CARDS_RANKED.index(card) for card in hand]

    if 5 in counts.values():
        type_rank = 0
    elif 4 in counts.values():
        type_rank = 1
    elif 3 in counts.values() and 2 in counts.values():
        type_rank = 2
    elif 3 in counts.values():
        type_rank = 3
    elif num_pairs := sum(1 for x in counts.values() if x == 2):
        if num_pairs == 2:
            type_rank = 4
        else:
            type_rank = 5
    else:
        type_rank = 6

    card_order_rank = 0
    for i, card_strength in enumerate(reversed(card_strengths)):
        card_order_rank += card_strength * (10 ** (i * 2))

    return type_rank * (10**10) + card_order_rank


def read_hands(input_file: str) -> Iterable[tuple[str, int]]:
    with open(input_file) as f:
        for line in f:
            hand, bid = line.split()
            yield hand, int(bid)


def part1(input_file: str):
    ranked_hands = sorted(
        read_hands(input_file), key=lambda x: get_rank(x[0]), reverse=True
    )

    # Return sum of bids, multiplied by 1-indexed rank
    return sum(bid * (i + 1) for i, (hand, bid) in enumerate(ranked_hands))


print("Part 1:", part1(INPUT_FILE))
