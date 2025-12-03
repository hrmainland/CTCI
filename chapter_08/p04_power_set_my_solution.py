# My solution to p04_power_set.py
"""
{1, 3, 4, 5}

binary decision: include or not

include then don't include

recursive_function(index):
    # base case
    index out of bounds
    add this_result to result

    # body
    include nums[index]
    recurse
    remove nums[index]
    recurse
    return

result = [{1, 3, 4}, {1, 3}, {1}, {}, {3, 4}]
subset = {1}

[1, 3, 4]
       i

"""


def power_set(nums):
    result = []
    nums = list(nums)

    def rec_search(index, subset: set):
        # base case
        if index == len(nums):
            result.append(subset.copy())
            return

        # main body
        subset.add(nums[index])
        rec_search(index + 1, subset)
        subset.remove(nums[index])
        rec_search(index + 1, subset)
        return

    rec_search(0, set())
    return result


nums = [1, 3, 4]

result = power_set(nums)
print(result)
