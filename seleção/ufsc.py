nota = float(input())

nota_inteira = nota // 1
nota_resto = (nota % 1)

if nota_resto < 0.25:
    soma = 0
elif nota_resto < 0.75:
    soma = 0.5
else:
    soma = 1

nota_final = nota_inteira + soma

print(nota_final)
