import os
import math


def main():
    input = os.path.join(os.path.dirname(__file__), "input.txt")
    f = open(input, "r")
    directions = f.readline()[:-1]
    f.readline()

    nodes = {}
    curr_nodes = []
    for line in f:
        node, paths = line.split(" = ")
        nodes[node] = tuple(paths.rstrip()[1:-1].split(", "))
        if node.endswith("A"):
            curr_nodes.append(node)
    steps = 0
    min_paths = {}
    while True:
        for d in directions:
            if d == "L":
                for x in range(len(curr_nodes)):
                    curr_nodes[x] = nodes[curr_nodes[x]][0]
            else:
                for x in range(len(curr_nodes)):
                    curr_nodes[x] = nodes[curr_nodes[x]][1]
            steps += 1
            for x in curr_nodes:
                if x.endswith("Z"):
                    min_paths[x] = steps
                    curr_nodes.remove(x)
            if len(curr_nodes) == 0:
                res = math.lcm(*min_paths.values())
                print(res)
                return res


main()
