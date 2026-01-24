"""
Day 2 Challenge: Even Number Checker

Problem:
Write a function to check if a given number is even or odd.

Approach:
- Use modulo operator (%) to check if number is divisible by 2
- If num % 2 == 0, it's even
- Otherwise, it's odd
"""

def is_even(n):
    """
    Check if a number is even.
    
    Args:
        n: Integer number to check
    
    Returns:
        True if even, False if odd
    """
    return n % 2 == 0

def check_even_odd(n):
    """
    Determine if number is even or odd and return message.
    
    Args:
        n: Integer number to check
    
    Returns:
        String message indicating even or odd
    """
    if is_even(n):
        return f"{n} is an Even number"
    else:
        return f"{n} is an Odd number"


# Test cases
if __name__ == "__main__":
    test_cases = [0, 1, 2, 5, 10, -3, -4, 100, 999]
    
    print("Even Number Checker Results:")
    print("-" * 40)
    for num in test_cases:
        print(check_even_odd(num))
