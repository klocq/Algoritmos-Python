comprimento_estrada, distancia_pedagios = [int(w) for w in input().split()]
custo_quilometro, preco_pedagio = [int(w) for w in input().split()]

qnt_pedagio = comprimento_estrada // distancia_pedagios 

custo_viagem = qnt_pedagio * preco_pedagio + comprimento_estrada * custo_quilometro

print(custo_viagem)