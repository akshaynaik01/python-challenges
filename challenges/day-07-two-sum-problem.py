"""Day 7 Challenge: Two Sum Problem

Given an array of integers nums and an integer target, return the indices 
of the two numbers that add up to the target. You may not use the same 
element twice.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
"""


def two_sum(nums, target):
    """
    Find two numbers that add up to target using HashMap approach.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def two_sum_brute_force(nums, target):
    """
    Find two numbers using brute force approach (nested loops).
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_sorted(nums, target):
    """
    Find two numbers using two-pointer approach on sorted array.
    
    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(1) or O(n) depending on sorting algorithm
    """
    sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
    left, right = 0, len(sorted_nums) - 1
    
    while left < right:
        current_sum = sorted_nums[left][1] + sorted_nums[right][1]
        if current_sum == target:
            return sorted([sorted_nums[left][0], sorted_nums[right][0]])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 2, 3, 4, 5], 9),
        ([-1, -2, -3, 5, 6], 5),
    ]
    
    print("Testing two_sum (HashMap approach):")
    for nums, target in test_cases:
        result = two_sum(nums, target)
        print(f"Input: {nums}, Target: {target}")
        print(f"Output: {result}")
        if result:
            print(f"Verification: {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")
        print()
    
    print("\nTesting two_sum_brute_force:")
    for nums, target in test_cases:
        result = two_sum_brute_force(nums, target)
        print(f"Input: {nums}, Target: {target}")
        print(f"Output: {result}")
        print()
    
    print("\nTesting two_sum_sorted:")
    for nums, target in test_cases:
        result = two_sum_sorted(nums, target)
        print(f"Input: {nums}, Target: {target}")
        print(f"Output: {result}")
        print()
