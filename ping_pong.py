"""hello, welcome back. today you will learn how to make ping pong game in python
using turtle
--------------------------------
the project: ping pong
used package: turtle
developer name: Omar
"""
'Omar kabil'

# Importing turtle and playsound and math Modules
import turtle
import os
import time

# Create the Scores
score_1 = 0
score_2 = 0

# Create the screen
screen = turtle.Screen()
screen.title("ping pong by omar")
screen.bgcolor("black")
screen.setup(height=700, width=1000)
screen.tracer(0)

# Paddle B
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(450, 0)

# Paddle A
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(-450, 0)

# The Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.9
ball.dy = 0.9

# Player 1 and Player 2 Scores
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 300)
pen.hideturtle()
pen.write("                 0                             0                ", align="center", font=("Pixel", 30, "normal"))

# Player 1 and Player 2 Areas Border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.shape("square")
border.shapesize(stretch_wid=90, stretch_len=0.2)
border.penup()
border.goto(0, 0)

# Player 1 or Player 2 wins !
menu = turtle.Turtle()
menu.speed(0)
menu.color("green")
menu.penup()
menu.goto(0, 0)
menu.hideturtle()

# game functions
def paddle_a_up():
    y = paddle_a.ycor()
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

def continue_game():
    menu.clear()
    pen.write("            0                           0           ", align="center", font=("Pixel", 30, "normal"))
    ball.goto(0, 0)

screen.listen()
screen.onkeypress(paddle_a_up, "Up")
screen.onkeypress(paddle_a_down, "Down")
screen.onkeypress(paddle_b_up, "w")
screen.onkeypress(paddle_b_down, "s")

while True:
    screen.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 350:
        ball.sety(350)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    elif ball.ycor() < -350:
        ball.sety(-350)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 550:
        score_2 += 1
        pen.clear()
        pen.write("            {}                           {}           ".format(score_2, score_1), align="center", font=("Pixel", 30, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -550:
        score_1 += 1
        pen.clear()
        pen.write("            {}                           {}           ".format(score_2, score_1), align="center", font=("Pixel", 30, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if (ball.xcor() > 450 and ball.xcor() < 460) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(450)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    elif (ball.xcor() < -450 and ball.xcor() > -460) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(-450)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if paddle_a.ycor() > 290:
        paddle_a.sety(290)

    elif paddle_a.ycor() < -290:
        paddle_a.sety(-290)

    elif paddle_b.ycor() > 290:
        paddle_b.sety(290)

    elif paddle_b.ycor() < -290:
        paddle_b.sety(-290)

    if score_1 == 10:
        menu.write("Player 2   WINS !!!!", align="center", font=("Courier", 30, "normal"))
        time.sleep(1.5)
        screen.bye()

    if score_2 == 10:
        menu.write("Player 1   WINS!!!!", align="center", font=("Courier", 30, "normal"))
        time.sleep(1.5)
        screen.bye()


