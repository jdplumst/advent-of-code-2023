import os


def main():
    res = 0
    input = os.path.join(os.path.dirname(__file__), "input.txt")
    f = open(input, "r")
    for x in f:
        first, last = 0, 0
        new = (
            x.replace("one", "o1e")
            .replace("two", "t2o")
            .replace("three", "t3e")
            .replace("four", "f4r")
            .replace("five", "f5e")
            .replace("six", "s6x")
            .replace("seven", "s7n")
            .replace("eight", "e8t")
            .replace("nine", "n9e")
        )
        for c in new:
            if c.isnumeric():
                first = c
                break
        for c in reversed(new):
            if c.isnumeric():
                last = c
                break
        res += int(first + last)
    print(res)
    return res


main()
