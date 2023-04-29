import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    rob = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    rob.shape('turtle')
    # Set your turtle's speed using .speed(2)
    rob.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    rob.color('green')
    rob.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?

    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    for i in range(4):
        rob.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
        rob.right(90)
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    rob.goto(50,50)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    rob.begin_fill()
    rob.circle(10,steps=30)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    rob.end_fill()
    # Draw 3 more shapes with different fill colors!
    rob.begin_fill()
    for x in range(3):
        rob.forward(50)
        rob.right(120)
    rob.end_fill()

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
