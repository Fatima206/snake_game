from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game using Turtle in Python")
screen.tracer(0)  # Turn off turtle animation

# by default, each turtle object is 20 by 20 pixels. Position coordinates relative to the centre.

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()  # Refresh screen
    time.sleep(0.1)
    # Delay refresh so that we can control how often it happens.
    # Also, to prevent the snake running off-screen
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        snake.extend()
        food.goto_random_location()
        scoreboard.score += 1
        scoreboard.update_score()

    # Detect collision with wall.
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
