frase = input().lower()
letras = {}

for letra in frase:
    letras[letra] = letras.get(letra, 0) + 1

mais_vez = max(letras, key=letras.get)
print(mais_vez)