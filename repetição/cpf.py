cpf = input()
cpf_limpo = ""

for caracter in cpf:
    if caracter.isalnum():
        cpf_limpo += caracter

# Verificações iniciais
if len(cpf_limpo) != 11 or cpf_limpo == cpf_limpo[0] * 11:
    print(False)
else:
    # Primeiro dígito
    soma = sum(int(cpf_limpo[i]) * (10 - i) for i in range(9))
    dv1 = 11 - (soma % 11)
    dv1 = 0 if dv1 >= 10 else dv1

    # Segundo dígito
    soma = sum(int(cpf_limpo[i]) * (11 - i) for i in range(10))
    dv2 = 11 - (soma % 11)
    dv2 = 0 if dv2 >= 10 else dv2

    # Verifica se bate com os dígitos finais
    print(cpf_limpo[-2:] == f"{dv1}{dv2}")
