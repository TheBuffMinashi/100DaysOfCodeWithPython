import turtle as t
import random

t.colormode(255)
t.bgcolor("black")
Tom = t.Turtle()
Tom.pensize(3)
Tom.speed("fastest")


def color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


# Make Tom draw a square
# for _ in range(4):
#     Tom.forward(100)
#     Tom.right(90)


# Make Tom draw a dashed line
# for _ in range(15):
#     Tom.forward(10)
#     Tom.penup()
#     Tom.forward(10)
#     Tom.pendown()


# Make Tom draw a triangle, square, pentagon, hexagon,...
# shapes = list(range(3, 11))
# for i in shapes:
#     angle = 360 / i
#     color = color_generator()
#     for _ in range(i):
#         Tom.color(color)
#         Tom.forward(100)
#         Tom.right(angle)


# Make timmy go for a random walk
# turns = [0, 90, 180, 270]
# for _ in range(100):
#     Tom.color(color_generator())
#     Tom.forward(30)
#     turn = random.choice(turns)
#     Tom.setheading(turn)

# Make Tom draw a Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        Tom.color(color_generator())
        Tom.circle(100)
        Tom.setheading(Tom.heading() + size_of_gap)
        Tom.hideturtle()


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
