massa_radiotiva = float(input())
segundos = 0

while massa_radiotiva >= 0.5:
    segundos += 50
    massa_radiotiva /= 2

print(segundos)