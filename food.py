import random
import turtle
class Food():
    def __init__(self) -> None:
        # self.food=self.new_food()
        # pass
    # def new_food(self):
        self.food=turtle.Turtle()
        self.food.shape("circle")
        self.food.color("blue")
        self.food.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.food.speed("fastest")
        self.food.penup()
        self.food.hideturtle()
        x=random.randint(-28,28)
        x*=10
        y=random.randint(-28,28)
        y*=10
        self.food.goto(x,y)
        self.food.showturtle()
        print(f"food is created at {x,y}")
        # return(food)
    # def delete_turtle(self,food_turtle):
    #     food_turtle.hideturtle()
    #     food_turtle.clear()
        



