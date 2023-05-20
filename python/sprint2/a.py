from typing import List, Tuple


def transp(matrix, n, m):
    result = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][i] = matrix[i][j]
    return result


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    return matrix, n, m


matrix, n, m = read_input()
result = transp(matrix, n, m)
for i in range(len(result)):
    print(" ".join(map(str, result[i])))
