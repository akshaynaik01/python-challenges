"""
Day 15 Challenge: Perfect Square

Problem Statement:
Given a positive integer n, determine if it is a perfect square.
A perfect square is a number that can be expressed as the product of two equal integers.

Examples:
- 16 is a perfect square (4 * 4)
- 25 is a perfect square (5 * 5)
- 10 is not a perfect square

Constraints:
- n is a positive integer
- 1 <= n <= 10^9
"""

# Approach 1: Using built-in sqrt function
import math

def is_perfect_square_v1(n):
    """
    Check if n is a perfect square using math.sqrt
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    if n < 0:
        return False
    
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n


# Approach 2: Binary Search
def is_perfect_square_v2(n):
    """
    Check if n is a perfect square using binary search
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    
    left, right = 1, n
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == n:
            return True
        elif square < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


# Approach 3: Newton's Method
def is_perfect_square_v3(n):
    """
    Check if n is a perfect square using Newton's method
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    if n < 0:
        return False
    if n == 0:
        return True
    
    x = n
    while True:
        x_new = (x + n // x) // 2
        if x_new >= x:
            break
        x = x_new
    
    return x * x == n


# Test cases
if __name__ == "__main__":
    test_cases = [
        (1, True),
        (4, True),
        (9, True),
        (16, True),
        (25, True),
        (49, True),
        (100, True),
        (2, False),
        (3, False),
        (5, False),
        (10, False),
        (15, False),
        (1000000000, False),
        (999999999, False),
        (1000000001, False),
    ]
    
    print("Testing is_perfect_square_v1 (sqrt approach):")
    for n, expected in test_cases:
        result = is_perfect_square_v1(n)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_perfect_square_v1({n}) = {result}, expected = {expected}")
    
    print("\nTesting is_perfect_square_v2 (binary search approach):")
    for n, expected in test_cases:
        result = is_perfect_square_v2(n)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_perfect_square_v2({n}) = {result}, expected = {expected}")
    
    print("\nTesting is_perfect_square_v3 (Newton's method approach):")
    for n, expected in test_cases:
        result = is_perfect_square_v3(n)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_perfect_square_v3({n}) = {result}, expected = {expected}")
