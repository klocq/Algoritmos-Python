assunto = input()

assunto_comeco = assunto.index("(")
asunto_aberto = assunto.count("(")
asunto_fechado = assunto.count(")", assunto_comeco)


num_assunto = int(asunto_aberto) - int(asunto_fechado)
print(f'Partiu RU! ' if num_assunto == 0 else f'Ainda temos {abs(num_assunto)} assunto(s) pendente(s)!')