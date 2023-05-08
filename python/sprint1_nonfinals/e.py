def get_longest_word(line: str) -> str:
    result = ''
    temp = ''
    for i in range(len(line)):
        if line[i] != ' ':
            temp += line[i]
        else:
            if len(temp) > len(result):
                result = temp
            temp = ''
    if len(temp) > len(result):
        result = temp
    return result


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
