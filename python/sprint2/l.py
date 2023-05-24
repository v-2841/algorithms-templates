n, lim = (int(i) for i in input().split())
lim = 10**lim
if n == 0 or n == 1:
    print('1')
else:
    sum = [0, 1]
    while n:
        n -= 1
        temp = sum[0] + sum[1]
        sum[0] = sum[1]
        sum[1] = temp % lim
    sum[1] = str(sum[1])
    lim = str(lim)
    while len(lim)-1 != len(sum[1]):
        sum[1] = '0'+sum[1]
    print(sum[1])
