import turtle
from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter your color: ")
colors: list[str] = ['yellow', 'red', 'orange', 'pink', 'purple', 'blue']
y_position = [100, 50, 0, -50, -100, -150]
turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-250, y=y_position[turtle_index])
    turtles.append(new_turtle)


if user_bet:
    race_on = True

while race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'Congrats, {winning_color} won the race.')

            else:
                print(f'Sorry, {winning_color} won the race.')


        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


screen.exitonclick()