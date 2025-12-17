def num_parens(string, expected):
    # base case
    if len(string) == 1:
        val = bool(int(string))
        return 1 if val == expected else 0

    if len(string) % 2 == 0:
        raise Exception(f"Even length String found: {string}")

    result = 0

    for i in range(1, len(string), 2):
        operator = string[i]
        left = string[:i]
        right = string[i + 1 :]

        left_true = num_parens(left, True)
        left_false = num_parens(left, False)
        right_true = num_parens(right, True)
        right_false = num_parens(right, False)

        left_total = left_true + left_false
        right_total = right_true + right_false
        total = left_total * right_total

        if operator == "|":
            if expected:
                result += total - left_false * right_false
            else:
                result += left_false * right_false

        elif operator == "&":
            if expected:
                result += left_true * right_true
            else:
                result += total - left_true * right_true

        elif operator == "^":
            if expected:
                result += left_true * right_false + left_false * right_true
            else:
                result += left_true * right_true + left_false * right_false

    return result


print(num_parens("1^0|0|1", False))
