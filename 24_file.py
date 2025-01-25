# with open("my_file.txt") as file:
#     contants = file.read()
#     print(contants)

with open("my_file.txt", mode="w") as file:
    file.write("Hello everybody")