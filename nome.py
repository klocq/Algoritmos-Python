partes = input().split()

abreviado = ''

for i in range(len(partes)):
    if i == 0 or i == len(partes) - 1:
        palavra = partes[i]
    elif len(partes[i]) > 3:
        palavra = partes[i][0] + '.'
    else:
        palavra = partes[i]

    if i > 0:
        abreviado += ' '
    abreviado += palavra

print(abreviado)