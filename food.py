'''import main
width = main.width
height = main.height
food_turtles = main.food_turtles'''
food_list = {}
from random import randint
import turtle 
def farm(count):
    from main import width,height
    for x in range(count):
        x = randint(-width/2,width/2)
        y = randint(-height/2,height/2)
        name = str(x)+str(y)
        food_list[name] = Food(x,y)


class Food:
    def __init__(self,x,y):
        #import main
        from main import food_turtles
        name = str(x)+str(y)
        food_turtles[name] = turtle.Turtle()
        food_turtles[name].penup()
        food_turtles[name].setx(x)
        self.x = x
        self.y =y
        food_turtles[name].sety(y)
        food_turtles[name].shape("circle")
        food_turtles[name].color("green")
        food_turtles[name].shape("circle")
        food_turtles[name].shapesize(0.05,0.05,0.05)
        
