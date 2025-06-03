from turtle import Turtle

STARTING_POSITION = (-280 , 0)
MOVE_DISTANCE = 10
FINISH_LINE_X = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("pikachu.gif")
        self.shapesize(stretch_wid=0.5 , stretch_len=0.5)
        self.setheading(0)
        self.go_to_start()

    def move_right(self):
     if self.xcor() < 280:
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def move_left(self):
     if self.xcor() > -280:
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def move_up(self):
     if self.ycor() < 280:
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
     if self.ycor() > -280:
        self.setheading(270)
        self.forward(MOVE_DISTANCE)            

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.xcor() > FINISH_LINE_X:
            return True
        else:
            return False
        
