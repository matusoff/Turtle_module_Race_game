#Turtle race game

from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)


is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors =["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles =[]

i = -100
for turtle_index in range(0,6):

    turtle = Turtle(shape = "turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=i)
    all_turtles.append(turtle)
    i+=40

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

screen.exitonclick()
