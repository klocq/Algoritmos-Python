febonacci = int(input())
anterior = 1
atual = 1
for _ in range(1, febonacci - 1):
    novo_termo = anterior + atual
    anterior = atual
    atual = novo_termo

print(novo_termo)
