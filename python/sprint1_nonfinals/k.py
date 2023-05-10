from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    l = ''
    for i in number_list:
        l += str(i)
    l = int(l)
    x = l + k
    x = str(x)
    x = list(x)
    return x


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
