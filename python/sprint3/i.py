n = int(input())
members = list(map(int, input().strip().split()))
k = int(input())
un = {}
for i in members:
    if i not in un:
        un[i] = -1
    else:
        un[i] -= 1
un = dict(sorted(un.items(), key=lambda item: item[1]))
print(" ".join(map(str, list(un.keys())[:k])))
