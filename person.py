people_list = {}
from random import randint
import turtle
from math import pi
def creator(size,speed,perception,name=""):
    from main import people_turtles,width,height
    name = name+str(size)+str(speed)+str(perception) 
    #print(name)
    people_list[name] = Person(size,speed,perception,name)
    people_turtles[name] = turtle.Turtle()
    people_turtles[name].penup()
    people_turtles[name].color("red")
    people_turtles[name].shape("circle")
    people_turtles[name].shapesize(size,size,1)
    people_turtles[name].setx(randint(-width/2,width/2))
    people_turtles[name].sety(randint(-height/2,height/2))
    #print(main.people_turtles[name].position,end="\n\n"    
    return people_turtles[name] ## Returns the child as a turtle object
def reproduce(mother_turtle):
    size = mother_turtle.size*range(1-mutation_rate,1+mutation_rate)
    speed =mother_turtle.speed*range(1-mutation_rate,1+mutation_rate)
    perception =mother_turtle.perception*range(1-mutation_rate,1+mutation_rate)
    child = creator(size,speed,perception,mother_turtle.name)
    child.position = mother_turtle.position
class Person:
    def __init__(self,size,speed, perception,name=""):
        self.size = size
        self.speed = speed
        self.perception = perception
        self.name = name
        self.energy = pi*size**2
        self.power = speed**2

def feed():
    from food import food_list
    from main import people_turtles,width,height,food_turtles

    from quadtree import nearest_neighbor

    for person_name in people_turtles.keys():
        foods = [[food_list[a].x+640,food_list[a].y+360] for a in food_list.keys()]
        person = people_turtles[person_name]
        if len(food_list) == 0:
            return
        destination = nearest_neighbor(person.xcor()+width/2,person.ycor()+height/2,people_list[person_name].perception,foods,width,height)
        if len(destination) == 0:
            continue
        
        required_energy =2*10**(-12)* people_list[person_name].power * ((person.xcor()-destination[0])**2 + (person.ycor() - destination[1])**2 )**0.5
        if people_list[person_name].energy < required_energy:
            people_turtles[person_name].hideturtle()
            '''del people_list[name]
            del people_turtles[name]
            '''
            continue
        person.goto(destination)
        people_list[person_name].energy += 3
        food_name = str(int(destination[0]))+str(int(destination[1]))
        food_turtles[food_name].hideturtle()
        del food_list[food_name]
        del food_turtles[food_name]

        
def kill(name):
    from main import people_turtles
    people_turtles[name].hideturtle()
    del people_list[name]
    del people_turtles[name]
   
