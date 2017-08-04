from __future__ import division

import turtle
import time

WIDTH, HEIGHT = 800, 600
FONT = ("Arial", 25, "normal")
DRAWING_SLEEPING_INTERVAL = 0.5
WRITING_SLEEPING_INTERVAL = 2.5
MAX_DEPTH = 5
SIZE_WHEN_CONSTANT_DEPTH = 300
DEPTH_WHEN_CONSTANT_SIZE = 4
RANGE_OF_SIZES = range(0, 5000, 5)
SIDES_OF_AN_EQUILATERAL_TRIANGLE = 3
EQUILATERAL_TRIANGLE_INTERNAL_ANGLE = 120
DRAWING_START_X = - 200
DRAWING_START_Y = 150

def snowflake(n, size=300):

    for _ in range(SIDES_OF_AN_EQUILATERAL_TRIANGLE):
        snowflake_edge(n, size)
        turtle.right(EQUILATERAL_TRIANGLE_INTERNAL_ANGLE)

    turtle.update()

def snowflake_edge(n, size=300):
    if n == 0:
        turtle.forward(size)
        return

    for movement in (lambda: turtle.left(EQUILATERAL_TRIANGLE_INTERNAL_ANGLE // 2),
                   lambda: turtle.right(EQUILATERAL_TRIANGLE_INTERNAL_ANGLE),
                   lambda: turtle.left(EQUILATERAL_TRIANGLE_INTERNAL_ANGLE // 2)):
        snowflake_edge(n - 1, size / SIDES_OF_AN_EQUILATERAL_TRIANGLE)
        movement()

    snowflake_edge(n - 1, size / SIDES_OF_AN_EQUILATERAL_TRIANGLE)

def costum_reset():
    turtle.reset()
    turtle.penup()
    turtle.setx( DRAWING_START_X )
    turtle.sety( DRAWING_START_Y )
    turtle.pendown()

def write_as_title(title, font=FONT):
    turtle.setx(- (WIDTH // 2.5) )
    turtle.sety(HEIGHT // 3)
    turtle.write(title, font=font)

if __name__ == "__main__":
    turtle.setup(width=WIDTH, height=HEIGHT)
    turtle.hideturtle()
    turtle.tracer(0, 0)

    write_as_title(\
        "Constant size, recursion depth increasing.", font=FONT)
    time.sleep(WRITING_SLEEPING_INTERVAL)

    for deepness in range(MAX_DEPTH):
        costum_reset()
        snowflake(deepness, SIZE_WHEN_CONSTANT_DEPTH)
        time.sleep(DRAWING_SLEEPING_INTERVAL)

    costum_reset()
    write_as_title(\
        "Constant recursion depth, size increasing.", font=FONT)
    time.sleep(WRITING_SLEEPING_INTERVAL)
    for size in RANGE_OF_SIZES:
        costum_reset()
        snowflake(DEPTH_WHEN_CONSTANT_SIZE, size)
