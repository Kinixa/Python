import turtle
import time
import random

# window
win = turtle.Screen()
win.title("Sssnake")
win.setup(width=600, height=600)
win.bgcolor("black")
win.tracer(0)

# snake options
snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = "Stop"

# game setting
score_point = 0
delay_time = 0.2

# points setting
point = turtle.Turtle()
point.shape("circle")
point.color("yellow")
point.penup()
point.speed(0)
point.goto(0, 100)

# score setting
score = turtle.Turtle()
score.goto(0, 270)
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.write("Score: ", align="center", font=("Arial", 18, "normal"))


# moving
def left():
    if snake.direction != "right":
        snake.direction = "left"


def right():
    if snake.direction != "left":
        snake.direction = "right"


def up():
    if snake.direction != "down":
        snake.direction = "up"


def down():
    if snake.direction != "up":
        snake.direction = "down"


def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


win.listen()
win.onkeypress(left, "a")
win.onkeypress(right, "d")
win.onkeypress(up, "w")
win.onkeypress(down, "s")


body = []

# gameplay

while True:
    win.update()
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "Stop"
        snake.shape("square")
        snake.color("white")
        for segment in body:
            segment.goto(1000, 1000)
        body.clear()
        score_point = 0
        delay_time = 0.1
        score.clear()
        score.write("Score: {}" .format(score_point),  align="center", font=("Arial", 18, "normal"))
    if snake.distance(point) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        point.goto(x, y)

        # adding new segments to snake's body
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("white")
        new_body.penup()
        body.append(new_body)
        delay_time -= 0.001
        score_point += 10
        score.clear()
        score.write("Score: {}" .format(score_point),  align="center", font=("Arial", 18, "normal"))

    for index in range(len(body) - 1, 0, -1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x, y)
    if len(body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)
    move()
    for segment in body:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"
            snake.shape("square")
            snake.color("white")
            for segment in body:
                segment.goto(1000, 1000)
            body.clear()

            score_point = 0
            delay = 0.1
            score.clear()
            score.write("Score: {}" .format(score_point),  align="center", font=("Arial", 18, "normal"))
    time.sleep(delay_time)

win.mainloop()













