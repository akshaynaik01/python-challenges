print("\n🔍 Prime Number Checker")
print("-" * 40)

number = int(input("🔢 Enter a number: "))

if number <= 1:
    print(f"\n❌ {number} is NOT a Prime Number.")
else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"\n✅ {number} is a Prime Number.")
    else:
        print(f"\n❌ {number} is NOT a Prime Number.")

print("-" * 40)
print("🎉 Program Completed Successfully!")
