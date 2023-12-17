import os
import math


def main():
    wins_list = []
    input = os.path.join(os.path.dirname(__file__), "input.txt")
    f = open(input, "r")
    times = f.readline().split()
    distances = f.readline().split()
    for i in range(1, len(times)):
        speed = 0
        wins = 0
        time = int(times[i])
        for j in range(time + 1):
            distance = speed * (time - j)
            if distance > int(distances[i]):
                wins += 1
            speed += 1
        wins_list.append(wins)

    res = math.prod(wins_list)
    print(res)
    return res


main()
