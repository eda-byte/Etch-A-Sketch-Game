from turtle import Turtle, Screen
tim=Turtle()
screen=Screen()


def move_forwards():
    tim.forward(10)
def move_backwards():
    #
    tim.backward(10)
def to_left():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
def to_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def clean():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=to_left)
screen.onkey(key="d", fun=to_right)
screen.onkey(key="c", fun=clean)

screen.exitonclick()