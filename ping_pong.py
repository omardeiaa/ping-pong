"""hello, welcome back. today you will learn how to make ping pong game in python
using turtle
--------------------------------
the project: ping pong
used package: turtle
developer name: Omar
"""



import turtle


screen = turtle.Screen()
screen.title("ping pong by omar")
screen.bgcolor("black")
screen.setup(height=700, width=1000)
screen.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(450, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(-450, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

def paddle_a_up():
    y = paddle_a_up.ycor()
    y += 10
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 10
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 10
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 10
    paddle_b.sety(y)

screen.listen()
screen.onkeypress(paddle_a_up, "Up")
screen.onkeypress(paddle_a_down, "Down")
screen.onkeypress(paddle_b_up, "w")
screen.onkeypress(paddle_b_down, "s")

while True:
    screen.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
