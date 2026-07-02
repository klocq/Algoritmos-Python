while True:
    jogadas = int(input())
    
    if jogadas == 0:
        break
    
    rodadas = (input()).split()
    
    mary = rodadas.count("0")
    john = rodadas.count("1")
    
    print(f"Mary won {mary} times and John won {john} times")