"""
Palindrome Checker - Check if a string is a palindrome

Challenge: Write a function that checks if a given string is a palindrome.
Ignore spaces and case sensitivity.

Example:
    is_palindrome("A man a plan a canal Panama") -> True
    is_palindrome("hello") -> False
"""

def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome (ignoring spaces and case).
    
    Args:
        s: Input string to check
        
    Returns:
        True if string is palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase
    cleaned = s.replace(" ", "").lower()
    
    # Compare with reversed string
    return cleaned == cleaned[::-1]


def is_palindrome_recursive(s: str) -> bool:
    """
    Check if a string is a palindrome using recursion.
    """
    # Remove spaces and convert to lowercase
    cleaned = s.replace(" ", "").lower()
    
    def check(left, right):
        if left >= right:
            return True
        if cleaned[left] != cleaned[right]:
            return False
        return check(left + 1, right - 1)
    
    return check(0, len(cleaned) - 1)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("A man a plan a canal Panama", True),
        ("hello", False),
        ("racecar", True),
        ("Was it a car or a cat I saw?", True),
        ("Python", False),
        ("", True),
        ("a", True),
    ]
    
    for test_str, expected in test_cases:
        result1 = is_palindrome(test_str)
        result2 = is_palindrome_recursive(test_str)
        status = "PASS" if result1 == expected and result2 == expected else "FAIL"
        print(f"{status}: '{test_str}' -> {result1} (expected {expected})")
