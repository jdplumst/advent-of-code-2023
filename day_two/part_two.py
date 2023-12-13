import os


def main():
    res = 0
    input = os.path.join(os.path.dirname(__file__), "input.txt")
    f = open(input, "r")
    for game in f:
        left, right = game.split(": ")
        red, green, blue = 0, 0, 0
        for handful in right.split("; "):
            for pair in handful.split(", "):
                count, colour = pair.split(" ")
                if colour.startswith("r"):
                    red = max(red, int(count))
                elif colour.startswith("g"):
                    green = max(green, int(count))
                elif colour.startswith("b"):
                    blue = max(blue, int(count))
        res += red * green * blue
    print(res)
    return res


main()
