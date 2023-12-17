import os

ORDER = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
PRIORITIES = {c: index for index, c in enumerate(ORDER)}


def main():
    # Lists based on each type of hand
    ordered_five = []
    ordered_four = []
    ordered_full = []
    ordered_three = []
    ordered_two = []
    ordered_one = []
    ordered_high = []

    # Hashmap mapping each hand to its bid
    hand_to_bid = {}

    input = os.path.join(os.path.dirname(__file__), "input.txt")
    f = open(input, "r")
    for line in f:
        hand, bid = line.split(" ")
        hand_to_bid[hand] = int(bid)
        sorted_hand = sorted(hand)
        card_count = {}
        for c in sorted_hand:
            card_count[c] = card_count.get(c, 0) + 1
        distinct_cards = len(dict.keys(card_count))
        if distinct_cards == 1:
            ordered_five.append(hand)
        elif distinct_cards == 2 and 1 in card_count.values():
            ordered_four.append(hand)
        elif distinct_cards == 2:
            ordered_full.append(hand)
        elif distinct_cards == 3 and 3 in card_count.values():
            ordered_three.append(hand)
        elif distinct_cards == 3:
            ordered_two.append(hand)
        elif distinct_cards == 4:
            ordered_one.append(hand)
        else:
            ordered_high.append(hand)

    # Sort each list based on custom sorting order
    ordered_five.sort(key=lambda x: tuple(map(lambda y: PRIORITIES[y], x)))
    ordered_four.sort(key=lambda x: tuple(map(lambda y: PRIORITIES[y], x)))
    ordered_full.sort(key=lambda x: tuple(map(lambda y: PRIORITIES[y], x)))
    ordered_three.sort(key=lambda x: tuple(map(lambda y: PRIORITIES[y], x)))
    ordered_two.sort(key=lambda x: tuple(map(lambda y: PRIORITIES[y], x)))
    ordered_one.sort(key=lambda x: tuple(map(lambda y: PRIORITIES[y], x)))
    ordered_high.sort(key=lambda x: tuple(map(lambda y: PRIORITIES[y], x)))

    # Combine the lists
    full_list = (
        ordered_high
        + ordered_one
        + ordered_two
        + ordered_three
        + ordered_full
        + ordered_four
        + ordered_five
    )

    res = 0
    for x in range(len(full_list)):
        res += hand_to_bid[full_list[x]] * (x + 1)
    print(res)
    return res


main()
