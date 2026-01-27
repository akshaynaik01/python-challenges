"""
Fibonacci Sequence - Generate Fibonacci numbers

Challenge: Write functions to generate Fibonacci numbers up to n terms
or up to a maximum value.

Example:
    fibonacci_sequence(7) -> [0, 1, 1, 2, 3, 5, 8]
    fibonacci_up_to(50) -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
"""

def fibonacci_sequence(n: int) -> list:
    """
    Generate first n Fibonacci numbers.
    
    Args:
        n: Number of Fibonacci numbers to generate
        
    Returns:
        List of first n Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib


def fibonacci_up_to(max_val: int) -> list:
    """
    Generate Fibonacci numbers up to a maximum value.
    
    Args:
        max_val: Maximum value for Fibonacci numbers
        
    Returns:
        List of Fibonacci numbers up to max_val
    """
    if max_val < 0:
        return []
    
    fib = [0]
    if max_val == 0:
        return fib
    
    fib.append(1)
    while True:
        next_fib = fib[-1] + fib[-2]
        if next_fib > max_val:
            break
        fib.append(next_fib)
    
    return fib


def fibonacci_recursive(n: int) -> int:
    """
    Get nth Fibonacci number using recursion (inefficient).
    
    Args:
        n: Position of Fibonacci number
        
    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_memo(n: int, memo=None) -> int:
    """
    Get nth Fibonacci number using memoization (efficient).
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]


# Test cases
if __name__ == "__main__":
    print("First 10 Fibonacci numbers:", fibonacci_sequence(10))
    print("Fibonacci up to 100:", fibonacci_up_to(100))
    print("10th Fibonacci number (memoization):", fibonacci_memo(10))
    print("\nTest cases:")
    
    test_cases = [
        (fibonacci_sequence(7), [0, 1, 1, 2, 3, 5, 8]),
        (fibonacci_up_to(50), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
        (fibonacci_memo(10), 55),
    ]
    
    for result, expected in test_cases:
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {result} (expected {expected})")
