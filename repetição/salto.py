num_saltadores = int(input())
melhor_salto = float("-inf")
melhor_saltador = ""

for _ in range(num_saltadores):
    
    salto1, salto2, salto3, saltador = input().split(" ")
    salto1 = float(salto1)
    salto2 = float(salto2)
    salto3 = float(salto3)
    saltador_melhor_salto = max(salto1, salto2, salto3)
    
    if saltador_melhor_salto > melhor_salto:
        melhor_salto = saltador_melhor_salto
        melhor_saltador = saltador

print(melhor_saltador)
