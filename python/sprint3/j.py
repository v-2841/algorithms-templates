n = int(input())
mas = list(map(int, input().strip().split()))
c = 1
if all(mas[i] <= mas[i+1] for i in range(len(mas) - 1)):
    print(" ".join(map(str, mas)))
else:
    while c != 0:
        c = 0
        for i in range(len(mas)-1):
            if mas[i] > mas[i+1]:
                temp = mas[i]
                mas[i] = mas[i+1]
                mas[i+1] = temp
                c += 1
        if c != 0:
            print(" ".join(map(str, mas)))
