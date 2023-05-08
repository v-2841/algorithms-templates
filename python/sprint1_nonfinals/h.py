from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    first_number = int(first_number)
    second_number = int(second_number)
    result = first_number + second_number
    result = str(result)
    temp = 0
    for i in reversed(range(len(result))):
        if result[i] == '2' and temp == 0:
            result[i] = '0'
            temp = 1
        elif result[i] == '2' and temp == 1:
            result[i] = '1'
            temp = 1
        elif result[i] == '1' and temp == 1:
            result[i] = '0'
            temp = 1
        elif result[i] == '0' and temp == 1:
            result[i] = '1'
            temp = 0
    if temp == 1:
        result = '1'+result
    return result


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

print(get_sum('100101','1001'))
#first_number, second_number = read_input()
#print(get_sum(first_number, second_number))
