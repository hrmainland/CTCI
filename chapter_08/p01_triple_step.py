def triple_hop(x):
    if x < 0:
        return 0
    if x == 0:
        return 1
    if x == 1:
        return 1
    return triple_hop(x - 1) + triple_hop(x - 2) + triple_hop(x - 3)


def method_2(x):
    memo = [-1] * (x + 1)
    return triple_hop_recursive(x, memo)


def triple_hop_recursive(x, memo):
    if x < 0:
        return 0
    memo[0] = 1
    if x >= 1:
        memo[1] = 1
    if x >= 2:
        memo[2] = memo[1] + memo[0]
    if x > 2:
        for i in range(3, x + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[x]


def n_ways_bu(n):
    first = (1, 2, 4)
    if n < 4:
        return first[n - 1]
    a, b, c = first
    for _ in range(4, n):
        d = a + b + c
        a, b, c = b, c, d
    return a + b + c


def n_ways_td(n):
    memo = [-1] * (n + 1)
    memo[:3] = [1, 1, 2]
    return n_ways_memo(n, memo)


def n_ways_memo(n, memo):
    if memo[n] == -1:
        result = (
            n_ways_memo(n - 1, memo)
            + n_ways_memo(n - 2, memo)
            + n_ways_memo(n - 3, memo)
        )
        memo[n] = result
    # print(memo)
    return memo[n]


if __name__ == "__main__":
    for n in range(1, 12):
        print(triple_hop(n), n_ways_bu(n), n_ways_td(n))
    # print(n_ways_td(5))

print(int(2**1000))
