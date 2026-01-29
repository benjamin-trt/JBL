import turtle

fenetre = turtle.Screen()
fenetre.title("autoroute")
fenetre.bgcolor("deepskyblue2")

stylo = turtle.Turtle()
stylo.speed(90000000000000000000000000000000)
stylo.hideturtle()

def dessiner_rectangle(couleur, l, H):
    stylo.color(couleur)
    stylo.begin_fill()
    for i in range(2):
        stylo.forward(l)
        stylo.left(90)
        stylo.forward(H)
        stylo.left(90)
    stylo.end_fill()

stylo.penup()
stylo.goto(-200, -340)
stylo.pendown()

dessiner_rectangle("gray", 400, 1000)

stylo.color("white")
stylo.width(6)

for x in [-100, 0, 100]:
    stylo.penup()
    stylo.goto(x, -400)
    stylo.pendown()
    stylo.setheading(90)
    stylo.forward(1000)

fenetre.mainloop()