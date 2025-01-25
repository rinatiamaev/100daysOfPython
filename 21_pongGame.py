from turtle import Screen, Turtle
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Super PingPong")
screen.setup(800, 600)
screen.tracer(0)

# <---- CLASS BALL --------->
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def change_move_y(self):
        self.y_move *= -1
    
    def change_move_x(self):
        self.x_move *= -1
    
    def reset_pos(self):
        self.home()

# <---- CLASS BALL --------->

# <---- CLASS PADDLE --------->
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(4, 1)
        self.color("white")
        self.penup()

    def setpos(self, x, y):
        self.goto(x, y)
    
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


# <---- CLASS PADDLE --------->

# <---- CLASS SCORE --------->
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()  # Clear the previous score
        self.goto(-150, 230)
        self.write(self.left_score, align="center", font=("Arial", 50, "bold"))
        self.goto(150, 230)
        self.write(self.right_score, align="center", font=("Arial", 50, "bold"))

    def increase_left_score(self):
        self.left_score += 1
        self.update_score()

    def increase_right_score(self):
        self.right_score += 1
        self.update_score()

# <---- CLASS SCORE --------->

# <---- CLASS WINER --------->
class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
    
    def print_msgR(self):
        self.goto(0,0)
        self.write("Right win.", align="center", font=("Arial", 16, "bold"))

    def print_msgL(self):
        self.goto(0,0)
        self.write("Left win.", align="center", font=("Arial", 16, "bold"))
# <---- CLASS WINER --------->

rightPaddle = Paddle()
rightPaddle.setpos(360, 0)

leftPaddle = Paddle()
leftPaddle.setpos(-360, 0)

ball = Ball()

scoreboard = Score()

game_over = GameOver()



screen.listen()
screen.onkey(rightPaddle.go_up, "w")
screen.onkey(rightPaddle.go_down, "s")
screen.onkey(leftPaddle.go_up, "Up")
screen.onkey(leftPaddle.go_down, "Down")
game_on = True

while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # detect collision up and down wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_move_y()

    # detect collision with Paddle
    if ball.distance(rightPaddle) < 50 and ball.xcor() > 330:
        ball.change_move_x()
    if ball.distance(leftPaddle) < 50 and ball.xcor() < -330:
        ball.change_move_x()

    # detect left goal
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.increase_left_score()


    # detect right goal 
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.increase_right_score()

    # detect winer
    if scoreboard.right_score == 5:
        game_on = False
        game_over.print_msgR()


    if scoreboard.left_score == 5:
        game_on = False
        game_over.print_msgL()


screen.exitonclick()