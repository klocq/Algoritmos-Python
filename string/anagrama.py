p1 = input()
p2 = input()

palavra_teste = ""

if p1 != p2 and len(p1) == len(p2):
    for letra in p1:
        if letra in p2:
            local_pala = p2.index(letra)
            palavra_teste += letra
            p2 = p2[:local_pala] + p2[local_pala + 1:]
        else:
            break

print(p1 == palavra_teste)
