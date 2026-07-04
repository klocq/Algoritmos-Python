while True:
    teutograma = input().lower()
    
    if teutograma == "*":
        break
    
    primeira_letra = teutograma[0]
    eh_teutograma = True
    
    for i in range(1, len(teutograma)):
        # se encontrou início de uma nova palavra
        if teutograma[i-1] == " ":
            if teutograma[i] != primeira_letra:
                eh_teutograma = False
                break
    
    if eh_teutograma:
        print("Y")
    else:
        print("N")
