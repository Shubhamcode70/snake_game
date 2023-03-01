from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score_data import Score

screen = Screen()
screen.title("Snake Game")
screen.setup(600, 600)
screen.tracer(0)

# big_snake = []
# x = 20
# for part in range(0, 3):
#     mon = Turtle("square")
#     mon.penup()
#     x = x - 20
#     mon.goto(x, 0)
#     big_snake.append(mon)
snake = Snake()
food = Food()
score = Score()


game_on = True
while game_on:
    time.sleep(0.10)
    screen.update()
    # for part in big_snake:
    #     part.forward(20)
    # for part_no in range(len(big_snake) - 1, 0, -1):
    #     old_x = big_snake[part_no - 1].xcor()
    #     old_y = big_snake[part_no - 1].ycor()
    #     big_snake[part_no].goto(old_x, old_y)
    #     big_snake[0].forward(20)

    snake.move()

    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    if snake.head.distance(food) < 15:
        # screen.resetscreen()
        score.score_update()
        # food.reset()
        # food.hideturtle()
        food.refresh()
        snake.extends()

    if snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() > 280:
        game_on = False
        score.game_over()

    #Detect collision with head / Check collision with any segment in the snake body
    for parts in snake.big_snake[1:]:
        # if parts == snake.head:
        #     pass
        if snake.head.distance(parts) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()