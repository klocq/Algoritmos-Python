def eh_primo(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


N, M = map(int, input().split())

# P1 → maior primo ≤ N
p1 = N
while p1 >= 2:
    if eh_primo(p1):
        break
    p1 -= 1

# P2 → menor primo ≥ M
p2 = M
while True:
    if eh_primo(p2):
        break
    p2 += 1

print(p1 * p2)