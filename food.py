from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.goto_random_location()

    def goto_random_location(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        # Go To a random location each time the snake touches the food
