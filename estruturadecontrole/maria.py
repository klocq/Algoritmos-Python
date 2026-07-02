num_testes = int(input())
marias = 0

for _ in range(num_testes):
    nome = input().split(" ")
    for nomes in nome:
        if nomes == "Maria":
            marias += 1

print(marias)
