from turtle import Turtle

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
Up=90
Down=270
Left=180
Right=0
class Snake:
  def __init__(self):
    self.segments=[]
    self.create_snake()
    self.head=self.segments[0]
  def create_snake(self):
    for position in STARTING_POSITIONS:
      self.add_segment(position)

  def add_segment(self,position):
    new_segment=Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    self.segments.append(new_segment)

  def extend(self):
    self.add_segment(self.segments[-1].position())

  def move(self):
    for seg_num in range(len(self.segments)-1,0,-1):
      new_x=self.segments[seg_num-1].xcor()
      new_y=self.segments[seg_num-1].ycor()
      self.segments[seg_num].goto(new_x,new_y)
    self.head.forward(MOVE_DISTANCE)

  def up(self):
    if self.head.heading()!=Down:
     self.head.setheading(Up)
  def down(self):
    if self.head.heading()!=Up:
     self.head.setheading(Down)

  def left(self):
    if self.head.heading()!=Right:
     self.head.setheading(Left)
  def right(self):
    if self.head.heading()!=Left:
     self.head.setheading(Right)








Snake.move()