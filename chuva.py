meses = [[int (x) for x in input().split()] for i in range(12)]

for mes in meses:
    chuva_mensal = sum(mes)/len(mes)
    print(f'{chuva_mensal:.2f}',end=" ")