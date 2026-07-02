import turtle
import math

# Criar a tartaruga
construtor = turtle.Turtle()
construtor.speed(3)

# Tamanho base
x = 100

# Desenhar o corpo da casa (retângulo)
for i in range(2):
    construtor.forward(2*x)
    construtor.left(90)
    construtor.forward(x)
    construtor.left(90)

# Porta
construtor.forward(x/3)
construtor.left(90)
construtor.forward(2*x/3)
construtor.right(90)
construtor.forward(x/3)
construtor.right(90)
construtor.forward(2*x/3)

# Janela
construtor.up()
construtor.left(90)
construtor.forward(x/3)
construtor.left(90)
construtor.forward(x/3)
construtor.down()

for i in range(4):
    construtor.forward(x/3)
    construtor.right(90)

construtor.up()
construtor.right(90)
construtor.forward(x/3)
construtor.down()

for i in range(4):
    construtor.forward(x/3)
    construtor.left(90)



construtor.up()
construtor.left(90)
construtor.forward(2*x/3)
construtor.right(90)
construtor.forward(x/3 + x/3)
construtor.down()

beiral = x/6 
construtor.right(45)
construtor.forward(beiral)
construtor.up()
construtor.backward(beiral)
construtor.down()
construtor.left(180)
construtor.forward(x * math.sqrt(2))

construtor.left(90)
construtor.forward(x * math.sqrt(2))
construtor.forward(beiral)

# Finalizar
turtle.done()