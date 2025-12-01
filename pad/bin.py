def bin_find(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return True
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return False


print(bin_find([2, 2, 2, 2, 3], 3))
