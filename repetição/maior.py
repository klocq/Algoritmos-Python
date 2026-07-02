repeticao = int(input())
maior_num = float('-inf')

for posicao in range(repeticao):
    numero_entrada = int(input())
    
    if numero_entrada > maior_num:
        maior_num = numero_entrada
        posicao_maior = posicao + 1
        
print(maior_num, posicao_maior)
