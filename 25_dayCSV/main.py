# # with open("weather_data.csv") as weather_data:
# #     data = weather_data.readlines()
# #     print(data)

# # import csv

# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")

# # Columns
# # data_dict = data.to_dict()
# # print(data_dict)

# # data_list = data["temp"].to_list()
# # average_temp = round(data["temp"].mean(), 1)

# # print(f"Average temp = {average_temp}")

# # max_temp = data["temp"].max()
# # print(f"max_temp = {max_temp}")
# # print(data.condition)

# # Row

# # print(data[data["day"] == "Monday"])
# # print(data[data["temp"] == data["temp"].max()])


# monday = data[data["day"] == "Monday"]
# print((monday.temp)*1.8 + 32)

import pandas

data = pandas.read_csv("Squirrel_Data.csv")

skin_color = data["Primary Fur Color"].to_list()
countGray = skin_color.count("Gray")
countCinnamon = skin_color.count("Cinnamon")
countBlack = skin_color.count("Black")

# grey_squirrels = data[data["Primary Fur Color"] == "Gray"]


data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [countGray, countCinnamon, countBlack]
}

dfSquirrels = pandas.DataFrame(data_dict)
dfSquirrels.to_csv("squirrels.csv")