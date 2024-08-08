#!/usr/bin/python3
"""
0-prime_game module
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime number game.

    Args:
        x (int): The number of rounds.
        nums (list): The list of integers n for each round.

    Returns:
        str or None: The name of the player that won the most rounds,
                or None if the winner cannot be determined.
    """
    if not nums or x < 1:
        return None

    def sieve_of_eratosthenes(n):
        """
        Implements the Sieve of Eratosthenes algorithm to find
                all prime numbers up to n.
        """
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        return [i for i in range(n + 1) if is_prime[i]]

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    primes_count = [0] * (max_num + 1)

    for i in range(1, max_num + 1):
        primes_count[i] = primes_count[i - 1]
        if i in primes:
            primes_count[i] += 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
