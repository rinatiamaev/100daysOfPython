from turtle import Turtle, Screen
import time, random
START_POS = [(0,0),(-20,0),(-40,0),]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Best Snack game")
screen.tracer(0)

# <----Class SNACK---->

class Snack:
    
    def __init__(self):
        self.segments = []
        self.create_snack()
        self.head = self.segments[0]

    def create_snack(self):
        for pos in START_POS:
            self.add_seg(pos)

    def add_seg(self, position):
        seg = Turtle()
        seg.shape("square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.segments.append(seg)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snack()
        self.head = self.segments[0]

    def extend_snack(self):
        self.add_seg(self.segments[-1].position())



    def move(self):
            for seg in range(len(self.segments) - 1, 0 , -1):
                x_cor = self.segments[seg - 1].xcor()
                y_cor = self.segments[seg - 1].ycor()
                self.segments[seg].goto(x_cor, y_cor)
            self.head.fd(20)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
# <----Class SNACK---->

# <----Class FOOD---->

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("pink")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

# <----Class FOOD---->

my_snack = Snack()
food = Food()

screen.listen()
screen.onkey(my_snack.up, "w")
screen.onkey(my_snack.down, "s")
screen.onkey(my_snack.left, "a")
screen.onkey(my_snack.right, "d")
game_on = True

score_turtle = Turtle()
score_turtle.hideturtle()
score_turtle.color("white")
score_turtle.penup()
score_turtle.goto(-280, 260)  

# <----Class scoreboard---->
class PointsCount(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open("snack_score.txt") as file:
            self.high_score_string = file.read()
        self.high_score = int(self.high_score_string)
        self.clear()
        self.update_screen()
        self.hideturtle()

    def update_screen(self):
        self.clear()
        self.write(f"Points = {self.score} | Hight score = {self.high_score}", align="center", font=("Arial", 16, "bold"))

    def increment_score(self):
        self.score += 1
        self.update_screen()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_screen()

# <----Class scoreboard---->

# <----GAMEOVER---->
class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.hideturtle()
    
    def print_msg(self):
        self.clear()  # Clear any previous message
        self.write("GAME OVER.", align="center", font=("Arial", 16, "bold"))
    
    def clear_msg(self):
        self.clear()  # Clear the "GAME OVER" message
# <----GAMEOVER---->

score = PointsCount()
game_over = GameOver()

while game_on:
    screen.update()
    time.sleep(0.1)
    my_snack.move()
    high_score_str = str(score.high_score)
    with open("snack_score.txt", mode="w") as file:
        file.write(high_score_str)
    # Detect collision with food
    if my_snack.head.distance(food) < 15:
        food.refresh()
        my_snack.extend_snack()
        score.increment_score()
        
    # Detect collision with wall
    if my_snack.head.xcor() > 280 or my_snack.head.xcor() < -280 or my_snack.head.ycor() > 280 or my_snack.head.ycor() < -280:
        game_on = False  
        game_over.print_msg() 
        time.sleep(2)  
        game_over.clear_msg()
        score.reset()
        my_snack.reset()  
        game_on = True

    # Detect collision with itself
    for seg in my_snack.segments[1:]:
        if my_snack.head.distance(seg) < 10:
            game_on = False
            game_over.print_msg()
            time.sleep(2) 
            game_over.clear_msg()
            score.reset() 
            my_snack.reset() 
            game_on = True  

screen.exitonclick()
