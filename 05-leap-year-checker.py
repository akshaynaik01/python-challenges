print("\n🌍 Welcome to Leap Year Checker")
print("-" * 40)

year = int(input("📅 Enter a Year : "))

print("\nChecking...")

if year % 400 == 0:
    print(f"✅ {year} is a Leap Year.")
elif year % 100 == 0:
    print(f"❌ {year} is NOT a Leap Year.")
elif year % 4 == 0:
    print(f"✅ {year} is a Leap Year.")
else:
    print(f"❌ {year} is NOT a Leap Year.")

print("-" * 40)
print("✨ Thank you for using the program!")
