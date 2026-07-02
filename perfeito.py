import math
maior_nota = -math.inf # consideramos, no início, que maior nota é absurdamente baixa, inferior a qualquer nota possível.
                # ao lermos as notas vamos progressivamente melhorando esta hipótese inicial
nota = float(input()) # lemos a primeira nota da sequência
while nota != -1:     # verificamos se o valor lido é o último; se for, paramos o processo de leitura
    if nota > maior_nota:   # a condição é verdadeira caso a nota lida seja superior à estimativa anterior
        maior_nota = nota   # neste caso, substituimos a estimativa anterior pela nova
    nota = float(input())   # lemos a próxima nota da sequência (da 2º em diante)
print(maior_nota)           # apresentamos a maior nota