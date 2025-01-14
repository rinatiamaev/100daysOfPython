# from turtle import Turtle, Screen
# from random import random
# from prettytable import PrettyTable

# # john = Turtle()
# # john.shape("turtle")
# # john.color("deeppink")
# # john.position()
# # john.forward(100)

# # my_screen = Screen()
# # # t = Turtle()
# # for i in range(100):
# #     steps = int(random() * 100)
# #     angle = int(random() * 360)
# #     t.right(angle)
# #     t.fd(steps)

# # # t.screen.mainloop()
# # my_screen.bgcolor("lightblue")
# # my_screen.exitonclick()

# x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"]) 
# x.align["City name"] = "l" 
# # Left align city names 

# x.padding_width = 1 
# # One space between column edges and contents (default) 
# x.add_row(["Adelaide",1295, 1158259, 600.5]) 
# x.add_row(["Brisbane",5905, 1857594, 1146.4]) 
# x.add_row(["Darwin", 112, 120900, 1714.7]) 
# x.add_row(["Hobart", 1357, 205556, 619.5]) 
# x.add_row(["Sydney", 2058, 4336374, 1214.8])
# x.add_row(["Melbourne", 1566, 3806092, 646.9]) 
# x.add_row(["Perth", 5386, 1554769, 869.4]) 
# print(x)

# y = PrettyTable(["Campus Name", "City", "Students amount"])
# y.align = "r"
# y.add_row(["Hive", "Helsinki", 314])
# y.add_row(["school 21", "Moscow", 1001])
# y.add_row(["1331", "Morocco", 190])
# print (y)

import time

class MenuItem:
    def __init__(self, name, water, coffee, milk, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "coffee": coffee,
            "milk": milk
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="espresso", water=50, coffee=18, milk=0, cost=1.5),
            MenuItem(name="latte", water=250, coffee=18, milk=100, cost=2.5),
            MenuItem(name="cappuccino", water=200, coffee=18, milk=150, cost=3)
        ]
    def getItem(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def finding_drink(self, order_name):
        for item in self.menu:
            if order_name == item.name:
                return item
        print("This drink is unavailable")

class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
        
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

menu = Menu()
ready = CoffeeMaker()
print("Welcome to COFFEE MACHINE")
order = input("Please select a drink: " + menu.getItem())
drink = menu.finding_drink(order)

if drink:
    print(f"Your {drink.name} costs {drink.cost}")
else:
    print("Error")

if drink and ready.is_resource_sufficient(drink):
    print("Please insert a coin")
    money = MoneyMachine()
    received_money = money.process_coins()
    order_success = money.make_payment(drink.cost)
    if order_success:
        print("Your coffee is being prepared, please wait...")
        time.sleep(3)  # ожидание для имитации процесса приготовления
        ready.make_coffee(drink)  # передаем drink в метод make_coffee
    else:
        print("Not enough money.")
else:
    print("Not enough resources or drink unavailable.")
