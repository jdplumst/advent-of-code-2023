import os


def main():
    input = os.path.join(os.path.dirname(__file__), "input.txt")
    f = open(input, "r")
    directions = f.readline()[:-1]
    f.readline()

    nodes = {}
    for line in f:
        node, paths = line.split(" = ")
        nodes[node] = tuple(paths[1:-2].split(", "))

    curr_node = "AAA"
    steps = 0
    while True:
        for d in directions:
            if d == "L":
                curr_node = nodes[curr_node][0]
            else:
                curr_node = nodes[curr_node][1]
            steps += 1
            if curr_node == "ZZZ":
                print(steps)
                return steps


main()
