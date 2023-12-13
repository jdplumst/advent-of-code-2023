import os


def main():
    res = 0
    input = os.path.join(os.path.dirname(__file__), "input.txt")
    f = open(input, "r")
    for game in f:
        left, right = game.split(": ")
        game_id = int("".join(c for c in left if c.isdigit()))
        possible = True
        for handful in right.split("; "):
            for pair in handful.split(", "):
                count, colour = pair.split(" ")
                if colour.startswith("r") and int(count) > 12:
                    possible = False
                elif colour.startswith("g") and int(count) > 13:
                    possible = False
                elif colour.startswith("b") and int(count) > 14:
                    possible = False
        if possible:
            res += game_id
    print(res)
    return res


main()
