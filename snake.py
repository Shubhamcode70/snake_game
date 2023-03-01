from turtle import Turtle
MOVE_DIST = 20
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
class Snake:
    def __init__(self):
        self.big_snake = []
        self.snake_gen()
        self.head = self.big_snake[0]

    def snake_gen(self):
        for position in STARTING_POSITION:
            self.add_parts(position)
        # x = 20
        # for part in range(0, self.extend):
        #     mon = Turtle("square")
        #     mon.penup()
        #     mon.speed("fastest")
        #     x = x - 20
        #     mon.goto(x, 0)
        #     self.big_snake.append(mon)

    def add_parts(self, position):
        mon = Turtle("square")
        #mon.color()
        mon.penup()
        mon.speed("fastest")
        mon.goto(position)
        self.big_snake.append(mon)

    def extends(self):
        self.add_parts(self.big_snake[-1].position())

    def move(self):
        for part_no in range(len(self.big_snake) - 1, 0, -1):
            old_x = self.big_snake[part_no - 1].xcor()
            old_y = self.big_snake[part_no - 1].ycor()
            self.big_snake[part_no].goto(old_x, old_y)
        self.big_snake[0].forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 360:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(360)