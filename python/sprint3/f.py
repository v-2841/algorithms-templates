import sys

n = int(input())
nums = list(map(int, input().strip().split()))
nums.sort(reverse=True)
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if nums[i] < nums[j] + nums[k]:
                print(nums[i] + nums[j] + nums[k])
                sys.exit()
