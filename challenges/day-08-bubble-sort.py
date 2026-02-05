"""Day 8 Challenge: Bubble Sort Algorithm

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they are in the wrong order.
The pass through the list is repeated until the list is sorted.

Time Complexity: O(n^2)
Space Complexity: O(1)

Best Case: O(n) with optimized version
Worst Case: O(n^2)
Average Case: O(n^2)
"""


def bubble_sort(arr):
    """
    Standard bubble sort implementation.
    Sorts the array in ascending order.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_optimized(arr):
    """
    Optimized bubble sort with early exit.
    Exits when no swaps are made (array is sorted).
    
    Time Complexity: O(n) in best case, O(n^2) in worst case
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def bubble_sort_descending(arr):
    """
    Bubble sort that sorts in descending order.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  # Changed comparison
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 3, 1, 2],
        [],
        [1],
        [-5, -1, -3, -2, -4],
    ]
    
    print("Testing bubble_sort (standard):")
    for test in test_cases:
        arr = test.copy()
        result = bubble_sort(arr)
        print(f"Input: {test}")
        print(f"Output: {result}")
        print()
    
    print("\nTesting bubble_sort_optimized:")
    for test in test_cases:
        arr = test.copy()
        result = bubble_sort_optimized(arr)
        print(f"Input: {test}")
        print(f"Output: {result}")
        print()
    
    print("\nTesting bubble_sort_descending:")
    for test in test_cases:
        arr = test.copy()
        result = bubble_sort_descending(arr)
        print(f"Input: {test}")
        print(f"Output: {result}")
        print()
