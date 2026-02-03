"""
Day 6 Challenge: Fibonacci Generator
Generate Fibonacci sequence using different approaches including recursion, iteration, and generators.
The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
"""

# Approach 1: Recursive (Not efficient for large n)
def fib_recursive(n):
    """
    Generate nth Fibonacci number using recursion.
    Time Complexity: O(2^n) - Exponential
    Space Complexity: O(n) due to recursion stack
    """
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Approach 2: Iterative (Efficient)
def fib_iterative(n):
    """
    Generate nth Fibonacci number using iteration.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Approach 3: Using Memoization (Recursive with optimization)
def fib_memoized(n, memo={}):
    """
    Generate nth Fibonacci number using memoization.
    Time Complexity: O(n)
    Space Complexity: O(n) for memoization cache
    """
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memoized(n - 1, memo) + fib_memoized(n - 2, memo)
    return memo[n]


# Approach 4: Generator (Memory efficient for sequence)
def fib_generator(limit):
    """
    Generate Fibonacci sequence up to limit using generator.
    Time Complexity: O(n)
    Space Complexity: O(1) - Only stores two values at a time
    """
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


# Approach 5: Generate list of Fibonacci numbers
def fib_sequence(n):
    """
    Generate list of first n Fibonacci numbers.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list


# Test cases
if __name__ == "__main__":
    print("Fibonacci Generator - Multiple Approaches:")
    print("=" * 70)
    
    # Test individual nth number
    test_n = 10
    print(f"\nFibonacci Number at position {test_n}:")
    print(f"  Recursive:   {fib_recursive(test_n)}")
    print(f"  Iterative:   {fib_iterative(test_n)}")
    print(f"  Memoized:    {fib_memoized(test_n)}")
    
    # Test sequence generation
    print(f"\nFirst {test_n} Fibonacci Numbers:")
    print(f"  Sequence:    {fib_sequence(test_n)}")
    
    # Test generator
    print(f"\nUsing Generator (First {test_n} numbers):")
    fib_list = list(fib_generator(test_n))
    print(f"  Generator:   {fib_list}")
    
    print("\n" + "=" * 70)
    print("Performance Comparison:")
    print("-" * 70)
    
    # Performance test for larger numbers
    import time
    test_val = 30
    
    start = time.time()
    result = fib_iterative(test_val)
    iter_time = time.time() - start
    print(f"Iterative (n={test_val}):    {result} | Time: {iter_time:.6f}s")
    
    start = time.time()
    result = fib_memoized(test_val)
    memo_time = time.time() - start
    print(f"Memoized (n={test_val}):     {result} | Time: {memo_time:.6f}s")
