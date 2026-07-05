print("\n🌀 Fibonacci Series Generator")
print("-" * 40)

terms = int(input("🔢 Enter the number of terms: "))

first = 0
second = 1

print("\n📋 Fibonacci Series:")

if terms <= 0:
    print("❌ Please enter a positive number.")
elif terms == 1:
    print(first)
else:
    for i in range(terms):
        print(first, end=" ")
        next_number = first + second
        first = second
        second = next_number

print("\n" + "-" * 40)
print("✅ Program Completed Successfully!")
