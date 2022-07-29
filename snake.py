from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.speed("slowest")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        #  add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        # for seg_num in range(start= len(segments), stop= 1, step= -1): This throws error because start, stop, step is
        # keyword argument which is not taken by range()
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # len(segment)-1 = start point , 0 = is stop point , -1 = step means
            # how much step size is taken to reach stop point.

            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Above for loop is very important because it moves the 3 segment to the position of 2 segment and 2 to the
        # position of 1 segment
        self.head.forward(MOVE_DISTANCE)  # And  finally the first segment(0th position of list segment) is
        # moved forward
        # self.segments[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left_turn(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right_turn(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create()
        self.head = self.segments[0]

