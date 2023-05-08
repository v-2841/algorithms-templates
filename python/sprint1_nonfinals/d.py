from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    result = 0
    num = len(temperatures)
    if num == 1:
        return 1
    if num == 2:
        if temperatures[0] == temperatures[1]:
            return 0
        return 1
    if temperatures[0] > temperatures[1]:
        result += 1
    if temperatures[num-1] > temperatures[num-2]:
        result += 1
    for i in range(1, num-1):
        if temperatures[i-1] < temperatures[i] > temperatures[i+1]:
            result += 1
    return result


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
