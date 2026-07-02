from classes import *
from funcoes import *

# 4. PROGRAMA PRINCIPAL (PONTO DE ENTRADA)

def main():
    acervo = []
    usuarios = []
    admin_unico = Administrador()

    while True:
        print("\n--- ACESSO AO SISTEMA ---")
        print("Digite: [1] Criar Conta | [0] Sair do Programa")
        login_ou_nome = input("Ou digite seu NOME de Usuário para Logar: ")

        if login_ou_nome == '0' or login_ou_nome.lower() == 'sair':
            print()
            print("Saindo do sistema...")
            break
        elif login_ou_nome == '1':
            cadastrar_usuario(usuarios)
        else:
            senha = input("Digite a senha: ")

            # Autenticação baseada em encapsulamento seguro através do método validar_senha()
            if login_ou_nome == admin_unico.get_nome() and admin_unico.validar_senha(senha):
                menu_admin(acervo, usuarios, admin_unico)
            else:
                usuario_logado = next((u for u in usuarios if u.get_nome() == login_ou_nome), None)
                if usuario_logado and usuario_logado.validar_senha(senha):
                    menu_usuario(acervo, usuario_logado)
                else:
                    print()
                    print("Usuário não encontrado ou senha incorreta!")


if __name__ == "__main__":
    main()