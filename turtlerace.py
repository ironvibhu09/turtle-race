from turtle import Turtle
from random import randint

laura = Turtle()
rik = Turtle()
lauren = Turtle()
carrieanne = Turtle()
line = Turtle()

line.hideturtle()
line.penup()
line.goto(159,120)
line.pendown()
line.left(90)
line.forward(-130)
line.penup()


laura.color('red')
laura.shape('turtle')

laura.penup()
laura.goto(-160, 100)
laura.pendown()

rik.color('orange')
rik.shape('turtle')

rik.penup()
rik.goto(-160, 70)
rik.pendown()

lauren.color('blue')
lauren.shape('turtle')

lauren.penup()
lauren.goto(-160, 40)
lauren.pendown()

carrieanne.color('green')
carrieanne.shape('turtle')

carrieanne.penup()
carrieanne.goto(-160, 10)
carrieanne.pendown()

for movement in range(100):
 laura.forward(randint(1,5))
 rik.forward(randint(1,5))
 lauren.forward(randint(1,5))
 carrieanne.forward(randint(1,5))


input("Press Enter to close")