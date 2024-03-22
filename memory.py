"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *
import string
import random

from freegames import path

car = path('car.gif')

tiles = list()
for i in range(32):
    tiles.append(string.ascii_letters[i])
    tiles.append(string.ascii_letters[i])
    
state = {'mark': None}
hide = [True] * 64
score = {"Taps": 0}
writer = Turtle(visible=False)
counter = 31
writer2 = Turtle(visible=False)

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    counter = 0
    writer.undo()
    writer.write(score["Taps"])
    
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        score["Taps"] += 1
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        counter += 1
        if counter == 32:
            writer2.write("Fin del juego")


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    


    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x+26, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align = "center")

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 500, 370, 0)
addshape(car)
hideturtle()    
tracer(False)
writer.goto(160, 210)
writer.color('black')
writer.write(score['Taps'])
writer2.goto(50, 210)
writer2.color('black')
writer2.write("")
onscreenclick(tap)
draw()
done()
