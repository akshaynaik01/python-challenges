"""
Day 4 Challenge: Reverse String
Reverse a string in multiple ways with different approaches.
"""

# Approach 1: Using slicing
def reverse_string_slicing(s):
    """
    Reverse a string using Python slicing.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return s[::-1]


# Approach 2: Using reversed() function
def reverse_string_reversed(s):
    """
    Reverse a string using the reversed() function.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return ''.join(reversed(s))


# Approach 3: Using a loop
def reverse_string_loop(s):
    """
    Reverse a string using a for loop.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    result = ""
    for char in s:
        result = char + result
    return result


# Approach 4: Using recursion
def reverse_string_recursion(s):
    """
    Reverse a string using recursion.
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion stack
    """
    if len(s) == 0:
        return s
    return reverse_string_recursion(s[1:]) + s[0]


# Test cases
if __name__ == "__main__":
    test_cases = [
        "hello",
        "python",
        "racecar",
        "a",
        "",
        "12345",
        "Hello World!"
    ]
    
    print("String Reversal - Multiple Approaches:")
    print("=" * 70)
    
    for test in test_cases:
        print(f"Original: '{test}'")
        print(f"  Slicing:     '{reverse_string_slicing(test)}'")
        print(f"  Reversed():  '{reverse_string_reversed(test)}'")
        print(f"  Loop:        '{reverse_string_loop(test)}'")
        print(f"  Recursion:   '{reverse_string_recursion(test)}'")
        print("-" * 70)
