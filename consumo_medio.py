distancia_percorrida = int(input())
combustivel_gasto = float(input())

#calculo do consumo

consumo_medio = distancia_percorrida / combustivel_gasto

consumo_medio = round(consumo_medio, 3)

print(consumo_medio, "km/l")