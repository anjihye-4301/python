import turtle
import random

swidth, sheight, psize, exitcount = 300, 300, 3, 0
r, g, b, angel, dist, curx, cury = [0]*7

turtle.title('거북이가 맘대로 다니기')
turtle.shape('turtle')
turtle.pensize(psize)
turtle.setup(width=swidth+30, height=sheight+30)
turtle.screensize(swidth, sheight)

while True:
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r,g,b))

    angle = random.randrange(0, 360)
    dist = random.randrange(1, 100)
    turtle.left(angle)
    turtle.forward(dist)
    curx = turtle.xcor()
    cury = turtle.ycor()

    if(-swidth/2<=curx and curx<=swidth/2)and(-sheight/2<=cury and cury<=sheight/2):
        pass
    else:
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()

        exitcount += 1
        if exitcount >=5:
            break

turtle.done()