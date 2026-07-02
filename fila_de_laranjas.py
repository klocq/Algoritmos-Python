import turtle

tata = turtle.Turtle()
tata.speed(0)  

raio = [15, 20, 30, 40, 50, 60]

for i in range(len(raio)):
    r = raio[i]

    tata.color("orange")
    tata.begin_fill()
    tata.circle(r)
    tata.end_fill()

    tata.penup()

    # mover até o próximo círculo (tangência)
    if i < len(raio) - 1:
        proximo = raio[i + 1]
        tata.forward(r + proximo)

    tata.pendown()



turtle.done()

