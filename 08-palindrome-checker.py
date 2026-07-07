print("Palindrome Checker")
print("-" * 40)

text = input("Enter a word or number: ")

reverse_text = text[::-1]

print("\nChecking...")

if text == reverse_text:
    print(f"'{text}' is a Palindrome.")
else:
    print(f"'{text}' is NOT a Palindrome.")

print("-" * 40)
print("Program Completed Successfully!")
