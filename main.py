# from turtle import Screen, Turtle
import turtle

screen=turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake")
turtle.listen()


def create_snake(length=3):
    temp=[]
    for i in range(length):
        s=turtle.Turtle()
        s.penup()
        s.shape("square")
        s.color("white")
        s.goto(0-len(temp)*20,0)
        temp.append(s)
    return(temp)

snake=(create_snake())


def move_forward():
    pos_list=[]
    for idx,s in enumerate(snake):
        pos=s.position()
        pos_list.append(pos)
        if idx==0:
            s.goto(pos[0]+20,pos[1])
        else:
            pos=pos_list[idx-1]
            s.goto(pos)
        print(idx, s.position())
    print("pos_list: ",pos_list)



def move_up():
    pass


# def move_down():
#     for each_block in (snake):
#         each_block.forward(10)
# def move_forward():
#     for each_block in (snake):
#         each_block.forward(10)

turtle.onkey(move_forward, "Right")
# turtle.onkey(move_up, "Up")
# turtle.onkey(move_down, "Left")
# turtle.onkey(move_forward, "Right")


screen.exitonclick()
