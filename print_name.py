from turtle import Turtle
import pandas
ALIGNMENT = "center"
FONT = ("Courier", 10, "bold")


class PrintName(Turtle):

    def __init__(self, position,  state_name):
        super().__init__()
        self.color("black")
        self.penup()
        self.ht()
        self.goto(position)
        self.state_name = state_name

    def show_name(self):
        self.write(f"{self.state_name}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.write("Well done, you guessed all of them ^_^", align=ALIGNMENT, font=("Courier", 25, "bold"))
