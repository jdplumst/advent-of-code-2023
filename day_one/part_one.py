import os


def main():
    res = 0
    input = os.path.join(os.path.dirname(__file__), "input.txt")
    f = open(input, "r")
    for x in f:
        first, last = 0, 0
        for c in x:
            if c.isnumeric():
                first = c
                break
        for c in reversed(x):
            if c.isnumeric():
                last = c
                break
        res += int(first + last)
    print(res)
    return res


main()
