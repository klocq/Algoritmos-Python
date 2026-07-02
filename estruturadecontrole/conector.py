conector1 = [int (x) for x in input().split()]
conector2 = [int (x) for x in input().split()]

eh_compativel = "Y"

for i in range(5):
    if conector1[i] == conector2[i]:
        eh_compativel == "N"
        break

print(eh_compativel)	
