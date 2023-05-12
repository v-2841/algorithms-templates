from typing import List


def distances_to_0(arrow: List[int]) -> List[int]:
    result = [None] * len(arrow)
    count = 0
    for pos, val in enumerate(arrow):
        if val == 0:
            result[pos] = 0
            count = 1
        elif count != 0:
            result[pos] = count
            count += 1
    for pos, val in reversed(list(enumerate(arrow))):
        if val == 0:
            count = 1
        elif result[pos] is None:
            result[pos] = count
            count += 1
        elif count < result[pos]:
            result[pos] = count
            count += 1
    return result


def read_input() -> List[int]:
    _ = input()
    return [int(num) for num in input().split()]


if __name__ == '__main__':
    print(*distances_to_0(read_input()), sep=' ', end='')
