from turtle import Turtle, Screen
import random

colors = ["red", "yellow", "green", "blue", "black"]





is_race = False
screen = Screen()
screen.setup(600,400)
user_bet = screen.textinput(title="Make your bet: ", prompt="Select a color: ")
print(user_bet)


all_turtles = []
x = -250
y = -150
i = 0
for turtle_index in range (0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 50
    i +=1
    all_turtles.append(new_turtle)

def step_forward():
    new_turtle.fd(10)
def step_back():
    new_turtle.bk(10)
def step_left():
    new_turtle.lt(10)
def step_right():
    new_turtle.rt(10)
def clear_screen():
    new_turtle.clear()
    new_turtle.penup()
    new_turtle.home()
    new_turtle.pendown()

if user_bet:
    is_race = True
while is_race:
    for turtle in all_turtles:
        turtle.fd(random.randint(0,10))
    if turtle.xcor() > 235:
        is_race = False
        win_color = turtle.pencolor()
        if (win_color == user_bet):
            print("you are win!")
        else:
            print("You are lose")

screen.listen()
screen.onkey(step_forward, "w")
screen.onkey(step_back, "s")
screen.onkey(step_left, "a")
screen.onkey(step_right, "d")
screen.onkey(clear_screen, "c")











screen.exitonclick()