import turtle as t
import time
from snake_body import Snake
from food import Food
from scoreboard import ScoreBoard


screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game!')
screen.tracer(0)


# snake = [t.Turtle('square') for turt in range(3)]
# x = 0
snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')


gameon = True

while gameon:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.respawn()
        snake.extend()
        scoreboard.update_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        gameon = False
        scoreboard.game_over()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 8:
            gameon = False
            scoreboard.game_over()


t.exitonclick()
