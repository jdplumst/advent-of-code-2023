import os


# Gets the difference between each consecutive number in a list
# and returns new list with these differences
def diff(l):
    res = []
    for x in range(len(l) - 1):
        res.append(l[x + 1] - l[x])
    return res


def main():
    res = 0
    input = os.path.join(os.path.dirname(__file__), "input.txt")
    f = open(input, "r")
    for line in f:
        history = [int(c) for c in line.rstrip().split(" ")]
        total = [history]
        seq = diff(history)
        while not all(v == 0 for v in seq):
            total.append(seq)
            seq = diff(seq)
        seq.insert(0, 0)
        for x in reversed(total):
            x.insert(0, x[0] - seq[0])
            seq = x
        res += total[0][0]

    print(res)
    return res


main()
