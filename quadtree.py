class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
class Rectangle:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def contains(self,point):
        return point.x > self.x - self.w and point.x < self.x + self.w and point.y > self.y - self.h and point.y < self.y + self.h

    def intersects(self,limit):
        return not ( limit.x - limit.w > self.x + self.w or limit.x + limit.w < self.x - self.w or  limit.y - limit.h > self.y + self.h or limit.y + limit.h < self.y - self.h )

class QuadTree:
    def __init__(self,boundary,capacity):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def insert(self,point):
        if not self.boundary.contains(point):
            return
        if len(self.points) < self.capacity:
            self.points.append(point)
        else:
            if not self.divided:
                self.subdivide()
            self.NorthWest.insert(point)
            self.NorthEast.insert(point)
            self.SouthWest.insert(point)
            self.SouthEast.insert(point)
    
    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h

        nw = Rectangle(x - w/2 , y - h/2 , w/2 , h/2)
        ne = Rectangle(x + w/2 , y - h/2 , w/2 , h/2)
        sw = Rectangle(x - w/2 , y + h/2 , w/2 , h/2)
        se = Rectangle(x + w/2 , y + h/2 , w/2 , h/2)
        
        self.NorthWest = QuadTree(nw,self.capacity)
        self.NorthEast = QuadTree(ne,self.capacity)
        self.SouthWest = QuadTree(sw,self.capacity)
        self.SouthEast = QuadTree(se,self.capacity)

        self.divided = True
    
    def query(self,limit):
        found = []
        if self.boundary.intersects(limit):   
            for p in self.points:
                if limit.contains(p):
                    found.append(p)
            if self.divided:
                found += self.NorthEast.query(limit) + self.NorthWest.query(limit) + self.SouthEast.query(limit) + self.SouthWest.query(limit)
        return found
        
from math import inf
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
#Food list must be 2-D array like [[1,5], [105,120],[98,269]]
def nearest_neighbor(person_x, person_y,perception,food_list,width,height):
    boundary = Rectangle(width/2,height/2,width/2,height/2)
    qt = QuadTree(boundary,4)
    for food in food_list:
        qt.insert(Point(food[0],food[1]))
    limit = Rectangle(person_x,person_y,perception,perception)
    near_foods = qt.query(limit)
    if len(near_foods) == 0:
        return []
    nearest_food = []
    nearest_food_distance = inf
    for n in near_foods:
        new_distance = distance(person_x, person_y, n.x, n.y)
        if new_distance < nearest_food_distance:
            nearest_food_distance = new_distance
            nearest_food = [n.x , n.y]
    return [nearest_food[0] -width/2 ,nearest_food[1]-height/2]
'''
foods = [[640,349],[1,1],[1,350],[630,360],[90,90]]
print(nearest_neighbor(640,360,600,foods,1280,720))
'''
    
