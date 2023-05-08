def is_palindrome(line: str) -> bool:
    line = line.lower()
    left = 0
    right = len(line) - 1
    while left < right:
        if not line[left].isalpha() and not line[left].isdigit():
            left += 1
        elif not line[right].isalpha() and not line[right].isdigit():
            right -= 1
        else:
            if line[left] != line[right]:
                return False
            left += 1
            right -= 1
    return True


print(is_palindrome(input().strip()))
