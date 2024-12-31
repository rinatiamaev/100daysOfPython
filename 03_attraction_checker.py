print("Attraction height checking program")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
totalPrice = 0
if height >= 120:
    print("Get fun and ride!")
else:
    print("sorry grow more and come back in future!")
if height >= 120 and age < 12:
    print("Your price 10$")
    totalPrice = 10
elif height >= 120 and (age >= 12 or age <= 18):
    print("Your price 15$")
    totalPrice = 15
else:
    print("Your price 20$")
    totalPrice = 20
photo = input("Do you want a photo for 5$ (yes/no)? ")
if (photo == "yes"):
    totalPrice += 5
print("Your total price is: " + str(totalPrice))
