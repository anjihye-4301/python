import turtle
import random


# 함수 선언 - 2줄 띄우기.
def screen_left_click(x, y):
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)


def screen_right_click(x, y):
    turtle.penup()
    turtle.goto(x, y)


def screen_mid_click(x, y):
    global r, g, b
    t_size = random.randrange(1, 10)
    turtle.shapesize(t_size)
    r = random.random()
    g = random.random()
    b = random.random()


pSize = 10
r, g, b = 0.0, 0.0, 0.0

turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

# onscreenclick - 클릭 이벤트 처리
turtle.onscreenclick(screen_left_click, 1)
turtle.onscreenclick(screen_mid_click, 2)
turtle.onscreenclick(screen_right_click, 3)

turtle.done()
