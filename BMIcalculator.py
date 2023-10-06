#EMMANUEL YATOR
#SCT211-0622/2022


def calculate_bmi(weight_kg, height_cm):
    # Convert height from cm to meters
    height_m = height_cm / 100

    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    else:
        return "Overweight"

while True:
    print("Welcome to the BMI Calculator!")
    try:
        weight_kg = float(input("Enter your weight in kilograms: "))
        height_cm = float(input("Enter your height in centimeters: "))

        if weight_kg <= 0 or height_cm <= 0:
            print("Invalid input. Please enter valid values.")
        else:
            bmi = calculate_bmi(weight_kg, height_cm)
            result = interpret_bmi(bmi)
            print("Your BMI is {:.2f}".format(bmi))
            print("You are categorized as:", result)

    except ValueError:
        print("Invalid input. Please enter valid numerical values.")

    choice = input("Do you want to calculate another BMI? (yes/no): ")
    if choice.lower() != 'yes':
        print("Goodbye!")
        break
