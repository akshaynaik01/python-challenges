"""
Day 16 Challenge: Word Frequency Counter

Problem Statement:
Given a string of text, count the frequency of each word (case-insensitive).
Ignore punctuation and return words sorted by frequency in descending order.

Examples:
- Input: "Hello world! hello Python. Python is great!"
  Output: [('hello', 2), ('python', 2), ('world', 1), ('is', 1), ('great', 1)]

Constraints:
- Words are separated by spaces
- Ignore common punctuation: . , ! ? ; : " ' -
- Case-insensitive comparison
"""

import re
from collections import Counter
from typing import List, Tuple

# Approach 1: Using Counter from collections
def word_frequency_v1(text: str) -> List[Tuple[str, int]]:
    """
    Count word frequency using Counter
    Time Complexity: O(n + k log k) where n is text length, k is unique words
    Space Complexity: O(k) for storing unique words
    """
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[.!?,;:"\'-]', '', text.lower())
    
    # Split into words and count
    words = text.split()
    word_counts = Counter(words)
    
    # Return sorted by frequency (descending)
    return word_counts.most_common()


# Approach 2: Using Dictionary
def word_frequency_v2(text: str) -> List[Tuple[str, int]]:
    """
    Count word frequency using dictionary
    Time Complexity: O(n + k log k) where n is text length, k is unique words
    Space Complexity: O(k) for storing unique words
    """
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[.!?,;:"\'-]', '', text.lower())
    
    # Split into words
    words = text.split()
    
    # Count frequencies manually
    word_count = {}
    for word in words:
        if word:  # Skip empty strings
            word_count[word] = word_count.get(word, 0) + 1
    
    # Sort by frequency (descending)
    return sorted(word_count.items(), key=lambda x: x[1], reverse=True)


# Approach 3: Using defaultdict
def word_frequency_v3(text: str) -> List[Tuple[str, int]]:
    """
    Count word frequency using defaultdict
    Time Complexity: O(n + k log k) where n is text length, k is unique words
    Space Complexity: O(k) for storing unique words
    """
    from collections import defaultdict
    
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[.!?,;:"\'-]', '', text.lower())
    
    # Split into words
    words = text.split()
    
    # Count frequencies
    word_count = defaultdict(int)
    for word in words:
        if word:
            word_count[word] += 1
    
    # Sort by frequency (descending)
    return sorted(word_count.items(), key=lambda x: x[1], reverse=True)


# Test cases
if __name__ == "__main__":
    test_cases = [
        "Hello world! hello Python. Python is great!",
        "The quick brown fox jumps over the lazy dog. The fox is quick.",
        "python python python java java javascript",
        "a a a b b c",
        "Hello, Hello, Hello!",
    ]
    
    print("Testing word_frequency_v1 (Counter approach):")
    for text in test_cases:
        result = word_frequency_v1(text)
        print(f"Input: '{text}'")
        print(f"Output: {result}\n")
    
    print("Testing word_frequency_v2 (Dictionary approach):")
    for text in test_cases:
        result = word_frequency_v2(text)
        print(f"Input: '{text}'")
        print(f"Output: {result}\n")
    
    print("Testing word_frequency_v3 (defaultdict approach):")
    for text in test_cases:
        result = word_frequency_v3(text)
        print(f"Input: '{text}'")
        print(f"Output: {result}\n")