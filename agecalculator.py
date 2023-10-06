import datetime

def greet():
    print("Welcome to the Age Calculator!")
    print("Enter your year of birth to calculate your age.")

def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    return age

def calculate_age_in_months(age):
    months = age * 12
    return months

def calculate_age_in_days(age):
    days = age * 365  # Approximation for simplicity
    return days

while True:
    greet()
    try:
        birth_year = int(input("Enter your year of birth (e.g., 1990): "))
        age = calculate_age(birth_year)

        if age < 0:
            print("Invalid birth year. Please enter a valid year.")
        else:
            print("Your age is {} years.".format(age))
            print("Your age is approximately {} months.".format(calculate_age_in_months(age)))
            print("Your age is approximately {} days.".format(calculate_age_in_days(age)))

    except ValueError:
        print("Invalid input. Please enter a valid year.")

    choice = input("Do you want to calculate another age? (yes/no): ")
    if choice.lower() != 'yes':
        print("Goodbye!")
        break
