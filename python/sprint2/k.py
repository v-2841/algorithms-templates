def fib(x, n):
    if n == 0:
        return x[1]
    else:
        n -= 1
        i = x[0] + x[1]
        x[0] = x[1]
        x[1] = i
        return fib(x, n)


n = int(input())
if n == 0 or n == 1:
    print(1)
else:
    print(fib([0, 1], n))
