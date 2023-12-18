import os
from collections import deque


# Updates matrix using queue (BFS)
def updateMatrix(row, col, orig_matrix, matrix, value):
    if row < 0 or row >= len(orig_matrix) or col < 0 or col >= len(orig_matrix[0]):
        return

    if matrix[row][col] != -1:
        return

    q = deque()
    q.append((row, col, value))

    while len(q) > 0:
        cell = q.popleft()
        x, y, v = cell[0], cell[1], cell[2]

        if x < 0 or x >= len(orig_matrix) or y < 0 or y >= len(orig_matrix[0]):
            continue

        if matrix[x][y] != -1:
            continue

        matrix[x][y] = v

        if orig_matrix[x][y] == "|":
            q.append((x - 1, y, v + 1))
            q.append((x + 1, y, v + 1))
        elif orig_matrix[x][y] == "-":
            q.append((x, y - 1, v + 1))
            q.append((x, y + 1, v + 1))
        elif orig_matrix[x][y] == "L":
            q.append((x - 1, y, v + 1))
            q.append((x, y + 1, v + 1))
        elif orig_matrix[x][y] == "J":
            q.append((x - 1, y, v + 1))
            q.append((x, y - 1, v + 1))
        elif orig_matrix[x][y] == "7":
            q.append((x + 1, y, v + 1))
            q.append((x, y - 1, v + 1))
        elif orig_matrix[x][y] == "F":
            q.append((x + 1, y, v + 1))
            q.append((x, y + 1, v + 1))
        elif orig_matrix[x][y] == "S":
            if (
                orig_matrix[x - 1][y] == "|"
                or orig_matrix[x - 1][y] == "7"
                or orig_matrix[x - 1][y] == "F"
            ):
                q.append((x - 1, y, v + 1))
            if (
                orig_matrix[x][y + 1] == "-"
                or orig_matrix[x][y + 1] == "J"
                or orig_matrix[x][y + 1] == "7"
            ):
                q.append((x, y + 1, v + 1))
            if (
                orig_matrix[x + 1][y] == "|"
                or orig_matrix[x + 1][y] == "L"
                or orig_matrix[x + 1][y] == "J"
            ):
                q.append((x + 1, y, v + 1))
            if (
                orig_matrix[x][y - 1] == "-"
                or orig_matrix[x][y - 1] == "L"
                or orig_matrix[x][y - 1] == "F"
            ):
                q.append((x, y - 1, v + 1))


def main():
    orig_matrix = []
    input = os.path.join(os.path.dirname(__file__), "input.txt")
    f = open(input, "r")
    for line in f:
        orig_matrix.append(list(line.rstrip()))

    matrix = [[-1 for i in range(len(orig_matrix[0]))] for j in range(len(orig_matrix))]
    for x in range(len(orig_matrix)):
        for y in range(len(orig_matrix[0])):
            if orig_matrix[x][y] == "S":
                updateMatrix(x, y, orig_matrix, matrix, 0)

    res = max(map(max, matrix))

    print(res)
    return res


main()
