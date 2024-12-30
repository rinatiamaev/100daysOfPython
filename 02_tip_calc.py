print("Welcome to the tip calculator.")
total_bill = float(input("What is your total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? $"))
people = int(input("How many people to split the bill? "))
tip = total_bill / 100 * tip_percentage
total_bill += tip
bill_per_person = total_bill / people
print(f"Each person should pay: ${bill_per_person:.2f}")
