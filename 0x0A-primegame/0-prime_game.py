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
    def is_prime(n):
        """
        Checks if a number is prime.
        """
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sieve_of_eratosthenes(n):
        """
        Implements the Sieve of Eratosthenes algorithm to
		find all prime numbers up to n.
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        return [i for i in range(n + 1) if primes[i]]

    if x == 0:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = sieve_of_eratosthenes(n)
        available_primes = primes[:]

        while available_primes:
            if len(available_primes) == 1:
                winner = "Maria"
            elif len(available_primes) == 0:
                winner = "Ben"
            else:
                first_prime = available_primes[0]
                second_prime = available_primes[1]
                if first_prime + second_prime > n:
                    winner = "Maria"
                else:
                    winner = "Ben"

            if winner == "Maria":
                maria_wins += 1
                available_primes.pop(0)
            else:
                ben_wins += 1
                available_primes.pop(0)

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
