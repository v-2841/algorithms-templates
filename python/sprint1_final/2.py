from typing import List, Tuple


def points_counter(k: int, matrix: List[List[str]]) -> int:
    nums_counter = [0]*9
    k = k*2
    result = 0
    for i in range(4):
        for j in range(4):
            if matrix[i][j] != '.':
                nums_counter[int(matrix[i][j])-1] += 1
    for i in range(9):
        if k >= nums_counter[i] and nums_counter[i] != 0:
            result += 1
    return result


def read_input() -> Tuple[int, List[List[str]]]:
    k = int(input())
    matrix = []
    for _ in range(4):
        matrix.append(list(map(str, [*input().strip()])))
    return k, matrix


k, matrix = read_input()
print(points_counter(k, matrix))
