import turtle

tt = turtle.Turtle()
num_lados = 12
tam_lado = 50

# Função para desenhar polígono regular
def desenhar_poligono(num_lados, tam_lado):
    angulo = 360 / num_lados
    
    for _ in range(num_lados):
        tt.forward(tam_lado)
        tt.left(angulo)

desenhar_poligono(num_lados, tam_lado)

turtle.done()
