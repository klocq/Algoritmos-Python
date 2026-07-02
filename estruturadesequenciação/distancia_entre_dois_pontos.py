import math

#input dos dados separados por um unico espaço
x1, y1 = [float(w) for w in input().split()]
x2, y2 = [float(w) for w in input().split()]

#realizar o calculo da distância
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f'{distancia:.4f}')
