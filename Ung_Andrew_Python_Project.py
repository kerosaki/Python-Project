# Author: Andrew Ung
# Created: Jan 5, 2022
# Description: A randomized cartoon-style waterfall scene using turtle graphics.

import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Randomized Waterfall Scene")

# Draw the cliff
cliff = turtle.Turtle()
cliff.penup()
cliff.goto(-200, -150)
cliff.pendown()
cliff.color("dimgray")
cliff.begin_fill()
cliff.goto(-200, 100)
cliff.goto(200, 100)
cliff.goto(200, -150)
cliff.goto(-200, -150)
cliff.end_fill()
cliff.hideturtle()

# Draw the waterfall
waterfall = turtle.Turtle()
waterfall.penup()
waterfall.goto(-100, 100)
waterfall.pendown()
waterfall.color("deepskyblue")
waterfall.begin_fill()
waterfall.goto(-100, -100)
waterfall.goto(100, -100)
waterfall.goto(100, 100)
waterfall.goto(-100, 100)
waterfall.end_fill()
waterfall.hideturtle()

# Add randomized water lines
water_lines = turtle.Turtle()
water_lines.color("white")
water_lines.width(2)
water_lines.speed(0)

for _ in range(random.randint(5, 12)):
    x = random.randint(-90, 90)
    water_lines.penup()
    water_lines.goto(x, 100)
    water_lines.pendown()
    water_lines.goto(x, -100)

water_lines.hideturtle()

# Draw randomized rocks at the bottom
rock = turtle.Turtle()
rock.color("gray")
rock.speed(0)

for _ in range(random.randint(3, 6)):
    x = random.randint(-180, 180)
    y = random.randint(-160, -130)
    size = random.randint(20, 40)
    rock.penup()
    rock.goto(x, y)
    rock.pendown()
    rock.begin_fill()
    rock.circle(size)
    rock.end_fill()

rock.hideturtle()

# Draw 5 trees using a loop
tree = turtle.Turtle()
tree.color("forestgreen")
tree.speed(0)

for _ in range(5):
    x = random.randint(-180, 180)
    y = random.randint(-150, 100)
    
    # Draw the tree top (triangle)
    tree.penup()
    tree.goto(x, y)
    tree.pendown()
    tree.begin_fill()
    for _ in range(3):  # triangle
        tree.forward(30)
        tree.left(120)
    tree.end_fill()
    
    # Draw the trunk
    tree.penup()
    tree.goto(x + 10, y - 10)
    tree.pendown()
    tree.color("saddlebrown")
    tree.begin_fill()
    for _ in range(2):
        tree.forward(10)
        tree.right(90)
        tree.forward(15)
        tree.right(90)
    tree.end_fill()
    tree.color("forestgreen")  # reset color for next tree

tree.hideturtle()

# Keep the window open
turtle.done()
