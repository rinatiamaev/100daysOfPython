# try:
#     file = open("tester.txt")
#     my_dict = {"key": "value"}
#     print(my_dict["brrr"])
# except FileNotFoundError:
#     file = open("tester.txt", "w")
#     file.write("YoYo")
# except KeyError as error_message:
#     print(f"Wrong key {error_message}")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file was closed")

# height = float(input("Height = "))
# weight = float(input("Weight = "))

# if height > 3:
#     raise ValueError("Please check your height")

# bmi = weight / height ** 2
# print(bmi)

fruits = ["apple", "banana", "pear"]

def make_cake(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("wrong index")
    else:
        print(fruit + " pie")
make_cake(2)