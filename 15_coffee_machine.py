import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

bank = {"Penny": {"cost": 1, "total" : 19},
        "Nickel": {"cost": 5, "total" : 7},
        "Dime": {"cost": 10, "total" : 20},
        "Quarter": {"cost": 25, "total" : 5},
        "Half": {"cost": 50, "total" : 7},
        "Dollar": {"cost": 100, "total" : 3},
        }

def checkResources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Not enough {item}")
            return False
    return True
    
def processCoins():
    print("Please insert coins")
    total = 0
    for coin in bank:
        count = int(input(f"How many {coin}: "))
        bank[coin]["total"] += count
        total += count * bank[coin]["cost"]
        total = float(total)
    return total

def transactionSuccess(coffeeCost, moneyReceived):
    if moneyReceived > coffeeCost:
        change = round(moneyReceived - coffeeCost, 2)
        print("Transaction success!")
        return True
    else:
        print("Not enough money")
        return False

def makeCoffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("Your coffee prepare")    
    time.sleep(3)
    print(f"Here is your {drink_name} ☕️. Enjoy!")

print("Welcome to best coffee machine!")
order = input("Choice your coffee: (espresso/latte/cappuccino)")
if order in MENU:
    drink = MENU[order]
    ingredients = drink["ingredients"]
    if checkResources(ingredients):
        print(f"The cost of {order} is ${drink['cost']}.")
    pay = processCoins()
    if transactionSuccess(drink["cost"], pay):
        makeCoffee(order, ingredients)
else:
    print("Cant prepare this coffee")