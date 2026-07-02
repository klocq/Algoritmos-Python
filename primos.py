import math 
numero_n = int(input())


p = numero_n / math.log(numero_n)
m = 1.25506 * p

print(f'{p:.1f} {m:.1f}')