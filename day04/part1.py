import os
import math


def main():
    res = 0
    input = os.path.join(os.path.dirname(__file__), "input.txt")
    f = open(input, "r")
    for card in f:
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
                curr_number = 0
            else:
                curr_number = (curr_number * 10) + int(y)
        res += math.floor(2 ** (count - 1))

    print(res)
    return res


main()
