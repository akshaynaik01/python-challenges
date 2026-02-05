"""Day 9 Challenge: Binary Search Algorithm

Binary Search is an efficient algorithm for finding an item in a sorted array.
It works by dividing the search interval in half and comparing the target value
with the middle element.

Precondition: The array must be sorted.

Time Complexity: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive

Best Case: O(1)
Worst Case: O(log n)
Average Case: O(log n)
"""


def binary_search_iterative(arr, target):
    """
    Iterative binary search implementation.
    Returns the index of target if found, else -1.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left, right):
    """
    Recursive binary search implementation.
    Returns the index of target if found, else -1.
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    """
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def binary_search_leftmost(arr, target):
    """
    Find the leftmost (first) occurrence of target.
    Useful when there are duplicates in the array.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching in left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def binary_search_rightmost(arr, target):
    """
    Find the rightmost (last) occurrence of target.
    Useful when there are duplicates in the array.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching in right half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5, 7, 9, 11, 13, 15], 7),
        ([1, 3, 5, 7, 9, 11, 13, 15], 1),
        ([1, 3, 5, 7, 9, 11, 13, 15], 15),
        ([1, 3, 5, 7, 9, 11, 13, 15], 10),
        ([1, 1, 1, 1, 5, 5, 5, 5], 5),
        ([], 5),
        ([5], 5),
        ([5], 3),
    ]
    
    print("Testing binary_search_iterative:")
    for arr, target in test_cases:
        result = binary_search_iterative(arr, target)
        print(f"Array: {arr}, Target: {target}")
        print(f"Index: {result}")
        print()
    
    print("\nTesting binary_search_recursive:")
    for arr, target in test_cases:
        result = binary_search_recursive(arr, target, 0, len(arr) - 1) if arr else -1
        print(f"Array: {arr}, Target: {target}")
        print(f"Index: {result}")
        print()
    
    print("\nTesting binary_search_leftmost (with duplicates):")
    dup_arr = [1, 1, 1, 1, 5, 5, 5, 5]
    for target in [1, 5, 3]:
        result = binary_search_leftmost(dup_arr, target)
        print(f"Array: {dup_arr}, Target: {target}")
        print(f"Leftmost Index: {result}")
        print()
    
    print("\nTesting binary_search_rightmost (with duplicates):")
    for target in [1, 5, 3]:
        result = binary_search_rightmost(dup_arr, target)
        print(f"Array: {dup_arr}, Target: {target}")
        print(f"Rightmost Index: {result}")
        print()
