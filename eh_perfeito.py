entrada = int(input())


for _ in range(entrada):
    eh_perfeito = int(input())
    calculo_perfeito = 0
    for numero in range(eh_perfeito - 1):
        if eh_perfeito % (numero + 1)  == 0:
            calculo_perfeito += numero + 1
        
    if calculo_perfeito == eh_perfeito:
        print(f'{eh_perfeito} eh perfeito')
    else:
        print(f'{eh_perfeito} nao eh perfeito')
            
            