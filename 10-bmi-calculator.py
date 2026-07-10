print("\BMI Calculator")
print("-" * 40)

name = input("👤 Enter Your Name : ")
weight = float(input("⚖️ Enter Weight (kg) : "))
height = float(input("📏 Enter Height (m) : "))

bmi = weight / (height ** 2)

print("\n📊 BMI REPORT")
print("-" * 40)
print(f"Name : {name}")
print(f"BMI  : {bmi:.2f}")

if bmi < 18.5:
    print("Category : Underweight 🟡")
elif bmi < 25:
    print("Category : Normal Weight 🟢")
elif bmi < 30:
    print("Category : Overweight 🟠")
else:
    print("Category : Obese 🔴")

print("-" * 40)
print("💪 Stay Healthy & Keep Exercising!")
print("=" * 40)
