n_dias, saldo_inicio = [int(w) for w in input().split()]
menor_saldo = saldo_inicio

for _ in range(n_dias):
    movimentacao_dia = int(input())
    saldo_inicio += movimentacao_dia
    
    if saldo_inicio < menor_saldo:
        menor_saldo = saldo_inicio
    
print(menor_saldo)
