import os


def main():
    input = os.path.join(os.path.dirname(__file__), "input.txt")
    num_lines = len(open(input, "r").readlines())

    # Store the number of copies for each card at index card_number - 1
    copies = [1] * num_lines

    f = open(input, "r")
    card_number = 0

    for card in f:
        card_number += 1
        card, numbers = card.split(": ")
        winning_nums, my_nums = numbers.split("|")
        curr_number = 0
        winning_nums_list = []

        for x in winning_nums:
            if not x.isdigit():
                winning_nums_list.append(curr_number)
                curr_number = 0
            else:
                curr_number = (curr_number * 10) + int(x)

        curr_number = 0
        count = 0

        for y in my_nums:
            if not y.isdigit():
                if curr_number != 0 and curr_number in winning_nums_list:
                    count += 1
                    copies[card_number - 1 + count] += copies[card_number - 1]
                curr_number = 0
            else:
                curr_number = (curr_number * 10) + int(y)

        res = sum(copies)

    print(res)
    return res


main()
