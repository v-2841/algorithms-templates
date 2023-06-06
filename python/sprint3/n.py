n = int(input())
mas = []
for i in range(n):
    mas.append(list(map(int, input().strip().split())))
mas.sort(key=lambda mas: mas[1])
n -= 1
while n > 0:
    if mas[n-1][1] < mas[n][0]:
        n -= 1
    elif mas[n][0] <= mas[n-1][0]:
        mas.pop(n-1)
        n -= 1
    else:
        mas[n][0] = mas[n-1][0]
        mas.pop(n-1)
        n -= 1
for i in range(len(mas)):
    print(" ".join(map(str, mas[i])))
