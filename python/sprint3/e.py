n, k = list(map(int, input().strip().split()))
houses = list(map(int, input().strip().split()))
houses.sort()
sum = 0
counter = 0
for i in range(n):
    if houses[i] + sum > k:
        break
    sum += houses[i]
    counter += 1
print(counter)
