"""Day 10 Challenge: Factorial Function

Factorial of a non-negative integer n, denoted by n!, is the product of
all positive integers less than or equal to n.

Example: 5! = 5 × 4 × 3 × 2 × 1 = 120
         0! = 1 (by definition)
         1! = 1

Time Complexity:
- Recursive: O(n)
- Iterative: O(n)

Space Complexity:
- Recursive: O(n) due to call stack
- Iterative: O(1)
"""

import math


def factorial_recursive(n):
    """
    Calculate factorial using recursion.
    
    Time Complexity: O(n)
    Space Complexity: O(n) - recursive call stack
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """
    Calculate factorial using iteration.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_builtin(n):
    """
    Calculate factorial using Python's built-in math library.
    
    This is the most efficient and recommended way.
    """
    return math.factorial(n)


def factorial_memoization(n, memo=None):
    """
    Calculate factorial using recursion with memoization.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Memoization improves performance by storing already computed values.
    """
    if memo is None:
        memo = {}
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n in memo:
        return memo[n]
    
    if n == 0 or n == 1:
        return 1
    
    memo[n] = n * factorial_memoization(n - 1, memo)
    return memo[n]


if __name__ == "__main__":
    test_cases = [0, 1, 5, 10, 15, 20]
    
    print("Testing factorial_recursive:")
    for num in test_cases:
        result = factorial_recursive(num)
        print(f"factorial_recursive({num}) = {result}")
    print()
    
    print("Testing factorial_iterative:")
    for num in test_cases:
        result = factorial_iterative(num)
        print(f"factorial_iterative({num}) = {result}")
    print()
    
    print("Testing factorial_builtin:")
    for num in test_cases:
        result = factorial_builtin(num)
        print(f"factorial_builtin({num}) = {result}")
    print()
    
    print("Testing factorial_memoization:")
    for num in test_cases:
        result = factorial_memoization(num)
        print(f"factorial_memoization({num}) = {result}")
    print()
    
    # Verify all methods produce same results
    print("Verifying all methods produce same results:")
    for num in test_cases:
        rec = factorial_recursive(num)
        it = factorial_iterative(num)
        bi = factorial_builtin(num)
        mem = factorial_memoization(num)
        
        if rec == it == bi == mem:
            print(f"✓ All methods agree for {num}! = {rec}")
        else:
            print(f"✗ Methods disagree for {num}!")
    
    # Test error handling
    print("\nTesting error handling:")
    try:
        factorial_recursive(-5)
    except ValueError as e:
        print(f"factorial_recursive(-5) raised error: {e}")
    
    try:
        factorial_iterative(-5)
    except ValueError as e:
        print(f"factorial_iterative(-5) raised error: {e}")
