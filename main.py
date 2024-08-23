from turtle import Screen,Turtle
from scoreboard import Scoreboard
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("my snake game")
""""starting_position=[(0,0),(-20,0),(-40,0)]
segments=[]
for position in starting_position:
  new_segment=Turtle('square')
  new_segment.color('white')
  new_segment.penup()
  new_segment.goto(position)
  segments.append(new_segment)"""
snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on=True
while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()
  if snake.head.distance(food)<15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()
  """"for seg_num in range(len(segments)-1,0,-1):
    new_x=segments[seg_num-1].xcor()
    new_y=segments[seg_num-1].ycor()
    segments[seg_num].goto(new_x,new_y)
  segments[0].forward(20)"""
  if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor() <- 280: 
    game_is_on=False
    scoreboard.game_over()
  for segment in snake.segments:
    if segment==snake.head:
      pass
    elif snake.head.distance(segment)<10:
      game_is_on=False
      scoreboard.game_over()





screen.exitonclick()