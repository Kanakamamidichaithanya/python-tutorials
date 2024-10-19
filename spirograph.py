from turtle import Turtle
import random
from turtle import Screen
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colour = (r,g,b)
    return random_colour
timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.speed("fastest")
for i in range(100):
    timmy.color(random_colour())
    timmy.circle(100)
    current_heading = timmy.heading()
    timmy.setheading(current_heading+10)
screen.exitonclick()