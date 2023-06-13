# 88161556
def effective_quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[-1]
    left, right = 0, len(array) - 1
    while left < right:
        if array[left] <= pivot:
            left += 1
        else:
            array[left], array[right - 1], array[
                right] = array[right - 1], array[right], array[left]
            right -= 1
    return (effective_quicksort(array[:left])
            + effective_quicksort(array[left:]))


if __name__ == '__main__':
    persons = [(lambda name, points, penalty:
                (-int(points), int(penalty), name))(*input().split())
               for _ in range(int(input()))]
    persons = effective_quicksort(persons)
    print(*[name for _, _, name in persons], sep='\n')
