# 88140298
def partition(array, pivot):
    left, right = 0, len(array) - 1
    while left < right:
        if array[left] <= pivot:
            left += 1
        else:
            array[left], array[right-1], array[
                right] = array[right-1], array[right], array[left]
            right -= 1
    return array[:left], array[left+1:]


def effective_quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[-1]
        left, right = partition(array, pivot)
        return effective_quicksort(left) + [pivot] + effective_quicksort(right)


def data_input():
    persons = []
    for _ in range(int(input())):
        name, points, penalty = input().split()
        persons.append([-int(points), int(penalty), name])
    return persons


if __name__ == '__main__':
    persons = effective_quicksort(data_input())
    for person in persons:
        print(person[2])
