from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Welcome to My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
Score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left_turn, "Left")
screen.onkey(snake.right_turn, "Right")

game_is_on = True
while game_is_on:

    snake.move()
    screen.update()
    time.sleep(0.1)

    # Detect Collision with Food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        Score.increase_score()

    # Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        Score.reset_score()
        snake.reset_snake()

    # Detect Collision with Tail, if head collides with any segment in the tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            Score.reset_score()
            snake.reset_snake()


screen.exitonclick()
