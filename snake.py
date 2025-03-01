from turtle import Turtle
STARTING_COORDINATES=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP= 90
DOWN= 270
LEFT= 180
RIGHT= 0

class Snake:
    
    def __init__(self):
        #list of the parts of the turtles
        self.segment=[]
        #method that creates a snake
        self.create_snake()
        #the snake head
        self.head=self.segment[0]
    def create_snake(self):
        #loop that places the snake at the beginnning coordinates
        for position in STARTING_COORDINATES:
            self.add_segment(position)
            
    def add_segment(self,position):
       #creates a new turtle aka snake square shaped
            new_segment = Turtle(shape="square")
            #modifies the segements color
            new_segment.color("red")
            #ensure when it doesn't draw when it moves
            new_segment.penup()
            #moves segment to the position stated aboce
            new_segment.goto(position)
            #moves the segment to the segment list
            self.segment.append(new_segment) 
        
    def extend(self):
        self.add_segment(self.segment[-1].position()) 
        
    def move(self):
        #loop that moves the segments
        for seg_num in range(len(self.segment) -1,0,-1):
            
            new_x= self.segment[seg_num -1].xcor()
            new_y= self.segment[seg_num -1].ycor()
            self.segment[seg_num ].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
                 
            
    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)
             
    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)
             
    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)
             
            
    