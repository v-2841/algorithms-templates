def merge(arr, lf, mid, rg):
    result = [None] * (rg-lf)
    i, j, k = lf, mid, 0
    while i < mid and j < rg:
        if arr[i] < arr[j]:
            result[k] = arr[i]
            i += 1
        else:
            result[k] = arr[j]
            j += 1
        k += 1
    while i < mid:
        result[k] = arr[i]
        i += 1
        k += 1
    while j < rg:
        result[k] = arr[j]
        j += 1
        k += 1
    return result


def merge_sort(arr, lf, rg):
    if rg - lf > 1:
        mid = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        arr[lf:rg] = merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
