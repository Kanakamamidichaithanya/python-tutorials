import turtle as t
import random
from turtle import Screen
screen = Screen()
timmy = t.Turtle()
t.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colour = (r,g,b)
    return random_colour
# colours = ["red", "black", "orange", "brown" , "green"]
for i in range(200):
    timmy.pensize(10)
    timmy.color(random_colour())
    direction = [0,90,180,270]
    timmy.forward(30)
    timmy.setheading(random.choice(direction))
    timmy.speed("fastest")
    
screen.exitonclick()