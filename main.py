import random
from turtle import Turtle,Screen
screen=Screen()
color=["black","red","green","purple","blue","orange"]
screen.setup(600,500)
user_bet=screen.textinput("Bet on any color",prompt="choose the any color:").lower()
x=-280
y=-200
turtle_list=[]

for i in range(0,6):
    names=Turtle()
    names.shape("turtle")
    names.color(color[i])
    names.penup()
    names.goto(x,y)
    names.pendown()
    names.shapesize(2)
    turtle_list.append(names)
    y+=75

if user_bet:
    race=True

while race:
    for t in turtle_list:
        if t.xcor()>=270:
            race = False
            winner=t.pencolor()
            winner_x=t.xcor()
            if user_bet==winner:
                print(f"you won the bet winner is : {winner}")
                print(winner_x)
            else:
                print(f"you lost the race, winner is : {winner}")
                print(winner_x)

        ran=random.randint(0,10)
        ran1 = random.randint(0, 15)
        t.penup()
        t.speed(ran1)
        t.forward(ran)




screen.exitonclick()