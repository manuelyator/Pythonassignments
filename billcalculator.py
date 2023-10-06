# EMMANUEL YATOR
# REG NO: SCT211-0622/2022


def calculate_split_bill(total_bill, tip_percentage, num_people):
    tip_percentage /= 100  # Convert tip_percentage to a decimal
    tip_amount = total_bill * tip_percentage
    total_amount = total_bill + tip_amount
    amount_per_person = total_amount / num_people
    return round(amount_per_person, 2)


total_bill = float(input("Enter the total bill amount: $"))
print("Select tip percentage:")
print("1. 10%")
print("2. 12%")
print("3. 15%")
choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    tip_percentage = 10
elif choice == 2:
    tip_percentage = 12
elif choice == 3:
    tip_percentage = 15
else:
    print("Invalid choice. Please select 1, 2, or 3.")
    exit()

num_people = int(input("Enter the number of people splitting the bill: "))


amount_per_person = calculate_split_bill(total_bill, tip_percentage, num_people)
print(f"Each person should pay: ${amount_per_person}")
