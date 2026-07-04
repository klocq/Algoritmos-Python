nome_completo = input().split()
primeiro_nome = nome_completo.pop(0)
ultimo_nome = nome_completo.pop()

nome_abreviado = ""
for nome in nome_completo:
    if len(nome) > 3:
        nome_abreviado += nome[0] + ". "
    else:
        nome_abreviado += nome + " "

print(primeiro_nome + " " + nome_abreviado + ultimo_nome)
