print("=" * 45)
print("          SIMPLE CALCULATOR")
print("=" * 45)

# User Input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

# Display Results
print("\n===== RESULTS =====")
print(f"Addition       : {addition}")
print(f"Subtraction    : {subtraction}")
print(f"Multiplication : {multiplication}")
print(f"Division       : {division}")

print("=" * 45)
print("Thank you for using the calculator!")
print("=" * 45)
