msg_codigo = input()

decodigo = ""
i = 0

while i < len(msg_codigo):
    if msg_codigo[i] == " ":
        decodigo += " "
        i += 1
    else: 
        decodigo += msg_codigo[i+1]
        i += 2
print(decodigo)
