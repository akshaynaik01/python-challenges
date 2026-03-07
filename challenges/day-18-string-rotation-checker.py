def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

def is_rotation_manual(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i:] + s1[:i] == s2:
            return True
    return False

def test_rotation():
    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("hello", "lohel", True),
        ("python", "thonpy", True),
        ("abc", "cab", True),
        ("abc", "acb", False),
        ("test", "ttes", True),
        ("same", "same", True),
        ("different", "length", False),
        ("", "", True),
        ("a", "a", True)
    ]
    
    print("Testing is_rotation function:")
    for s1, s2, expected in test_cases:
        result = is_rotation(s1, s2)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: is_rotation('{s1}', '{s2}') = {result} (expected {expected})")
    
    print("\nTesting is_rotation_manual function:")
    for s1, s2, expected in test_cases:
        result = is_rotation_manual(s1, s2)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: is_rotation_manual('{s1}', '{s2}') = {result} (expected {expected})")

if __name__ == "__main__":
    test_rotation()
