# # list = [1,2, 3]
# # new_list = []
# # # for n in list:
# # #     add1 = n + 1
# # #     new_list.append(add1)

# # new_list = [n + 2 for n in list]


# # print(new_list)

# # name = "HIVE HELSINKI"

# # name_list = [letter for letter in name]
# # print(name_list)


# # list_range = [n * 2 for n in range(1, 5)]
# # print(list_range)

# # real_madrid = ["Mbappe", "Vini", "Lunin", "Modrich"]

# # short_names = [name.upper() for name in real_madrid if len(name) > 4]

# # print(short_names)


# # nbrs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# # squar_nbr = [n * n for n in nbrs]

# # print(squar_nbr)

# # even_nbrs = [n for n in nbrs if n % 2 == 0]

# # print(even_nbrs)

# # # result [3, 6, 5, 33, 12, 7, 42, 13]

# # txtfile1=open('file1.txt')

# # L1=[]
# # for line in txtfile1:
# #     L1.append(line.rstrip())

# # print(L1)

# # txtfile2=open('file2.txt')

# # L2=[]
# # for line in txtfile2:
# #     L2.append(line.rstrip())

# # print(L2)
# # result = [int(n) for n in L1 if n in L2]
# # print(result)

# # txtfile1.close()
# # txtfile2.close()

# # import random
# # goal_make = {player : random.randint(0,23) for player in real_madrid}

# # gold_ball = {player : goal for player, goal in goal_make.items() if goal > 10}

# # print(gold_ball)

# # sentence = "What is the Airspeed Velocity of an Unlanden Swallow?"
# # s = sentence.split()
# # dict_word = {word:len(word) for word in s }
# # print(dict_word)

# # weather_helsinki_celc = {
# #     "Monday": -2,
# #     "Tuesday": -1,
# #     "Wednesday": 0,
# #     "Thursday": 1,
# #     "Friday": -2,
# #     "Saturday": -3,
# #     "Sunday": -10,
# # }

# # weather_helsinki_farin = {day:(t*9/5 + 32) for (day,t)  in weather_helsinki_celc.items()}
# # print(weather_helsinki_farin)

# real_madrid = {
#     "players" : ["Mbappe", "Kamovinga", "Vini", "Belingham"],
#     "goals" :[16, 4, 12, 11]
# }

# import pandas

# real_madrid_data_frame = pandas.DataFrame(real_madrid)
# print(real_madrid_data_frame)

# for (index, row) in real_madrid_data_frame.iterrows():
#     if row.players == "Mbappe":
#         print(row.goals)

