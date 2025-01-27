# # # with open("weather_data.csv") as weather_data:
# # #     data = weather_data.readlines()
# # #     print(data)

# # # import csv

# # # with open("weather_data.csv") as data_file:
# # #     data = csv.reader(data_file)
# # #     temperatures = []
# # #     for row in data:
# # #         if row[1] != "temp":
# # #             temperatures.append(int(row[1]))
# # #     print(temperatures)

# # import pandas

# # data = pandas.read_csv("weather_data.csv")

# # # Columns
# # # data_dict = data.to_dict()
# # # print(data_dict)

# # # data_list = data["temp"].to_list()
# # # average_temp = round(data["temp"].mean(), 1)

# # # print(f"Average temp = {average_temp}")

# # # max_temp = data["temp"].max()
# # # print(f"max_temp = {max_temp}")
# # # print(data.condition)

# # # Row

# # # print(data[data["day"] == "Monday"])
# # # print(data[data["temp"] == data["temp"].max()])


# # monday = data[data["day"] == "Monday"]
# # print((monday.temp)*1.8 + 32)

# import pandas

# data = pandas.read_csv("Squirrel_Data.csv")

# skin_color = data["Primary Fur Color"].to_list()
# countGray = skin_color.count("Gray")
# countCinnamon = skin_color.count("Cinnamon")
# countBlack = skin_color.count("Black")

# # grey_squirrels = data[data["Primary Fur Color"] == "Gray"]


# data_dict = {
#     "Fur Color" : ["Gray", "Cinnamon", "Black"],
#     "Count" : [countGray, countCinnamon, countBlack]
# }

# dfSquirrels = pandas.DataFrame(data_dict)
# dfSquirrels.to_csv("squirrels.csv")

import pandas
import turtle

# Set up the screen and map image
screen = turtle.Screen()
screen.title("U.S. State Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load state data
states = pandas.read_csv("50state.csv")
all_states = states.state.to_list()

# Create a separate turtle for writing text
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()

# Game state variables
game_on = True
guessed_states = []

while game_on:
    # Prompt user for a state name
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's the name of a state?").title()
    
    if answer_state == "Exit":
        break  # Exit the game when "Exit" is typed
    
    # Check if the answer is correct and not already guessed
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        
        # Get the state data
        state_data = states[states["state"] == answer_state]
        x = int(state_data["x"].values[0])
        y = int(state_data["y"].values[0])
        
        # Write the state name on the map using the text turtle
        text_turtle.goto(x, y)
        text_turtle.write(answer_state, align="center", font=("Arial", 12, "normal"))
    
    # End the game if all states are guessed
    if len(guessed_states) == len(all_states):
        game_on = False

# Close the screen on click
screen.exitonclick()



