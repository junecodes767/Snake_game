#make the score board inherit the turtle class
#place text in the middle of the screen
#make the score board increase when the food was hit

from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.count=-1
        self.hideturtle()
        self. color("white")
        self.goto(-57,270)        
        self.update()
        
    def update(self):
        self.clear()
        self.count+=1
        self.write(f"Score Board:{self.count}",font=('Arial',18,'normal'))
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=('Arial',18,'normal'))