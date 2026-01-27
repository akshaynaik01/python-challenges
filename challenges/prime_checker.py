"""
Prime Number Checker - Check if a number is prime

Challenge: Write functions to determine if a number is prime.

Example:
    is_prime(17) -> True
    is_prime(10) -> False
    get_primes_up_to(30) -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
"""

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
        n: Number to check
        
    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_primes_up_to(n: int) -> list:
    """
    Get all prime numbers up to n using Sieve of Eratosthenes.
    
    Args:
        n: Upper limit for prime numbers
        
    Returns:
        List of all primes up to n
    """
    if n < 2:
        return []
    
    # Create a boolean array
    is_prime_arr = [True] * (n + 1)
    is_prime_arr[0] = is_prime_arr[1] = False
    
    # Sieve of Eratosthenes
    for i in range(2, int(n**0.5) + 1):
        if is_prime_arr[i]:
            for j in range(i*i, n + 1, i):
                is_prime_arr[j] = False
    
    return [i for i in range(2, n + 1) if is_prime_arr[i]]


def prime_factors(n: int) -> list:
    """
    Find all prime factors of a number.
    
    Args:
        n: Number to factorize
        
    Returns:
        List of prime factors
    """
    factors = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    if n > 1:
        factors.append(n)
    
    return factors


def count_primes_up_to(n: int) -> int:
    """
    Count number of primes up to n.
    """
    return len(get_primes_up_to(n))


# Test cases
if __name__ == "__main__":
    test_cases = [
        (is_prime(2), True),
        (is_prime(17), True),
        (is_prime(10), False),
        (is_prime(1), False),
        (is_prime(0), False),
        (get_primes_up_to(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
        (prime_factors(60), [2, 2, 3, 5]),
        (count_primes_up_to(20), 8),
    ]
    
    for result, expected in test_cases:
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {result} (expected {expected})")
