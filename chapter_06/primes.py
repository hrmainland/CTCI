import time
import math


def naive_primes(n):
    """
    Lists all primes up to n and records the time it takes
    """
    start = time.time()
    primes = []
    for contender in range(1, n + 1):
        is_prime = True
        for divisor in range(2, int(math.sqrt(contender)) + 1):
            if contender % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(contender)
    end = time.time()
    print(f"Found {len(primes)} primes in {end - start} seconds")
    return primes


# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def cross_off(flags, prime):
    i = prime * prime
    while i < len(flags):
        flags[i] = False
        i += prime


def next_prime(flags, i):
    i += 1
    while i < len(flags) and flags[i] == False:
        i += 1
    return i


def sieve(n):
    start = time.time()
    # flags = [True] * 2 + [False] * (n - 1)
    flags = [True] * (n + 1)
    i = 2
    while i <= int(math.sqrt(n)):
        cross_off(flags, i)
        i = next_prime(flags, i)
    end = time.time()
    primes = []
    print(f"Found {len(primes)} primes in {end - start} seconds")
    primes = [i for i in range(len(flags)) if flags[i]][1:]
    print(f"Found {len(primes)} primes in {end - start} seconds")
    return


# write function that lists all primes up to n and records the time it takes

n = 10000000
# naive_primes(n)
sieve(n)
