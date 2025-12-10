# My solution to p11_coins.py
"""
bottom up:


"""


def n_ways(value, denoms):
    def rec_search(value, index, memo):
        coin = denoms[index]
        if coin == 1:
            return 1
        if memo[coin].get(value):
            return memo[coin][value]
        result = 0
        for n_coins in range(0, (value // coin) + 1):
            new_val = value - coin * n_coins
            result += rec_search(new_val, index + 1, memo)

        memo[coin][value] = result
        return result

    denoms = sorted(denoms, reverse=True)
    memo = {key: {} for key in denoms}
    return rec_search(value, 0, memo)


print(n_ways(10000, [1, 5, 10, 25]))
