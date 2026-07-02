quantas_praias = int(input())
maior_distancia = float("-inf")
praia_mais_dist = ""
praia_entre_15_20 = 0
dist_media = 0

for _ in range(quantas_praias):
    praia, distancia = input().split(';')
    distancia = int(distancia)
    
    if distancia > maior_distancia:
        maior_distancia = distancia
        praia_mais_dist = praia
    
    if 15 >= distancia and distancia <= 20:
        praia_entre_15_20 += 1
    
