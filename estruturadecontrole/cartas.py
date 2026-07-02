cartas = [int (x) for x in input().split()]

cartas_teste = cartas.copy()

cartas_teste.sort()

if cartas == cartas_teste:
    print("C")
elif cartas == cartas_teste[::-1]:
    print("D")
else:
    print("N")
