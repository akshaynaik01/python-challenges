print("Currency Converter")
print("=" * 45)

print("Available Currencies")
print("1. USD 🇺🇸")
print("2. EUR 🇪🇺")
print("3. GBP 🇬🇧")
print("4. JPY 🇯🇵")

print("-" * 45)

amount = float(input("Enter Amount in INR (₹): "))
choice = int(input("Choose Currency (1-4): "))

usd = 0.012
eur = 0.010
gbp = 0.0087
jpy = 1.74

print("\n📊 Conversion Result")
print("-" * 45)

if choice == 1:
    print(f"₹{amount:.2f} = ${amount * usd:.2f} USD")
elif choice == 2:
    print(f"₹{amount:.2f} = €{amount * eur:.2f} EUR")
elif choice == 3:
    print(f"₹{amount:.2f} = £{amount * gbp:.2f} GBP")
elif choice == 4:
    print(f"₹{amount:.2f} = ¥{amount * jpy:.2f} JPY")
else:
    print("❌ Invalid Choice!")

print("=" * 45)
print("✅ Thank You for Using Currency Converter!")
