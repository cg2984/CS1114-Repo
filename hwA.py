"""
CS-UY 1114
Homework A
starter code
"""

import math
import turtle

class Point:
    def __init__(self, x, y):
        # sig: Point, float, float -> NoneType
        # Construct a new Point from coordinates
        self.x = x
        self.y = y
    def move(self, horiz, vert):
        # sig: Point, float, float -> NoneType
        # Move the point by some amount in both axes
        self.x += horiz
        self.y += vert
    def draw(self):
        # sig: Point -> NoneType
        # Use turtle to draw the point as a dot on the screen
        turtle.up()
        turtle.goto(self.x, self.y)
        turtle.down()
        turtle.dot(5)
    def distance(self, other):
        # sig: Point, Point -> float
        # Calculate the distance between the point and
        # another point
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

class Rectangle:
    def __init__(self, upperleft, lowerright):
        # sig: Rectangle, Point, Point -> NoneType
        # Construct a new Rectangle from two points
        self.upperleft = upperleft
        self.lowerright = lowerright
    def diagonal_length(self):
        # sig: Rectangle -> float
        # Return the distance between the upper left point
        # and the lower right point
        return Point.distance(self.upperleft, self.lowerright)        
    def draw(self):
        turtle.showturtle()
        turtle.penup()
        turtle.goto(self.upperleft.x,self.upperleft.y)
        turtle.pendown()
        turtle.goto(self.upperleft.x,self.lowerright.y)
        turtle.goto(self.lowerright.x,self.lowerright.y)
        turtle.goto(self.lowerright.x,self.upperleft.y)
        turtle.goto(self.upperleft.x,self.upperleft.y)
    def width(self):
        # sig: Rectangle -> float
        # Return the (positive) width of the rectangle
        return self.lowerright.x - self.upperleft.x
    def height(self):
        # sig: Rectangle -> float
        # Return the (positive) height of the rectangle
        return  self.upperleft.y-self.lowerright.y
    def area(self):
        return  self.height()*self.width()
    def move(self, horiz, vert):
        return Point.move(self.lowerright,horiz,vert)
        return Point.move(self.upperleft,horiz,vert)
    def overlaps(self, other):
        if self.lowerright.y > other.upperleft.y:
            print("self is above")
            return False
        if self.upperleft.y < other.lowerright.y:
            print("self is below")
            return False
        if self.lowerright.x < other.upperleft.x:
            print("self is to the right")
            return False
        if self.upperleft.x > other.lowerright.x:
            print("self is to the left")
            return False
        else:
            return True
    def intersection(self, other):   
        if not self.overlaps(other):
            return Rectangle(Point(0.0, 0.0), Point(0.0, 0.0))
        else:
            

class Line:
    def __init__(self,first,second):
        self.first = first
        self.second = second 
    def draw(self):
        turtle.penup()
        turtle.goto(self.first.x,self.first.y)
        turtle.pendown()
        turtle.goto(self.second.x,self.second.y)
    def slope(self):
        try:
            slope = (self.first.y-self.second.y)/(self.first.x-self.second.x)
            return slope
        except:
            return "Value Error: There is no slope!"
        
def line_slope_test():
    l1 = Line(Point(1.0, 1.0),Point(3.0, 3.0))
    l2 = Line(Point(1.0, 1.0),Point(-3.0, 3.0))
    print("l1 has slope " + str(l1.slope()))
    print("l2 has slope " + str(l2.slope()))

def point_move_test():
    turtle.hideturtle()
    p1 = Point(50.0, 40.0)
    turtle.color("black")
    for _ in range(20):
        p1.draw()
        p1.move(5.0, 5.0)

def rectangle_area_test():
    r1 = Rectangle(Point(50.0, 260.0), Point(160.0, 150.0))
    print("r1 has width " + str(r1.width()))
    print("r1 has height " + str(r1.height()))
    print("r1 has area " + str(r1.area()))
    print("r1 has diagonal length: " + str(r1.diagonal_length()))

def rectangle_move_test():
    turtle.hideturtle()
    r1 = Rectangle(Point(50.0, 260.0), Point(160.0, 150.0))
    for i in range(20):
        turtle.color(["black", "green", "red"][i % 3])
        r1.draw()
        r1.move(5.0, 5.0)

def rectangle_draw_test():
    turtle.hideturtle()
    r1 = Rectangle(Point(10.0, 300.0),Point(90.0, 100.0))
    r2 = Rectangle(Point(70.0, 180.0), Point(200.0, 150.0))
    turtle.color("black")
    r1.draw()
    r2.draw()

def overlap_test():
    r1 = Rectangle(Point(10.0, 300.0),Point(90.0, 100.0))
    r2 = Rectangle(Point(70.0, 180.0), Point(200.0, 150.0))
    print("r1 and r2 overlap? " + str(r1.overlaps(r2)))
    r1.draw()
    r2.draw()

    r3 = Rectangle(Point(10.0, 300.0),Point(90.0, 100.0))
    r4 = Rectangle(Point(100.0, 180.0), Point(200.0, 150.0))
    print("r3 and r4 overlap? " + str(r3.overlaps(r4)))    

def intersection_test():
    turtle.hideturtle()
    r1 = Rectangle(Point(10.0, 300.0),Point(90.0, 100.0))
    r2 = Rectangle(Point(70.0, 180.0), Point(200.0, 150.0))
    turtle.color("black")
    r1.draw()
    r2.draw()
    turtle.color("red")
    theintersection = r1.intersection(r2)
    theintersection.draw()
    print("Area of interesection: " + str(theintersection.area()))

def main():
    line_slope_test()
main()
