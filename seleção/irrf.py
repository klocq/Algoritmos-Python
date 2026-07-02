valor = float(input())
dependente = int(input())

if valor > 2400:
    inss = 2400 * 0.11
elif valor > 1200:
    inss = valor * 0.11
elif valor > 720:
    inss = valor * 0.09
else:
    inss = valor * 0.0765

desconto_dep = dependente * 137.99

if valor <= 1372.81:
    aliquota = 0
    deducao = 0
elif valor <= 2743.25:
    aliquota = 0.15
    deducao = 205.92
else:
    aliquota = 0.275
    deducao = 548.82

irrf = (valor - desconto_dep - inss) * aliquota - deducao
print(f'{irrf:.2f}')
