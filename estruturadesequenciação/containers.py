
largura_cont, comprimento_cont, altura_cont = [int(w) for w in input().split()]
largura_navio, comprimento_navio, altura_navio = [int(w) for w in input().split()]

#calculo para quantidade de containers
qnt_conteiners = largura_navio // largura_cont * (comprimento_navio // comprimento_cont) * (altura_navio // altura_cont)

print(qnt_conteiners)
