from snake import Snake
from food import Food
import turtle
from food import Food



screen=turtle.Screen()
set_width=600
set_height=600
screen.setup(width=set_width, height=set_height)
screen.bgcolor("black")
screen.title("Python Snake")
food_=Food()



turtle.listen()



def create_snake(length=10):
    temp=[]
    start_pos=(0-len(temp)*20,0)
    for i in range(length):
        s=turtle.Turtle()
        s.penup()
        s.shape("square")
        s.color("white")
        s.goto(start_pos)
        temp.append(s)
    return(temp)

snake_list=(create_snake())

def update_snake(pos):
    global snake_list
    temp=[]
    for i in snake_list:
        temp.append(i)
    s=turtle.Turtle()
    s.hideturtle()
    s.penup()
    s.shape("square")
    s.color("white")
    s.goto(pos)
    s.showturtle()
    temp.append(s)
    
    snake_list=temp




while True:
    snake_=Snake(set_width,set_height,snake_list,food_)
    resp_from_snake=snake_.move_constant()
    if resp_from_snake == "wall":
        print("GAME OVER!")
        break
    elif resp_from_snake==False: 
        screen.update()
        turtle.onkey(snake_.move_forward, "Right")
        turtle.onkey(snake_.move_up, "Up")
        turtle.onkey(snake_.move_down, "Down")
        turtle.onkey(snake_.move_backwards, "Left")
    else:
        food_.food.hideturtle()
        food_.food.clear()
        food_=Food()
        update_snake(resp_from_snake)
screen.exitonclick()



    
