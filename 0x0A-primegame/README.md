# Prime Game

This project is a solution to a competitive game scenario where players take turns removing prime numbers and their multiples from a set of consecutive integers.

## Concepts Needed

1. **Prime Numbers**:
   - Understanding what prime numbers are.
   - Efficient algorithms for identifying prime numbers within a range.
2. **Sieve of Eratosthenes**:
   - An efficient algorithm for finding all prime numbers up to any given limit, which can be particularly useful for this task.
3. **Game Theory**:
   - Basic principles of competitive games where players take turns and the concept of optimal play.
   - Understanding win conditions and strategies that lead to a win or loss.
4. **Dynamic Programming/Memoization**:
   - Using previous results to make future calculations faster, potentially necessary for optimizing the solution for multiple rounds of the game.
5. **Python Programming**:
   - Loops and conditional statements for implementing game logic and algorithms.
   - Arrays and lists for storing the integers and tracking removed numbers.

## Problem Description

Maria and Ben are playing a game. Given a set of consecutive integers starting from `1` up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round. Assuming Maria always goes first and both players play optimally, the task is to determine who the winner of each game is.

## Solution

The solution is implemented in the `0-prime_game.py` file, which contains the following functions:

1. `is_prime(n)`: Checks if a number is prime.
2. `sieve_of_eratosthenes(n)`: Implements the Sieve of Eratosthenes algorithm to find all prime numbers up to `n`.
3. `isWinner(x, nums)`: Determines the winner of the prime number game.

The `isWinner()` function takes two arguments:
- `x`: The number of rounds.
- `nums`: The list of integers `n` for each round.

The function returns the name of the player that won the most rounds, or `None` if the winner cannot be determined.

## Usage

To use the solution, you can call the `isWinner()` function with the appropriate input parameters:

```python
from 0-prime_game import isWinner

winner = isWinner(5, [2, 5, 1, 4, 3])
print(winner)  # Output: Ben

The provided main_0.py file demonstrates the usage of the isWinner() function.
Time Complexity
The time complexity of the solution is O(n * log(log(n))) for each round, where n is the maximum value in the nums list. This is due to the Sieve of Eratosthenes algorithm, which is an efficient way to find all prime numbers up to a given limit.
Conclusion
This solution leverages the understanding of prime numbers, game theory, and algorithm optimization to solve the competitive prime number game scenario. It uses the Sieve of Eratosthenes algorithm to efficiently identify prime numbers and implements the game logic to determine the winner of each round and the overall winner.
