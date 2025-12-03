# My solution to p03_magic_index.py

"""

[-10, -5, 0, 2, 4]


"""


def magic_index(nums):
    left, right = 0, len(nums)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == mid:
            return mid
        if nums[mid] < mid:
            left = mid + 1
        elif nums[mid] > mid:
            right = mid - 1
    return -1


nums = [-10, -5, 0, 2, 4]
nums = [-10, -5, 0, 2, 5]

result = magic_index(nums)
print(result)
