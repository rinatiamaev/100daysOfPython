import random
print("Welcome to PY password generatore!!!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nb_char = int(input("How many letters password must contain? "))
nb_nums = int(input("How many numbers password must contain? "))
nb_symb = int(input("How many symbols password must contain? "))
password_list = []
for char in range(1, nb_char + 1):
    password_list.append(random.choice(letters))
for char in range(1, nb_nums + 1):
    password_list.append(random.choice(numbers))
for char in range(1, nb_symb + 1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"your password is: {password}")