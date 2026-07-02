i = 1
while True:
    partidas = int(input())
    aldo = 0
    beto = 0
    
    if partidas == 0:
        break
    for rodada in range(partidas):
        a, b = [int(w) for w in input().split()]
        aldo += a
        beto += b
        
    print(f'Teste {i}')
    if aldo > beto:
        print("Aldo\n")
    else:
        print("Beto\n")
    i += 1