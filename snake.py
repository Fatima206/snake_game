from turtle import Turtle

STARTING_X_COR = 0
STARTING_Y_COR = 0
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def create_snake(self):
        global STARTING_X_COR
        for n in range(3):
            self.add_segment((STARTING_X_COR, STARTING_Y_COR))
            STARTING_X_COR -= 20

    def extend(self):
        """Add a new segment to the snake each time it collides with the food"""
        # send new segment to the last segment's position
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # move to the 2nd to last segment's position
            new_pos = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(new_pos)

        self.head.forward(MOVE_DISTANCE)

    # To prevent snake moving backwards
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
