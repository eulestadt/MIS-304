# Name: Phoenix Wang
# Assignment Number: Final Project
# Date: 12/5/19
# Section: 9:30-11
# Description: Class for the cupcake project that allows the user to
# draw different shapes using turtle by calling specific shapes,
# including square, circle, line, and write

#Turtle graphics functions
import turtle

#The square function draws a square.
#x and y coordinates are the bottom left of the circle
def square(x, y, width, color):
    turtle.penup()
    #start turtle at coordinate
    turtle.goto(x, y)
    #set the fill color
    turtle.fillcolor(color)
    #start pen
    turtle.pendown()
    turtle.begin_fill()
    #draw the four sides
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    #end turtle fill
    turtle.end_fill()

#the circle function raws a circle
#x and y coordinates are the circle's center
def circle(x, y, radius, color):
    turtle.penup()
    #start turtle at coordinate
    turtle.goto(x, y - radius)
    #set the fill color
    turtle.fillcolor(color)
    #start pen
    turtle.pendown()
    turtle.begin_fill()
    #draw the circle
    turtle.circle(radius)
    turtle.end_fill()

#the line function draws a line from (StartX, startY)
# to (endX, endY).
def line(startX, startY, endX, endY, color):
    turtle.penup()
    #start turtle at coordinate
    turtle.goto(startX,startY)
    #set the fill color
    turtle.fillcolor(color)
    #start pen
    turtle.pendown()
    #draw the line
    turtle.pencolor(color)
    turtle.goto(endX, endY)

#the write function writes a word starting from x and y at the bottom left
def write(x, y, text):
    turtle.penup()
    turtle.goto(x, y)
    #write the text
    turtle.write(text, font=('Arial', 16, 'normal'))
    
