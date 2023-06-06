n = int(input())
mas = list(map(str, input().strip().split()))
c = 1
while c != 0:
    c = 0
    for i in range(len(mas) - 1):
        if int(mas[i] + mas[i+1]) < int(mas[i+1] + mas[i]):
            temp = mas[i]
            mas[i] = mas[i+1]
            mas[i+1] = temp
            c += 1
print("".join(map(str, mas)))
