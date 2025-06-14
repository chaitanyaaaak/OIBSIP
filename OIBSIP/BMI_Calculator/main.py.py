def bmi_calculator():
    print("Welcome to the BMI Calculator!")
    while True:
        try:
            weight = float(input("Please enter your weight in kilograms: "))
            height = float(input("Please enter your height in meters: "))
            if weight <= 0 or height <= 0:
                print("Weight and height must be positive numbers.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter numeric values.\n")
            continue

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}\n")

        again = input("Would you like to calculate another BMI? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Thank you for using the BMI Calculator. Goodbye!")
            break
        print("-" * 40)

bmi_calculator()
