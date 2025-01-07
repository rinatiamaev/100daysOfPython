import operator

calc_dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def Calc():
    print("Welcome to calc! use num1, operator: + - * / and num2")
    while True:
        try:
            n1 = float(input("Type number 1: "))
            op = input("Type operator: ")
            n2 = float(input("Type number 2: "))
            if op not in calc_dict:
                print("wrong operator")
                continue
            operation = calc_dict[op]
            res = operation(n1, n2)
            print(f"{n1} {op} {n2} = {res}")
        except ZeroDivisionError: print("Division by zero!")
        again = input("New operation? type y/n: ").lower()
        if again != "y":
            print("Thanks you for using our calculator")
            break

# Calc()

stud_score = {
    "Anna" : 98,
    "Boris" : 50,
    "Fil" : 100,
    "Bob" : 86
}
stud_res = {}

def CheckStud():
    for student in stud_score:
        score = stud_score[student]
        if score in range(90, 101):
            stud_res[student] = "Best"
        elif score in range(60, 90):
            stud_res[student] = "good"
        else:
            stud_res[student] = "Bad"
    print(stud_res)

# CheckStud()

Capitals_dict = {
    "USA": "Washingtone",
    "Finland": "Helsinki",
    "Spain" : "Madrid",
    "Japan" : "Tokio"
}

MyTravel_dict = {
    "USA" : {"New York" : 2, "Florida" : 1, "Cansas" : 3},
    "Finland" : {"Helsinki": 5, "Turku" : 4 },
    "Spain" : {"Barselona" : 12, "Sevila" : 21},
    "Japan" : {"Tokio" : 6, "Osaka" : 8}
}

def CapitalChecker():
    for country, capital in Capitals_dict.items():
        if country in MyTravel_dict:
            visited_city = MyTravel_dict[country]
            if capital in visited_city:
                visits = visited_city[capital]
                print(f"You are visited {country} ({capital}) {visits} times")
CapitalChecker()

        