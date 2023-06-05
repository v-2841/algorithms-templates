def check(a):
    a = list(bin(a)[2:])
    one = 0
    for i in a:
        if i == '1':
            one += 1
        elif one > 0:
            one -= 1
        else:
            return False
    return one == 0


n = int(input())
a = 0
for i in reversed(range(n, n*2)):
    a += 2**i
lim = 0
for i in range(1, n*2, 2):
    lim += 2**i
res = []
while a >= lim:
    if check(a):
        res.append(a)
    a -= 2
for i in range(len(res)):
    res[i] = bin(res[i])[2:]
    res[i] = res[i].replace('1', '(')
    res[i] = res[i].replace('0', ')')
    print(res[i])
