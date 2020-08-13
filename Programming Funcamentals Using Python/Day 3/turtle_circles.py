import turtle           # allows us to use the turtles library
wn = turtle.Screen()    # creates a graphics window
wn.setup(500, 500)       # set window dimension

alex = turtle.Turtle()  # create a turtle named alex
alex.shape("turtle")    # alex looks like a turtle


alex.color("green")
alex.right(60)
alex.left(60)
alex.circle(50)
for counter in range(1, 4):
    alex.circle(20*counter)

alex.color("blue")
alex.right(100)
alex.circle(50)
for counter in range(1, 4):
    alex.circle(20*counter)

alex.color("red")
alex.right(160)
alex.circle(50)
for counter in range(1, 4):
    alex.circle(20*counter)
