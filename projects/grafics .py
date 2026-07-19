import turtle

# Set up screen
turtle.bgcolor("green")
turtle.title("Creative Turtle Drawing")
turtle.speed(8)  # Speed from 1 (slow) to 10 (fast), 0 is instant

# Customize turtle appearance
turtle.pensize(3)
turtle.pencolor("yellow")
turtle.shape("turtle")  # Makes the cursor look like a turtle

# Start filling shapes
turtle.fillcolor("orange")
turtle.begin_fill()

a = 0
b = 0

# Drawing loop
for _ in range(50):
    turtle.forward(200)
    a += 3
    turtle.right(100)
    b += 3

# End filling
turtle.end_fill()

# Hide turtle and finish
turtle.hideturtle()
turtle.done()
