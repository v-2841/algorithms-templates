def to_binary(number: int) -> str:
    if number == 0:
        return '0'
    result = ''
    while number > 0:
        if number % 2 == 0:
            result = '0'+result
        else:
            result = '1'+result
        number = int(number/2)
    return result


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
