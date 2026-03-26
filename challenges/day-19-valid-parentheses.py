"""Day 19 Challenge: Valid Parentheses Checker

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: "()"        Output: True
Input: "()[]{}"    Output: True
Input: "(]"        Output: False
Input: "([)]"      Output: False
Input: "{[]}"      Output: True
Input: ""          Output: True (empty string is valid)

Time Complexity:
- Stack-based: O(n)
- Counter-based: O(n)
- Recursive: O(n^2) due to repeated slicing

Space Complexity:
- Stack-based: O(n)
- Counter-based: O(1)
- Recursive: O(n) due to call stack
"""

def is_valid_stack(s: str) -> bool:
    """
    Check if parentheses are valid using a stack.

    This is the most efficient and commonly used approach.

    Time Complexity: O(n) - single pass through the string
    Space Complexity: O(n) - stack can grow up to n/2 in worst case
    """
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            # Ignore non-bracket characters
            continue

    return len(stack) == 0

def is_valid_counter(s: str) -> bool:
    """
    Check if only round parentheses () are valid using a counter.

    This approach works ONLY for strings containing '(' and ')'.
    It cannot handle mixed bracket types like {}, [], so it's limited.

    Time Complexity: O(n)
    Space Complexity: O(1) - only uses a counter variable
    """
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

def is_valid_recursive(s: str) -> bool:
    """
    Check if parentheses are valid using recursion.

    This approach repeatedly finds and removes the innermost
    matching pair until the string is empty (valid) or no
    more pairs can be found (invalid).

    Time Complexity: O(n^2) - each pass takes O(n), and we do up to n/2 passes
    Space Complexity: O(n) - due to recursive call stack and string creation
    """
    if len(s) == 0:
        return True

    # Find and remove innermost pairs
    new_s = s.replace('()', '').replace('{}', '').replace('[]', '')

    if new_s == s:
        # No changes made, means invalid
        return False

    return is_valid_recursive(new_s)

if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("{[]}", True),
        ("", True),
        ("((()))", True),
        ("({[]})", True),
        ("[{()}]", True),
        ("(]", False),
        ("([)]", False),
        ("(())(", False),
        (")()", False),
        ("({[})", False),
        ("a(b)c[d]e{f}g", True),
        ("(a+b)*(c-d)", True),
        ("((a+b)", False),
        ("abc", True),
    ]

    print("Testing is_valid_stack (Stack-based approach):")
    print("=" * 50)
    for i, (test_input, expected) in enumerate(test_cases, 1):
        result = is_valid_stack(test_input)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: Input: {repr(test_input):20} | Expected: {expected}, Got: {result} | {status}")

    print("\nTesting is_valid_counter (Counter-based approach - only for ()): ")
    print("=" * 50)
    counter_tests = [
        ("()", True),
        ("(())", True),
        ("((()))", True),
        ("()()()", True),
        ("(())(", False),
        (")()", False),
        ("(()))", False),
    ]
    for i, (test_input, expected) in enumerate(counter_tests, 1):
        result = is_valid_counter(test_input)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: Input: {repr(test_input):15} | Expected: {expected}, Got: {result} | {status}")

    print("\nTesting is_valid_recursive (Recursive approach):")
    print("=" * 50)
    recursive_tests = [
        ("()", True),
        ("()[]{}", True),
        ("{[]}", True),
        ("", True),
        ("((()))", True),
        ("({[]})", True),
        ("(]", False),
        ("([)]", False),
    ]
    for i, (test_input, expected) in enumerate(recursive_tests, 1):
        result = is_valid_recursive(test_input)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: Input: {repr(test_input):20} | Expected: {expected}, Got: {result} | {status}")

    print("\nComparing all approaches:")
    print("=" * 50)
    for test_input, expected in test_cases:
        stack_res = is_valid_stack(test_input)
        recursive_res = is_valid_recursive(test_input) if len(test_input) <= 30 else "N/A"

        if stack_res == expected:
            print(f"Input: {repr(test_input):20} | Stack: {stack_res} (correct)")
        else:
            print(f"Input: {repr(test_input):20} | Stack: {stack_res} (WRONG - expected {expected})")
