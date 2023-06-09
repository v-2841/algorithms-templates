n = int(input())
mas = list(map(int, input().strip().split()))
count = [0]*3
for val in mas:
    count[val] += 1
mas = [0]*count[0]+[1]*count[1]+[2]*count[2]
print(" ".join(map(str, mas)))
