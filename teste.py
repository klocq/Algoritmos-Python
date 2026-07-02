n = int(input())

atual, proximo = 1, 1

for _ in range(n - 1):
    atual, proximo = proximo, atual + proximo

print(atual)