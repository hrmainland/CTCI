def bin_search(target, array):
    result = None
    left, right = 0, len(array)
    while left < right:
        mid = (right + left) // 2
        if array[mid] == target:
            result = min(target, mid)
            right = mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid
    return result if result else left


array = [1, 2, 2, 3, 4, 6, 7, 7, 7]
target = 8
print(bin_search(target, array))
