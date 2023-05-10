from typing import List


def factorize(n: int) -> List[int]:
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(int(i))
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(int(n))
    return primfac


result = factorize(int(input()))
print(" ".join(map(str, result)))
