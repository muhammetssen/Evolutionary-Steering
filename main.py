import turtle 
from tkinter import mainloop
people_turtles = {}
food_turtles = {}
from random import random,randint
width = 1280
height = 720
screen = turtle.Screen()
screen.screensize(width,height)
turtle.bgcolor("black")
mutation_rate = 0.25
import person
import food
from quadtree import nearest_neighbor
people_count = 200
food_count= 500
turtle.tracer(food_count)
food.farm(food_count)

turtle.tracer(people_count/2)
for x in range(people_count):
    person.creator(random()*1.5,random()*110000,random()*2000)
turtle.tracer(people_count/10)

while len(list(food_turtles.keys())) >0:
    person.feed()
print("done")
turtle.Screen().exitonclick()
