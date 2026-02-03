"""
Day 3 Challenge: Armstrong Number Checker
An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
Example: 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153
"""

def is_armstrong_number(num):
    """
    Check if a number is an Armstrong number.
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if the number is an Armstrong number, False otherwise
    """
    # Convert number to string to get digits
    digits = str(num)
    num_digits = len(digits)
    
    # Calculate sum of each digit raised to the power of number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    return sum_of_powers == num


# Test cases
if __name__ == "__main__":
    test_cases = [
        (153, True),      # 1^3 + 5^3 + 3^3 = 153
        (370, True),      # 3^3 + 7^3 + 0^3 = 370
        (371, True),      # 3^3 + 7^3 + 1^3 = 371
        (407, True),      # 4^3 + 0^3 + 7^3 = 407
        (1634, True),     # 1^4 + 6^4 + 3^4 + 4^4 = 1634
        (8208, True),     # 8^4 + 2^4 + 0^4 + 8^4 = 8208
        (9474, True),     # 9^4 + 4^4 + 7^4 + 4^4 = 9474
        (100, False),     # Not an Armstrong number
        (123, False),     # Not an Armstrong number
        (9, True),        # 9^1 = 9 (single digit)
    ]
    
    print("Armstrong Number Checker - Test Results:")
    print("=" * 50)
    
    for num, expected in test_cases:
        result = is_armstrong_number(num)
        status = "PASS" if result == expected else "FAIL"
        print(f"Number: {num:6d} | Result: {result:5} | Expected: {expected:5} | {status}")
