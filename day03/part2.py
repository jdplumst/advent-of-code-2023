import os


# Returns True if item at index is adjacent to exactly 2 numbers
def isGear(top_line, mid_line, bot_line, index):
    # Index 0 (leftmost position)
    if index != 0:
        if top_line:
            top_left = top_line[index - 1].isdigit() and not top_line[index].isdigit()
        else:
            top_left = False
        left = mid_line[index - 1].isdigit()
        if bot_line:
            bot_left = bot_line[index - 1].isdigit() and not bot_line[index].isdigit()
        else:
            bot_left = False
    else:
        top_left = False
        left = False
        bot_left = False

    if top_line:
        top = top_line[index].isdigit()
        top_right = top_line[index + 1].isdigit() and not top_line[index].isdigit()
    else:
        top = False
        top_right = False
    right = mid_line[index + 1].isdigit()
    if bot_line:
        bot = bot_line[index].isdigit()
        bot_right = bot_line[index + 1].isdigit() and not bot_line[index].isdigit()

    else:
        bot = False
        bot_right = False

    return sum([top_left, top, top_right, left, right, bot_left, bot, bot_right]) == 2


# Gets whole number located at index by searching both left and right of it
def getNumber(line, index):
    res = ""
    for i in range(index, -1, -1):
        if line[i].isdigit():
            res += line[i]
        else:
            break
    res = res[::-1]
    for j in range(index + 1, len(line), 1):
        if line[j].isdigit():
            res += line[j]
        else:
            break
    return int(res)


def main():
    res = 0
    input = os.path.join(os.path.dirname(__file__), "input.txt")
    f = open(input, "r")
    line1 = None
    line2 = None
    line3 = f.readline()
    adjacent = False
    curr_number = 0
    counter = 0
    while True:
        counter += 1
        adjacent = False
        curr_number = 0
        line1 = line2
        line2 = line3
        line3 = f.readline()
        if not line2:
            break
        for c in range(len(line2)):
            part_numbers = []
            if not line2[c].isdigit() and line2[c] != "." and line2[c] != "\n":
                if isGear(line1, line2, line3, c):
                    if line1 and line1[c - 1].isdigit() and not line1[c].isdigit():
                        part_numbers.append(getNumber(line1, c - 1))
                    if line1 and line1[c].isdigit() and not line1[c + 1].isdigit():
                        part_numbers.append(getNumber(line1, c))
                    if line1 and line1[c + 1].isdigit():
                        part_numbers.append(getNumber(line1, c + 1))
                    if line2[c - 1].isdigit():
                        part_numbers.append(getNumber(line2, c - 1))
                    if line2[c + 1].isdigit():
                        part_numbers.append(getNumber(line2, c + 1))
                    if line3 and line3[c - 1].isdigit() and not line3[c].isdigit():
                        part_numbers.append(getNumber(line3, c - 1))
                    if line3 and line3[c].isdigit() and not line3[c + 1].isdigit():
                        part_numbers.append(getNumber(line3, c))
                    if line3 and line3[c + 1].isdigit():
                        part_numbers.append(getNumber(line3, c + 1))
                    gear_ratio = part_numbers[0] * part_numbers[1]
                    res += gear_ratio
    print(res)
    return res


main()
