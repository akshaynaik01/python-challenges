print("=" * 45)
print("      LARGEST OF THREE NUMBERS")
print("=" * 45)

# User Input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Display Result
print("\n===== RESULT =====")
print(f"The largest number is: {largest}")

print("=" * 45)
print("Program Completed Successfully!")
print("=" * 45)
