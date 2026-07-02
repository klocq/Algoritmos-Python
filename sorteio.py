camisas = int(input())

for _ in range(camisas):
    pessoas, segredo = [int(x) for x in input().split()]
    num_chutados = [int (x) for x in input().split()]
    
    if segredo in num_chutados:
        acerto = num_chutados.index(segredo) + 1
    else:
        mais_perto = 100
        for numero in range(pessoas):
            perto = abs(segredo - num_chutados[numero])
            if perto < mais_perto:
                mais_perto = perto
                acerto = numero + 1
    print(acerto)
            