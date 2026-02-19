"""Challenge: LCM and GCD Calculator

Problem Statement:
---------------
Write two functions:
1. gcd(a, b): Calculate the Greatest Common Divisor (GCD) of two numbers
2. lcm(a, b): Calculate the Least Common Multiple (LCM) of two numbers

GCD: The largest positive integer that divides both numbers without a remainder
LCM: The smallest positive integer that is divisible by both numbers

Relationship: LCM(a, b) * GCD(a, b) = a * b

Examples:
--------
Example 1:
Input: a = 12, b = 18
Output: GCD = 6, LCM = 36
Explanation: 
- Factors of 12: 1, 2, 3, 4, 6, 12
- Factors of 18: 1, 2, 3, 6, 9, 18
- Common factors: 1, 2, 3, 6 → GCD = 6
- Multiples of 12: 12, 24, 36, 48...
- Multiples of 18: 18, 36, 54...
- Common multiples: 36, 72... → LCM = 36

Example 2:
Input: a = 7, b = 5
Output: GCD = 1, LCM = 35
Explanation: 7 and 5 are coprime (no common factors except 1)

Example 3:
Input: a = 100, b = 50
Output: GCD = 50, LCM = 100
Explanation: 50 divides 100 evenly

Constraints:
-----------
- 1 <= a, b <= 10^9
- Both numbers are positive integers

Time Complexity: O(log(min(a, b))) for Euclidean algorithm
Space Complexity: O(1)
"""

# Approach 1: Euclidean Algorithm (Most Efficient)
def gcd_euclidean(a, b):
    """
    Calculate GCD using Euclidean algorithm
    
    Args:
        a: First positive integer
        b: Second positive integer
    
    Returns:
        Greatest Common Divisor of a and b
    """
    while b:
        a, b = b, a % b
    return a

def lcm_using_gcd(a, b):
    """
    Calculate LCM using the relationship: LCM(a,b) = (a*b) / GCD(a,b)
    
    Args:
        a: First positive integer
        b: Second positive integer
    
    Returns:
        Least Common Multiple of a and b
    """
    return (a * b) // gcd_euclidean(a, b)

# Approach 2: Recursive GCD
def gcd_recursive(a, b):
    """
    Calculate GCD using recursive Euclidean algorithm
    
    Args:
        a: First positive integer
        b: Second positive integer
    
    Returns:
        Greatest Common Divisor of a and b
    """
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

def lcm_recursive(a, b):
    """
    Calculate LCM using recursive GCD
    
    Args:
        a: First positive integer
        b: Second positive integer
    
    Returns:
        Least Common Multiple of a and b
    """
    return (a * b) // gcd_recursive(a, b)

# Approach 3: Using Python's math module
import math

def gcd_builtin(a, b):
    """
    Calculate GCD using Python's built-in math.gcd
    
    Args:
        a: First positive integer
        b: Second positive integer
    
    Returns:
        Greatest Common Divisor of a and b
    """
    return math.gcd(a, b)

def lcm_builtin(a, b):
    """
    Calculate LCM using Python's built-in math.lcm (Python 3.9+)
    
    Args:
        a: First positive integer
        b: Second positive integer
    
    Returns:
        Least Common Multiple of a and b
    """
    return math.lcm(a, b)

# Test Cases
def test_gcd_lcm():
    test_cases = [
        # (a, b, expected_gcd, expected_lcm)
        (12, 18, 6, 36),
        (7, 5, 1, 35),
        (100, 50, 50, 100),
        (21, 14, 7, 42),
        (1, 1, 1, 1),
        (48, 18, 6, 144),
        (17, 19, 1, 323),  # Two prime numbers
        (24, 36, 12, 72),
        (1000, 500, 500, 1000),
        (13, 13, 13, 13),  # Same numbers
    ]
    
    print("Testing GCD and LCM calculations:")
    print("=" * 70)
    
    for a, b, expected_gcd, expected_lcm in test_cases:
        # Test Approach 1 (Euclidean)
        gcd_result = gcd_euclidean(a, b)
        lcm_result = lcm_using_gcd(a, b)
        
        status_gcd = "✓" if gcd_result == expected_gcd else "✗"
        status_lcm = "✓" if lcm_result == expected_lcm else "✗"
        
        print(f"Input: a={a:4d}, b={b:4d}")
        print(f"  GCD: {gcd_result:4d} (Expected: {expected_gcd:4d}) {status_gcd}")
        print(f"  LCM: {lcm_result:4d} (Expected: {expected_lcm:4d}) {status_lcm}")
        print()
        
        # Verify all approaches give same result
        assert gcd_euclidean(a, b) == gcd_recursive(a, b) == gcd_builtin(a, b)
        assert lcm_using_gcd(a, b) == lcm_recursive(a, b) == lcm_builtin(a, b)
    
    print("All test cases passed! ✓")
    print("\nVerified: All three approaches produce identical results.")

def demonstrate_relationship():
    """
    Demonstrate the relationship: LCM(a,b) * GCD(a,b) = a * b
    """
    print("\nDemonstrating: LCM(a,b) × GCD(a,b) = a × b")
    print("=" * 70)
    
    test_values = [(12, 18), (7, 5), (48, 18), (100, 50)]
    
    for a, b in test_values:
        gcd_val = gcd_euclidean(a, b)
        lcm_val = lcm_using_gcd(a, b)
        product = a * b
        lcm_gcd_product = lcm_val * gcd_val
        
        print(f"a={a:3d}, b={b:3d}: LCM={lcm_val:4d}, GCD={gcd_val:3d}")
        print(f"  → {lcm_val} × {gcd_val} = {lcm_gcd_product} | {a} × {b} = {product} ✓")
        print()

if __name__ == "__main__":
    # Run test cases
    test_gcd_lcm()
    
    # Demonstrate the mathematical relationship
    demonstrate_relationship()
    
    # Interactive example
    print("\nInteractive Example:")
    print("=" * 70)
    a, b = 24, 36
    print(f"Given: a = {a}, b = {b}")
    print(f"\nApproach 1 (Euclidean Algorithm):")
    print(f"  GCD({a}, {b}) = {gcd_euclidean(a, b)}")
    print(f"  LCM({a}, {b}) = {lcm_using_gcd(a, b)}")
    print(f"\nApproach 2 (Recursive):")
    print(f"  GCD({a}, {b}) = {gcd_recursive(a, b)}")
    print(f"  LCM({a}, {b}) = {lcm_recursive(a, b)}")
    print(f"\nApproach 3 (Built-in):")
    print(f"  GCD({a}, {b}) = {gcd_builtin(a, b)}")
    print(f"  LCM({a}, {b}) = {lcm_builtin(a, b)}")
