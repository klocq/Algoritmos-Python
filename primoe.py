def primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    
    return True 


x = int(input())
y = int(input())

contador = 0

for num in range(x, y + 1):
    if primo(num):
        contador += 1

print(contador)