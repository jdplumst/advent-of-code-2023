import os
import math


def main():
    wins_list = []
    input = os.path.join(os.path.dirname(__file__), "input.txt")
    f = open(input, "r")
    total_time = int("".join(c for c in f.readline() if c.isdigit()))
    total_distance = int("".join(c for c in f.readline() if c.isdigit()))
    speed = 0
    wins = 0
    for j in range(total_time + 1):
        distance = speed * (total_time - j)
        if distance > total_distance:
            wins += 1
        speed += 1
    wins_list.append(wins)

    res = math.prod(wins_list)
    print(res)
    return res


main()
