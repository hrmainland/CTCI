nums = []


def recurse(depth):
    if depth == 5:
        return
    nums.append(depth)
    recurse(depth + 1)


recurse(0)

print(nums)
