from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
i = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    #ditect colision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.clear()
        score.strack()
        
    #detect colisionwith wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        game_is_on = False
        
        score.game_over()
        
    #detect collision with tail
    for segment in snake.segments[1:]:
        
        # if snake.head.distance(segments) < 10:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
    #if head colliad with any segment, game over

        
    
   
        














screen.exitonclick()