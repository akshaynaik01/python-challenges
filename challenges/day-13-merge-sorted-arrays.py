"""Day 13 Challenge: Merge Sorted Arrays

Challenge:
Write a function that merges two sorted arrays into a single sorted array.

Example:
Input: arr1 = [1, 3, 5, 7], arr2 = [2, 4, 6, 8]
Output: [1, 2, 3, 4, 5, 6, 7, 8]

Example 2:
Input: arr1 = [1, 2, 3], arr2 = [4, 5, 6]
Output: [1, 2, 3, 4, 5, 6]

Example 3:
Input: arr1 = [], arr2 = [1, 2, 3]
Output: [1, 2, 3]

Constraints:
- Both arrays are sorted in ascending order
- Arrays can be empty
- Arrays can contain duplicate values
"""

# Approach 1: Simple concatenation and sorting
# Time Complexity: O((n+m) log(n+m))
# Space Complexity: O(n+m)
def merge_sorted_arrays_v1(arr1, arr2):
    """
    Merges two sorted arrays using built-in sort.
    Simple but not optimal for already sorted arrays.
    """
    return sorted(arr1 + arr2)


# Approach 2: Two-pointer technique
# Time Complexity: O(n+m)
# Space Complexity: O(n+m)
def merge_sorted_arrays_v2(arr1, arr2):
    """
    Merges two sorted arrays using two-pointer technique.
    Optimal for already sorted arrays.
    """
    result = []
    i, j = 0, 0
    
    # Compare elements from both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Add remaining elements from arr1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    
    # Add remaining elements from arr2
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    
    return result


# Approach 3: Using extend and slicing
# Time Complexity: O(n+m)
# Space Complexity: O(n+m)
def merge_sorted_arrays_v3(arr1, arr2):
    """
    Merges two sorted arrays using list extend and slicing.
    More Pythonic approach.
    """
    result = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Extend with remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result


# Test cases
if __name__ == "__main__":
    # Test Case 1: Regular merge
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]
    print("Test Case 1:")
    print(f"Input: arr1 = {arr1}, arr2 = {arr2}")
    print(f"V1 Output: {merge_sorted_arrays_v1(arr1, arr2)}")
    print(f"V2 Output: {merge_sorted_arrays_v2(arr1, arr2)}")
    print(f"V3 Output: {merge_sorted_arrays_v3(arr1, arr2)}")
    print()
    
    # Test Case 2: No overlap
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    print("Test Case 2:")
    print(f"Input: arr1 = {arr1}, arr2 = {arr2}")
    print(f"V1 Output: {merge_sorted_arrays_v1(arr1, arr2)}")
    print(f"V2 Output: {merge_sorted_arrays_v2(arr1, arr2)}")
    print(f"V3 Output: {merge_sorted_arrays_v3(arr1, arr2)}")
    print()
    
    # Test Case 3: Empty first array
    arr1 = []
    arr2 = [1, 2, 3]
    print("Test Case 3:")
    print(f"Input: arr1 = {arr1}, arr2 = {arr2}")
    print(f"V1 Output: {merge_sorted_arrays_v1(arr1, arr2)}")
    print(f"V2 Output: {merge_sorted_arrays_v2(arr1, arr2)}")
    print(f"V3 Output: {merge_sorted_arrays_v3(arr1, arr2)}")
    print()
    
    # Test Case 4: Empty second array
    arr1 = [1, 2, 3]
    arr2 = []
    print("Test Case 4:")
    print(f"Input: arr1 = {arr1}, arr2 = {arr2}")
    print(f"V1 Output: {merge_sorted_arrays_v1(arr1, arr2)}")
    print(f"V2 Output: {merge_sorted_arrays_v2(arr1, arr2)}")
    print(f"V3 Output: {merge_sorted_arrays_v3(arr1, arr2)}")
    print()
    
    # Test Case 5: Both empty
    arr1 = []
    arr2 = []
    print("Test Case 5:")
    print(f"Input: arr1 = {arr1}, arr2 = {arr2}")
    print(f"V1 Output: {merge_sorted_arrays_v1(arr1, arr2)}")
    print(f"V2 Output: {merge_sorted_arrays_v2(arr1, arr2)}")
    print(f"V3 Output: {merge_sorted_arrays_v3(arr1, arr2)}")
    print()
    
    # Test Case 6: With duplicates
    arr1 = [1, 3, 3, 5]
    arr2 = [2, 3, 4, 5]
    print("Test Case 6:")
    print(f"Input: arr1 = {arr1}, arr2 = {arr2}")
    print(f"V1 Output: {merge_sorted_arrays_v1(arr1, arr2)}")
    print(f"V2 Output: {merge_sorted_arrays_v2(arr1, arr2)}")
    print(f"V3 Output: {merge_sorted_arrays_v3(arr1, arr2)}")
