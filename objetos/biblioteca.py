# --- SISTEMA DE BIBLIOTECA - VERSÃO ÚNICA ---

class ItemBiblioteca:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
        self._disponivel = True

    # Getters e Setters
    def get_titulo(self): return self._titulo
    def set_titulo(self, t): self._titulo = t
    def get_autor(self): return self._autor
    def set_autor(self, a): self._autor = a
    def get_disponivel(self): return self._disponivel

    def emprestar(self):
        if self._disponivel:
            self._disponivel = False
            return True
        return False

    def devolver(self):
        self._disponivel = True

    def exibir_info(self):
        status = "Disponível" if self._disponivel else "Emprestado"
        return f"Título: {self.get_titulo()} | Autor: {self.get_autor()} | Status: {status}"

    # Método base que será sobrescrito (Polimorfismo)
    def calcular_multa(self, dias):
        return 0.0

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, isbn):
        super().__init__(titulo, autor)
        self.__isbn = isbn
    def get_isbn(self): return self.__isbn
    def set_isbn(self, i): self.__isbn = i
    def exibir_info(self):
        return f"[LIVRO] {super().exibir_info()} | ISBN: {self.get_isbn()}"
    def calcular_multa(self, dias):
        return dias * 2.0

class Revista(ItemBiblioteca):
    def __init__(self, titulo, autor, edicao):
        super().__init__(titulo, autor)
        self.__edicao = edicao
    def get_edicao(self): return self.__edicao
    def set_edicao(self, e): self.__edicao = e
    def exibir_info(self):
        return f"[REVISTA] {super().exibir_info()} | Edição: {self.get_edicao()}"
    def calcular_multa(self, dias):
        return dias * 1.5

class DVD(ItemBiblioteca):
    def __init__(self, titulo, autor, duracao):
        super().__init__(titulo, autor)
        self.__duracao = duracao
    def get_duracao(self): return self.__duracao
    def set_duracao(self, d): self.__duracao = d
    def exibir_info(self):
        return f"[DVD] {super().exibir_info()} | Duração: {self.get_duracao()} min"
    def calcular_multa(self, dias):
        return dias * 3.5

# --- Funções de Interface ---
def menu_criar():
    print("\n1. Livro | 2. Revista | 3. DVD")
    tipo = input("Escolha: ")
    t = input("Título: ")
    a = input("Autor: ")
    if tipo == '1': return Livro(t, a, input("ISBN: "))
    elif tipo == '2': return Revista(t, a, input("Edição: "))
    elif tipo == '3': return DVD(t, a, input("Duração: "))
    return None

def main():
    acervo = []
    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Inserir | 2. Listar | 3. Alterar | 4. Excluir | 5. Emprestar | 6. Devolver/Multa | 0. Sair")
        op = input("Opção: ")
        
        if op == '1':
            item = menu_criar()
            if item: acervo.append(item)
            
        elif op == '2':
            for i, item in enumerate(acervo): print(f"{i} - {item.exibir_info()}")
            
        elif op == '3':
            for i, item in enumerate(acervo): print(f"{i} - {item.get_titulo()}")
            idx = int(input("Índice: "))
            item = acervo[idx]
            print("1. Título | 2. Autor | 3. Específico")
            sub = input("Escolha: ")
            if sub == '1': item.set_titulo(input("Novo Título: "))
            elif sub == '2': item.set_autor(input("Novo Autor: "))
            elif sub == '3':
                if isinstance(item, Livro): item.set_isbn(input("Novo ISBN: "))
                elif isinstance(item, Revista): item.set_edicao(input("Nova Edição: "))
                elif isinstance(item, DVD): item.set_duracao(input("Nova Duração: "))
                
        elif op == '4':
            for i, item in enumerate(acervo): print(f"{i} - {item.get_titulo()}")
            acervo.pop(int(input("Índice para excluir: ")))
            
        elif op == '5':
            for i, item in enumerate(acervo):
                if item.get_disponivel(): print(f"{i} - {item.get_titulo()}")
            idx = int(input("Índice para emprestar: "))
            if acervo[idx].emprestar(): print("Emprestado!")
            else: print("Já está emprestado.")
            
        elif op == '6':
            for i, item in enumerate(acervo):
                if not item.get_disponivel(): print(f"{i} - {item.get_titulo()}")
            idx = int(input("Índice para devolver: "))
            item = acervo[idx]
            dias = int(input("Dias de atraso: "))
            print(f"Multa a pagar: R$ {item.calcular_multa(dias):.2f}")
            item.devolver()
            
        elif op == '0': break

if __name__ == "__main__":
    main()
