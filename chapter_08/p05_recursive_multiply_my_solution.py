# My solution to p05_recursive_multiply.py
"""

4 * 9

2 * a = a + a
1 * a = a

4 * a = 2 * 2 * a
5 * a = 2 * 2 * a + a

if num % 2 == 0:
return rec(num/2) + rec(num/2)

else:
return rec(num/2) + rec(num/2) + num

"""


def multiply(a, b):
    # base case
    if a == 1:
        return b
    if a == 2:
        return b + b

    # main body
    partial = multiply(a // 2, b)
    if a % 2 == 0:
        return partial + partial
    else:
        return partial + partial + b


result = multiply(214, 123)
print(result)
