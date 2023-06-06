def binarySearch(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] >= x and arr[mid-1] < x and mid != 0:
        return mid
    elif arr[mid] >= x and mid == 0:
        return mid
    elif x <= arr[mid]:
        return binarySearch(arr, x, left, mid)
    else:
        return binarySearch(arr, x, mid + 1, right)


n = int(input())
arr = list(map(int, input().strip().split()))
x = int(input())
# n = 6
# arr = [1, 1, 4, 4, 4, 4]
# x = 1
day1 = binarySearch(arr, x, left=0, right=len(arr))
day2 = binarySearch(arr, x*2, left=0, right=len(arr))
if day1 != -1:
    day1 += 1
if day2 != -1:
    day2 += 1
print(day1, day2)
