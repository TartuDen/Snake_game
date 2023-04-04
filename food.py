import random
import turtle
class Food():
    def __init__(self) -> None:
        self.food=turtle.Turtle()
        self.food.hideturtle()
        self.food.shape("circle")
        self.food.color("blue")
        self.food.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.food.speed("fastest")
        self.food.penup()
        x=random.randint(-27,27)
        x*=10
        y=random.randint(-27,27)
        y*=10
        self.food.goto(x,y)
        self.food.showturtle()




