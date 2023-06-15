# 88224443
def effective_quicksort(array, left=0, right=-1):
    if right == -1:
        right = len(array) - 1
    if left < right:
        pivot = array[left]
        l_pointer, r_pointer = left - 1, right + 1
        while True:
            l_pointer += 1
            r_pointer -= 1
            while array[l_pointer] < pivot:
                l_pointer += 1
            while array[r_pointer] > pivot:
                r_pointer -= 1
            if l_pointer >= r_pointer:
                break
            array[l_pointer], array[r_pointer] = array[
                r_pointer], array[l_pointer]
        effective_quicksort(array, left, r_pointer)
        effective_quicksort(array, r_pointer + 1, right)
    return array


if __name__ == '__main__':
    persons = [(lambda name, points, penalty:
                (-int(points), int(penalty), name))(*input().split())
               for _ in range(int(input()))]
    persons = effective_quicksort(persons)
    print(*[name for _, _, name in persons], sep='\n')
