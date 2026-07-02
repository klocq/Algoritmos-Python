cedulas = int(input())
caixa_ele = {}

for _ in range(cedulas):
    valor = float(input())
    qnt_cedula = int(input())
    caixa_ele[valor] = qnt_cedula

saque = float(input())

while saque != 0:
    mais_notas = -1
    for dinheiro in caixa_ele.keys():
        notas = saque // dinheiro
        if mais_notas < notas:
            mais_notas = notas
            cedula = dinheiro
    saque -= cedula * mais_notas
