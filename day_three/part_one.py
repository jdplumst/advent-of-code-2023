import os


# Returns true if item at index is adjacent to a symbol
def isAdjacent(top_line, mid_line, bot_line, index):
    # Index 0 (leftmost position)
    if index != 0:
        if top_line:
            top_left = not top_line[index - 1].isdigit() and top_line[index - 1] != "."
        else:
            top_left = False
        left = not mid_line[index - 1].isdigit() and mid_line[index - 1] != "."
        if bot_line:
            bot_left = not bot_line[index - 1].isdigit() and bot_line[index - 1] != "."
        else:
            bot_left = False
    else:
        top_left = False
        left = False
        bot_left = False

    if top_line:
        top = not top_line[index].isdigit() and top_line[index] != "."
        top_right = (
            not top_line[index + 1].isdigit()
            and top_line[index + 1] != "."
            and top_line[index + 1] != "\n"
        )
    else:
        top = False
        top_right = False
    right = (
        not mid_line[index + 1].isdigit()
        and mid_line[index + 1] != "."
        and mid_line[index + 1] != "\n"
    )
    if bot_line:
        bot = not bot_line[index].isdigit() and bot_line[index] != "."
        bot_right = (
            not bot_line[index + 1].isdigit()
            and bot_line[index + 1] != "."
            and bot_line[index + 1] != "\n"
        )
    else:
        bot = False
        bot_right = False

    return top_left or top or top_right or left or right or bot_left or bot or bot_right


def main():
    res = 0
    input = os.path.join(os.path.dirname(__file__), "input.txt")
    f = open(input, "r")
    line1 = None
    line2 = None
    line3 = f.readline()
    adjacent = False
    curr_number = 0
    while True:
        adjacent = False
        curr_number = 0
        line1 = line2
        line2 = line3
        line3 = f.readline()
        if not line2:
            break
        for c in range(len(line2)):
            if not line2[c].isdigit() and line2[c - 1].isdigit() and adjacent:
                res += curr_number
                curr_number = 0
                adjacent = False
            elif not line2[c].isdigit():
                curr_number = 0
                adjacent = False
            elif line2[c].isdigit():
                curr_number = (curr_number * 10) + int(line2[c])
                if isAdjacent(line1, line2, line3, c):
                    adjacent = True
    print(res)
    return res


main()
