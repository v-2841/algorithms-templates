n = int(input())
factors = list(map(int, input().strip().split()))
m = int(input())
sizes = list(map(int, input().strip().split()))

# n = 10
# factors = [8, 5, 5, 8, 6, 9, 8, 2, 4, 7]
# m = 8
# sizes = [9, 8, 1, 1, 1, 5, 10, 8]
happy = 0
factors.sort()
sizes.sort()
for pk, val in enumerate(factors):
    if val > sizes[-1]:
        factors = factors[:pk]
        break
for pk, val in enumerate(sizes):
    if val >= factors[0]:
        sizes = sizes[pk:]
        break
while factors and sizes:
    i = j = 0
    while i < len(factors) and j < len(sizes):
        if factors[i] == sizes[j]:
            happy += 1
            factors.pop(i)
            sizes.pop(j)
        elif factors[i] > sizes[j]:
            j += 1
        elif sizes[j] > factors[i]:
            i += 1
    for i in range(len(factors)):
        factors[i] += 1
print(happy)
