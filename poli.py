frase = input()

frase = frase.replace(" ", "").lower()

print(frase == frase[::-1])