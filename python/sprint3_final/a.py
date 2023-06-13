# 88161621
def broken_search(nums, target) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_num = nums[mid]
        if target == nums[mid]:
            return mid
        if mid_num <= nums[right]:
            if mid_num < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left] <= target < mid_num:
                right = mid - 1
            else:
                left = mid + 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
