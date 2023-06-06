def result(nums, prefix):
    if not nums:
        res.append(prefix)
    else:
        for i in buttons[nums[0]]:
            result(nums[1:], prefix + i)


buttons = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}
nums = list(input().strip())
res = []
s = ''
result(nums, '')
for i in res:
    s += i + ' '
print(s)
