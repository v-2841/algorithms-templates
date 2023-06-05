s = list(input())
t = list(input())
sl = 0
sll = len(s)
for i in t:
    if sl < sll and i == s[sl]:
        sl += 1
if sl == sll:
    print(True)
else:
    print(False)
