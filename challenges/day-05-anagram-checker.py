"""
Day 5 Challenge: Anagram Checker
An anagram is a word or phrase formed by rearranging the letters of another word or phrase, typically using all the original letters exactly once.
Example: 'listen' and 'silent' are anagrams.
"""

# Approach 1: Using sorted()
def is_anagram_sorted(str1, str2):
    """
    Check if two strings are anagrams using sorted().
    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(n)
    """
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Compare sorted versions
    return sorted(str1) == sorted(str2)


# Approach 2: Using character count with dictionary
def is_anagram_dict(str1, str2):
    """
    Check if two strings are anagrams using dictionary.
    Time Complexity: O(n)
    Space Complexity: O(k) where k is the number of unique characters
    """
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    char_count = {}
    
    # Count characters in str1
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Subtract characters found in str2
    for char in str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return True


# Approach 3: Using Counter from collections
from collections import Counter

def is_anagram_counter(str1, str2):
    """
    Check if two strings are anagrams using Counter.
    Time Complexity: O(n)
    Space Complexity: O(k) where k is the number of unique characters
    """
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return Counter(str1) == Counter(str2)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("listen", "silent", True),
        ("hello", "world", False),
        ("anagram", "nagaram", True),
        ("The Morse Code", "Here come dots", True),
        ("python", "typhon", True),
        ("abc", "def", False),
        ("a gentleman", "elegant man", True),
        ("abc", "abcd", False),
    ]
    
    print("Anagram Checker - Multiple Approaches:")
    print("=" * 70)
    
    for str1, str2, expected in test_cases:
        result1 = is_anagram_sorted(str1, str2)
        result2 = is_anagram_dict(str1, str2)
        result3 = is_anagram_counter(str1, str2)
        
        status = "PASS" if result1 == expected else "FAIL"
        print(f"Strings: '{str1}' and '{str2}'")
        print(f"  Expected: {expected} | Sorted: {result1} | Dict: {result2} | Counter: {result3} | {status}")
        print("-" * 70)
