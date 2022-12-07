from turtle import Screen
from snake import Snake
from game_env import Game_Env
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(650, 650)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
snake.create_snake()
game_env = Game_Env()
game_env.draw_walls()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

game_on = True
while game_on:
    time.sleep(snake.move_speed)
    screen.update()
    snake.move_snake()

    #Detect walls
    if snake.cor_x() >= 280 or snake.cor_x() <= -280:
        game_on = False
        scoreboard.game_over()
    elif snake.cor_y() >= 280 or snake.cor_y() <= -280:
        game_on = False
        scoreboard.game_over()

    # Detect tail
    # for segment in snake.segments[1:]:
    #     if snake.head.distance(segment) < 5:
    #         game_on = False
    #         scoreboard.game_over()

    #Detect food
    if snake.head.distance(food) < 15:
        food.show_food()
        snake.extend_snake()
        scoreboard.update_score()
        snake.speed()


screen.exitonclick()