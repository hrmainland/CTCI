nums = [1, 2, 3, 4]

prefix = [prefix[i-1] if i > 0 else 1 for i in range(5)]