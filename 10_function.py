import operator

calc_ascii = '''
+-------------------------+
|   ASCII Calc 3000      |
+-------------------------+
|  [7] [8] [9]   [÷]     |
|  [4] [5] [6]   [×]     |
|  [1] [2] [3]   [-]     |
|  [0] [.] [=]   [+]     |
+-------------------------+

'''
print(calc_ascii)

calc_dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def Calc():
    print("Welcome to calc! use num1, operator: + - * / and num2")
    add_res = True
    n1 = float(input("Type first number: "))
    while add_res:
        try:
            op = input("Type operator: ")
            n2 = float(input("Type next number: "))
            if op not in calc_dict:
                print("wrong operator")
                continue
            operation = calc_dict[op]
            res = operation(n1, n2)
            print(f"{n1} {op} {n2} = {res}")
        except ZeroDivisionError: print("Division by zero!")
        again = input("Do you want add in result new operation? type y/n: ").lower()
        if again == "y":
            n1 = res
        else:
            add_res = False
            print("Thanks for using our calc")
            
Calc()

# def is_leap(year):
#     if  year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False

# def day_of_monts(m: int, y : int):
#     """take a month 1-12 and year from user input"""
#     month_no_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(y):
#         return month_leap[m - 1]
#     else:
#         return month_no_leap[m - 1]

# month = int(input("Type month: "))
# year = int(input("Type Year: "))
# day_in_month_of_year = day_of_monts(month, year)
# print(f"in month {month} of year: {year} have: {day_in_month_of_year} days")