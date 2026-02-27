"""
Day 17 Challenge: Matrix Rotation

Problem Statement:
Given an n x m matrix, rotate it 90 degrees clockwise.
The rotation should be done in-place if possible.

Examples:
Input:
1 2 3
4 5 6
7 8 9

Output (90 degrees clockwise):
7 4 1
8 5 2
9 6 3

Constraints:
- The matrix is not empty
- Matrix dimensions: 1 <= n, m <= 100
"""

from typing import List

# Approach 1: Using Transpose + Reverse Rows
def rotate_matrix_v1(matrix: List[List[int]]) -> None:
    """
    Rotate matrix 90 degrees clockwise using transpose and reverse
    Time Complexity: O(n*m)
    Space Complexity: O(1) - in-place
    """
    if not matrix:
        return
    
    n = len(matrix)
    m = len(matrix[0])
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()


# Approach 2: Using Layer-by-Layer Rotation
def rotate_matrix_v2(matrix: List[List[int]]) -> None:
    """
    Rotate matrix 90 degrees clockwise layer by layer
    Time Complexity: O(n*m)
    Space Complexity: O(1) - in-place
    """
    if not matrix:
        return
    
    n = len(matrix)
    m = len(matrix[0])
    
    # Process each layer
    layers = min(n, m) // 2
    
    for layer in range(layers):
        first = layer
        last = max(n, m) - 1 - layer
        
        for i in range(first, last):
            offset = i - first
            
            # Save top
            top = matrix[first][i]
            
            # Move left to top
            matrix[first][i] = matrix[last - offset][first]
            
            # Move bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]
            
            # Move right to bottom
            matrix[last][last - offset] = matrix[i][last]
            
            # Move top to right
            matrix[i][last] = top


# Approach 3: Create New Matrix
def rotate_matrix_v3(matrix: List[List[int]]) -> None:
    """
    Rotate matrix 90 degrees clockwise by creating a new matrix
    Time Complexity: O(n*m)
    Space Complexity: O(n*m) - extra space for new matrix
    """
    if not matrix:
        return
    
    n = len(matrix)
    m = len(matrix[0])
    
    # Create rotated matrix
    rotated = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            rotated[j][n - 1 - i] = matrix[i][j]
    
    # Copy back to original matrix
    for i in range(m):
        for j in range(n):
            matrix[i][j] = rotated[i][j]


def print_matrix(matrix: List[List[int]]) -> None:
    """Helper function to print matrix"""
    for row in matrix:
        print(row)
    print()


# Test cases
if __name__ == "__main__":
    test_matrices = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2], [3, 4]],
        [[1]],
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
    ]
    
    print("Testing rotate_matrix_v1 (Transpose + Reverse):")
    for matrix in test_matrices:
        test_matrix = [row[:] for row in matrix]
        print("Original:")
        print_matrix(test_matrix)
        rotate_matrix_v1(test_matrix)
        print("Rotated:")
        print_matrix(test_matrix)
    
    print("\nTesting rotate_matrix_v2 (Layer-by-Layer):")
    for matrix in test_matrices:
        test_matrix = [row[:] for row in matrix]
        print("Original:")
        print_matrix(test_matrix)
        rotate_matrix_v2(test_matrix)
        print("Rotated:")
        print_matrix(test_matrix)
    
    print("\nTesting rotate_matrix_v3 (New Matrix):")
    for matrix in test_matrices:
        test_matrix = [row[:] for row in matrix]
        print("Original:")
        print_matrix(test_matrix)
        rotate_matrix_v3(test_matrix)
        print("Rotated:")
        print_matrix(test_matrix)