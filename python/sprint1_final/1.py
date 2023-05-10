# номер решения
from typing import List


def street_map(street: List[int]) -> List[int]:
    length = len(street)
    result = [None]*length
    count = 0
    for i in range(length):
        if street[i] == 0:
            result[i] = 0
            count = 1
        elif count != 0:
            result[i] = count
            count += 1
    for i in reversed(range(length)):
        if street[i] == 0:
            count = 1
        elif count < result[i]:
            result[i] = count
            count += 1
    return result


def read_input() -> List[int]:
    _ = input()
    street = list(map(int, input().strip().split()))
    return street


street = read_input()
print(" ".join(map(str, street_map(street))))
