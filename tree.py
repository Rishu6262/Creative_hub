import turtle
import random
import math
import colorsys

# =========================
# Screen Setup
# =========================
screen = turtle.Screen()
screen.setup(width=500, height=1000)
screen.bgcolor("black")
screen.title("Fractal Tree")
screen.tracer(5)
screen.colormode(255)

# =========================
# Turtle for Tree
# =========================
t = turtle.Turtle()
t.hideturtle()
t.speed(1.5)

# =========================
# Turtle for Text
# =========================
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)


# =========================
# Fractal Tree Function
# =========================
def draw_tree(length, angle, depth):
    # Base condition:
    # Jab depth 0 ho jayegi, recursion stop ho jayega.
    if depth == 0:
        return

    # Branch ko depth ke according thick banayenge
    t.pensize(max(1, depth // 2))

    # Green shades generate karna
    hue = 0.25 + (10 - depth) * 0.02
    r, g, b = colorsys.hsv_to_rgb(hue, 0.8, 1)

    t.color(
        int(r * 255),
        int(g * 255),
        int(b * 255)
    )

    # Main branch draw karo
    t.forward(length)

    # Left branch
    t.left(angle)

    draw_tree(
        length * 0.7,
        angle,
        depth - 1
    )

    # Wapas center branch par
    t.right(angle * 2)

    # Right branch
    draw_tree(
        length * 0.7,
        angle,
        depth - 1
    )

    # Original direction mein wapas
    t.left(angle)

    # Parent branch par wapas aao
    t.backward(length)


# =========================
# Refresh Function
# =========================
def refresh():
    # Purani drawing clear karo
    t.clear()
    pen.clear()

    # Turtle ko starting position par lao
    t.penup()
    t.goto(0, -400)

    # Tree ko upward direction mein set karo
    t.setheading(90)

    t.pendown()

    # New tree draw karo
    draw_tree(100, 25, 10)

    # =========================
    # Refresh Text
    # =========================
    pen.penup()
    pen.goto(-200, 400)
    pen.pendown()

    pen.color("white")
    pen.write(
        "Click to refresh",
        font=("Arial", 16, "normal")
    )


# =========================
# Mouse Click Event
# =========================
def click_refresh(x, y):
    refresh()


# =========================
# First Tree
# =========================
refresh()

# Screen par click karne par tree refresh hoga
screen.onclick(click_refresh)

# Window ko open rakho
turtle.done()
print("Fractal Tree program has ended.")