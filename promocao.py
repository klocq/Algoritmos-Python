valor = float(input())

desconto = valor * 0.2

if valor >= 500:
    desconto += valor * 0.1

if valor >= 1000:
    desconto += (valor - 1000) * 0.15

valor_final = valor - desconto

print(round(valor_final,2))