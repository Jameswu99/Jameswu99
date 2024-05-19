import turtle
import turtle as t
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'lawn green', 'seashell', 'light blue',
                'goldenrod', 'hot pink', 'thistle', 'gold', 'peru', 'forest green', 'maroon', 'navy', 'peach puff',
                'misty rose', 'deep pink', 'lemon chiffon', 'aquamarine'])


def draw_circle(size):
    t.pencolor(next(colors))
    t.circle(size)
    draw_circle(size + 1)


t.hideturtle()
t.bgcolor('black')
t.speed(200)
t.pensize(4)
draw_circle(1)
t.pencolor('red')
t.circle(30)
