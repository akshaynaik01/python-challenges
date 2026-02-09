"""
Day 11 Challenge: Longest Substring Without Repeating Characters

Problem:
Given a string s, find the length of the longest substring without repeating characters.

Examples:
- Input: "abcabcbb" -> Output: 3 ("abc")
- Input: "bbbbb" -> Output: 1 ("b")
- Input: "pwwkew" -> Output: 3 ("wke")

Approach: Sliding Window with HashMap
Time Complexity: O(n)
Space Complexity: O(min(m, n)) where m is charset size
"""

def lengthOfLongestSubstring(s: str) -> int:
    """
    Find the length of longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        Length of longest substring without repeating characters
    """
    char_index = {}  # Store character and its last seen index
    max_length = 0
    start = 0  # Left pointer of sliding window
    
    for end in range(len(s)):
        char = s[end]
        
        # If character is found and is within current window
        if char in char_index and char_index[char] >= start:
            # Move start pointer to right after the last occurrence
            start = char_index[char] + 1
        
        # Update the character's latest index
        char_index[char] = end
        
        # Update max length
        max_length = max(max_length, end - start + 1)
    
    return max_length


# Alternative Approach: Using Set
def lengthOfLongestSubstring_v2(s: str) -> int:
    """
    Alternative approach using set instead of hashmap.
    """
    char_set = set()
    max_length = 0
    start = 0
    
    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        
        char_set.add(s[end])
        max_length = max(max_length, end - start + 1)
    
    return max_length


# Test Cases
if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("au", 2),
        ("dvdf", 3),
        ("", 0),
        ("a", 1),
        ("abcdefghijklmnopqrstuvwxyz", 26),
    ]
    
    print("Testing Approach 1 (HashMap):")
    for s, expected in test_cases:
        result = lengthOfLongestSubstring(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{s}' | Expected: {expected} | Got: {result}")
    
    print("\nTesting Approach 2 (Set):")
    for s, expected in test_cases:
        result = lengthOfLongestSubstring_v2(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{s}' | Expected: {expected} | Got: {result}")
