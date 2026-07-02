numero1 = int(input())
numero2 = int(input())
menor = numero1

i = 1
while numero1 <= numero2:
    print(numero1, end=" ")
    i += 1
    numero1 = menor * i
    