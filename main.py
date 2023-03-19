import turtle


window = turtle.Screen()
tortoise = turtle.Turtle()


tortoise.speed(0)
window.bgcolor("white")
tortoise.pencolor("green")
tortoise.fillcolor("lime")


tortoise.begin_fill()
for i in range(3):
    tortoise.forward(100)
    tortoise.left(120)
tortoise.end_fill()

tortoise.fillcolor("lightblue")
tortoise.begin_fill()
for i in range(4):
    tortoise.forward(100)
    tortoise.right(90)
tortoise.end_fill()

tortoise.fillcolor("pink")
tortoise.begin_fill()
tortoise.circle(50)
tortoise.end_fill()

window.exitonclick()
