import time

class Snake():
    def __init__(self,set_width,set_height,snake,food):
        self.set_width=set_width
        self.set_height=set_height
        self.food=food
        self.snake=snake  
    
    def move_forward(self):
        pos_list=[]
        for idx,s in enumerate(self.snake):
            pos=s.position()
            pos_list.append(pos)
            if idx==0:
                heading=s.heading()
                if int(heading)==90:
                    s.right(90)
                elif int(heading)==270:
                    s.left(90)
                s.goto(pos[0]+20,pos[1])
            else:
                pos=pos_list[idx-1]
                s.goto(pos)


    def move_up(self):
        pos_list=[]
        for idx,s in enumerate(self.snake):
            pos=s.position()
            pos_list.append(pos)
            if idx==0:
                heading=s.heading()
                if int(heading)==0:
                    s.left(90)
                elif int(heading)==180:
                    s.right(90)
                s.goto(pos[0],pos[1]+20)
            else:
                pos=pos_list[idx-1]
                s.goto(pos)


    def move_down(self):
        pos_list=[]
        for idx,s in enumerate(self.snake):
            pos=s.position()
            pos_list.append(pos)
            if idx==0:
                heading=s.heading()
                if int(heading)==0:
                    s.right(90)
                elif int(heading)==180:
                    s.left(90)
                s.goto(pos[0],pos[1]-20)
            else:
                pos=pos_list[idx-1]
                s.goto(pos)


    def move_backwards(self):
        pos_list=[]
        for idx,s in enumerate(self.snake):
            pos=s.position()
            pos_list.append(pos)
            if idx==0:
                heading=s.heading()
                if int(heading)==90:
                    s.left(90)
                elif int(heading)==270:
                    s.right(90)
                s.goto(pos[0]-20,pos[1])
            else:
                pos=pos_list[idx-1]
                s.goto(pos)


    def move_constant(self):
        speed=0.0
        pos_list=[]
        for idx,s in enumerate(self.snake):
            time.sleep(speed)
            pos=s.position()
            pos_list.append(pos)
            if idx==0:
                heading = s.heading()
                if heading == 0:
                    s.goto(pos[0]+20,pos[1])
                elif heading == 180:
                    s.goto(pos[0]-20,pos[1])
                elif heading == 90:
                    s.goto(pos[0],pos[1]+20)
                elif heading == 270:
                    s.goto(pos[0],pos[1]-20)
                if self.hit_the_wall(pos):
                    return("wall")
                if self.consume_the_food(pos):
                    return(pos)
            else:
                pos=pos_list[idx-1]
                s.speed("fastest")
                s.goto(pos)
        return(False)
    
    def consume_the_food(self, pos):
        x,y=self.food.food.position()
        marg=10
        if abs(pos[0]-x)<=marg and abs(pos[1]-y)<=marg:
            return(True)
        else:
            return(False)
    
    def hit_the_wall(self, pos):
        if pos[0]<=-self.set_width/2+10 or pos[0]>=self.set_width/2-10 or pos[1]<=-self.set_height/2 or pos[1]>=self.set_height/2:
            return(True)
        else:
            return(False)






   
    