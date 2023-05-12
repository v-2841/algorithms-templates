from typing import List, Tuple


MATRIX_DIMENSION = 4


def points_counter(clicks: int, matrix: List[List[str]]) -> int:
    nums_counter = [0] * 9
    clicks = clicks * 2
    points = 0
    for row in range(MATRIX_DIMENSION):
        for col in range(MATRIX_DIMENSION):
            if matrix[row][col] != '.':
                nums_counter[int(matrix[row][col])-1] += 1
    for row in range(9):
        if clicks >= nums_counter[row] and nums_counter[row] != 0:
            points += 1
    return points


def read_input() -> Tuple[int, List[List[str]]]:
    clicks = int(input())
    matrix = []
    for _ in range(MATRIX_DIMENSION):
        matrix.append([*input()])
    return clicks, matrix


if __name__ == '__main__':
    clicks, matrix = read_input()
    print(points_counter(clicks, matrix))
