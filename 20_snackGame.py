from turtle import Turtle, Screen
import time
start_pos = [(0,0),(-20,0),(-40,0),]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Best Snack game")
screen.tracer(0)


class Snack:
    
    def __init__(self):
        self.segments = []
        self.create_snack()
        self.head = self.segments[0]

    def create_snack(self):
        
        for pos in start_pos:
            seg = Turtle()
            seg.shape("square")
            seg.color("white")
            seg.penup()
            seg.goto(pos)
            self.segments.append(seg)


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



my_snack = Snack()
screen.listen()
screen.onkey(my_snack.up, "w")
screen.onkey(my_snack.down, "s")
screen.onkey(my_snack.left, "a")
screen.onkey(my_snack.right, "d")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    my_snack.move()

screen.exitonclick()