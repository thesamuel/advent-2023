from collections import Counter
from typing import Iterable

INPUT_FILE = "inputs/07-input.txt"
SAMPLE_FILE = "inputs/07-sample.txt"

CARDS_RANKED_PART_1 = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
CARDS_RANKED_PART_2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def read_hands(input_file: str) -> Iterable[tuple[str, int]]:
    with open(input_file) as f:
        for line in f:
            hand, bid = line.split()
            yield hand, int(bid)


def get_type_rank(counts: Counter) -> int:
    if 5 in counts.values():
        return 0
    elif 4 in counts.values():
        return 1
    elif 3 in counts.values() and 2 in counts.values():
        return 2
    elif 3 in counts.values():
        return 3
    elif num_pairs := sum(1 for x in counts.values() if x == 2):
        if num_pairs == 2:
            return 4
        else:
            return 5
    else:
        return 6


def get_card_order_rank(hand: str, cards_ranked: list[str]) -> int:
    return sum(
        cards_ranked.index(card) * (10 ** (i * 2))
        for i, card in enumerate(reversed(hand))
    )


def part1(input_file: str) -> int:
    def get_rank(hand: str) -> int:
        counts = Counter(hand)
        return get_type_rank(counts) * (10**10) + get_card_order_rank(
            hand, CARDS_RANKED_PART_1
        )

    ranked_hands = sorted(
        read_hands(input_file), key=lambda x: get_rank(x[0]), reverse=True
    )

    # Return sum of bids, multiplied by 1-indexed rank
    return sum(bid * (i + 1) for i, (hand, bid) in enumerate(ranked_hands))


def part2(input_file: str) -> int:
    def replace_jokers(counts: Counter):
        # Since we can use the joker as a wildcard, set it to the most common card
        if joker_count := counts.get("J", 0):
            del counts["J"]
            # Arbitrarily use "A" as the card if all the cards are jokers
            most_common_card, _ = (counts.most_common(1) or [("A", 5)])[0]
            counts[most_common_card] += joker_count

    def get_rank(hand: str) -> int:
        counts = Counter(hand)
        replace_jokers(counts)

        return get_type_rank(counts) * (10**10) + get_card_order_rank(
            hand, CARDS_RANKED_PART_2
        )

    ranked_hands = sorted(
        read_hands(input_file), key=lambda x: get_rank(x[0]), reverse=True
    )

    # Return sum of bids, multiplied by 1-indexed rank
    return sum(bid * (i + 1) for i, (hand, bid) in enumerate(ranked_hands))


def test_part1_sample():
    assert part1(SAMPLE_FILE) == 6440


def test_part2_sample():
    assert part2(SAMPLE_FILE) == 5905


if __name__ == "__main__":
    print("Part 1:", part1(INPUT_FILE))
    print("Part 2:", part2(INPUT_FILE))
