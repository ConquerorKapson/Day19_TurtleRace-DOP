import turtle as t
import random

screen = t.Screen()
screen.setup(width=900, height=400)
turtles = []
color = ["red", "blue", "pink", "green", "purple", "yellow"]
random.shuffle(color)
for i in range(6):
    new_turtle = t.Turtle("turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x=-435, y=-140+i*50)
    turtles.append(new_turtle)

bet_turtle = t.textinput("kachue pe satta laga do", "Kaunse rang ke kachue pe satta lagaana chaahte ho?")
# print(bet_turtle)
# print(turtles)
# bet_turtle = t.textinput("kachue pe satta laga do", "Kaunse rang ke kachue pe satta lagaana chaahte ho?")

# is_race_on = False
# while not is_race_on:
#     # print("Wrong Choice")
#     if bet_turtle in color:
is_race_on = True

while is_race_on:
    for kachua in turtles:
        if kachua.xcor() >= 433:
            is_race_on = False
            if kachua.pencolor() == bet_turtle:
                print(f"Congratulations, aapka {bet_turtle} kachua jeet gaya!!!")
            else:
                print(f"Hame khed hai ki {kachua.pencolor()} kachua jeet gaya, aapka {bet_turtle} kachua haar gaya :(")
        kachua.fd(random.randint(0, 8))

screen.exitonclick()
