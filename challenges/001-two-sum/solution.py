from typing import List, Tuple

def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """Return indices of the two numbers that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        Tuple of indices (i, j) where nums[i] + nums[j] == target
    
    Raises:
        ValueError: If no solution found
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    raise ValueError("No solution found")


if __name__ == "__main__":
    # Test cases
    arr = [2, 7, 11, 15]
    t = 9
    i, j = two_sum(arr, t)
    print(f"indices: {i}, {j}, values: {arr[i]}, {arr[j]}")
