"""
Palindrome Checker Challenge

Problem:
Check if a given string is a palindrome.
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

Approaches:
1. Using string slicing and comparison
2. Using two pointers
3. Using recursion

Test Cases:
- "racecar" -> True
- "hello" -> False
- "A man a plan a canal Panama" -> True (ignoring spaces and case)
- "12321" -> True
- "" -> True (empty string is palindrome)
"""

# Approach 1: Using String Slicing (Simplest)
def is_palindrome_slicing(s):
    """
    Check if string is palindrome using string slicing.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Convert to lowercase and remove spaces
    cleaned = s.lower().replace(" ", "")
    # Compare with reverse
    return cleaned == cleaned[::-1]


# Approach 2: Using Two Pointers
def is_palindrome_two_pointers(s):
    """
    Check if string is palindrome using two pointer approach.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Clean the string
    cleaned = s.lower().replace(" ", "")
    
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True


# Approach 3: Using Recursion
def is_palindrome_recursive(s):
    """
    Check if string is palindrome using recursion.
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion stack
    """
    # Clean the string
    cleaned = s.lower().replace(" ", "")
    
    def helper(left, right):
        if left >= right:
            return True
        if cleaned[left] != cleaned[right]:
            return False
        return helper(left + 1, right - 1)
    
    return helper(0, len(cleaned) - 1)


# Test Cases
if __name__ == "__main__":
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("A man a plan a canal Panama", True),
        ("12321", True),
        ("", True),
        ("Madam", True),
        ("python", False),
        ("noon", True),
        ("civic", True),
        ("level", True),
    ]
    
    # Test Approach 1
    print("Testing Approach 1: String Slicing")
    print("-" * 40)
    for string, expected in test_cases:
        result = is_palindrome_slicing(string)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_palindrome_slicing('{string}') = {result}")
    
    print("\nTesting Approach 2: Two Pointers")
    print("-" * 40)
    for string, expected in test_cases:
        result = is_palindrome_two_pointers(string)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_palindrome_two_pointers('{string}') = {result}")
    
    print("\nTesting Approach 3: Recursion")
    print("-" * 40)
    for string, expected in test_cases:
        result = is_palindrome_recursive(string)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_palindrome_recursive('{string}') = {result}")
