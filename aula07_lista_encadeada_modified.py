class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Lista:
    def __init__(self):
        self.cabeca = None

    def insere_no_inicio(self, dado):
        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(dado)

        if self.cabeca is None:                     # lista vazia
            # define o novo nodo como cabeça da lista
            self.cabeca = novo_nodo
        else:                                      # lista não vazia
            # novo nodo aponta para a cabeça da lista.
            novo_nodo.proximo = self.cabeca
            self.cabeca = novo_nodo

    def insere_no_final(self, dado):
        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(dado)

        if self.cabeca is None:                     # lista vazia
            # define o novo nodo como cabeça da lista
            self.cabeca = novo_nodo
        else:                                       # lista não vazia
            nodo_atual = self.cabeca
            while nodo_atual.proximo is not None:
                nodo_atual = nodo_atual.proximo
            nodo_atual.proximo = novo_nodo

    def remove_do_inicio(self):
        if self.cabeca is None:                     # lista vazia
            raise 'Fila Vazia'
        else:                                       # lista não vazia
            # altera a cabeça da lista
            self.cabeca = self.cabeca.proximo

    def remove_do_final(self):
        if self.cabeca is None:                     # lista vazia
            raise 'Fila Vazia'
        elif self.cabeca.proximo is None:           # apenas 1 item
            self.cabeca = None
        else:                                       # lista não vazia
            nodo_atual = self.cabeca
            nodo_anterior = None

            # percorre os nós até o penultimo item
            while nodo_atual.proximo is not None:
                nodo_anterior = nodo_atual          # atualiza o nó anterior
                nodo_atual = nodo_atual.proximo     # atualiza o nó atual

            nodo_anterior.proximo = None            # remove ultimo item

    def buscar(self, valor):
        nodo_atual = self.cabeca
        while nodo_atual is not None:           # percorre os nós da lista
            if nodo_atual.dado == valor:        # verifica se encontrou o item
                return True
            nodo_atual = nodo_atual.proximo     # atualiza o nó atual
        return False                        # terminou a lista e não encontrou

    def imprimir(self):
        nodo_atual = self.cabeca
        lista = ""
        while nodo_atual is not None:           # percorre os nós da lista
            lista += str(nodo_atual.dado) + ", "
            # atualiza o nó atual
            nodo_atual = nodo_atual.proximo
        return lista[0:len(lista)-2]

    """
    EXERCICIO 1:
    Implemente a função 'tamanho' que retorna a quantidade de itens da lista.
    Caso a lista esteja vazia, deve retornar zero.
    """

    def tamanho(self):
        if self.cabeca is None:
            return 0
        passo_atual = self.cabeca
        contador = 0
        while passo_atual is not None:
            contador += 1
            passo_atual = passo_atual.proximo
        return contador

    """
    EXERCICIO 2:
    implemente a função 'menor' que retorna o menor item contido na lista.
    Caso a lista esteja vazia deve retornar None.
    """

    def menor(self):
        if self.cabeca is None:
            return None
        passo_atual = self.cabeca
        menor = passo_atual
        while passo_atual is not None:
            if passo_atual.dado < menor.dado:
                menor = passo_atual
            passo_atual = passo_atual.proximo
        return menor.dado

    """
    EXERCÍCIO 3:
    Implemente a função 'remover_valor' que recebe um valor e remove a primeira
    ocorrência desse valor da lista.
    Caso a lista esteja vazia, nada deve ser feito.
    """

    def remover_valor(self, valor):
        if self.cabeca is None:
            ...
        if self.cabeca is not None:
            passo_anterior = None
            passo_atual = self.cabeca
            while passo_atual is not None:
                if passo_atual.dado == valor:
                    if passo_anterior is None:
                        self.cabeca = passo_atual.proximo
                        return
                    else:
                        passo_anterior.proximo = passo_atual.proximo
                        return
                passo_anterior = passo_atual
                passo_atual = passo_atual.proximo

    """
    EXERCÍCIO 4:
    Implemente a função 'lista_reversa' que retorna uma lista (padrão do
    python) com os itens da lista encadeada na ordem inversa
    Caso a lista esteja vazia, deve retornar [].
    """

    def lista_reversa(self):
        lista_reversa = []
        if self.cabeca is None:
            return lista_reversa
        nodo_atual = self.cabeca
        while nodo_atual is not None:
            lista_reversa.append(nodo_atual.dado)
            nodo_atual = nodo_atual.proximo
        return lista_reversa[::-1]


# Exemplo de utilização da classe Lista
lista = Lista()
lista.insere_no_inicio(10)
lista.insere_no_inicio(20)
lista.insere_no_inicio(30)
lista.insere_no_inicio(40)
print(lista.imprimir())         # 40, 30, 20, 10

lista.insere_no_final(50)
lista.insere_no_final(60)
lista.insere_no_final(70)
lista.insere_no_final(80)
print(lista.imprimir())         # 40, 30, 20, 10, 50, 60, 70, 80

print(lista.buscar(10))         # True
print(lista.buscar(100))        # False

lista.remove_do_inicio()
lista.remove_do_inicio()
print(lista.imprimir())         # 20, 10, 50, 60, 70, 80

lista.remove_do_final()
lista.remove_do_final()
print(lista.imprimir())         # 20, 10, 50, 60


# Testes para os métodos a serem implementados
print("\nEXECUÇÃO DOS TESTES:\n")


def test_01_tamanho():
    try:
        lista3 = Lista()
        assert lista3.tamanho() == 0, 'Tamanho deve ser zero'
        print("ACERTO test_01_tamanho")
    except AssertionError as erro:
        print("ERRO test_01_tamanho: ", erro)


def test_02_tamanho():
    try:
        lista = Lista()
        lista.insere_no_final(10)
        assert lista.tamanho() == 1, 'Tamanho deve ser 1'
        print("ACERTO test_02_tamanho")
    except AssertionError as erro:
        print("ERRO test_02_tamanho: ", erro)


def test_03_tamanho():
    try:
        lista = Lista()
        lista.insere_no_final(10)
        lista.insere_no_final(20)
        lista.insere_no_final(30)
        assert lista.tamanho() == 3, 'Tamanho deve ser 3'
        print("ACERTO test_03_tamanho")
    except AssertionError as erro:
        print("ERRO test_03_tamanho: ", erro)


def test_04_menor():
    try:
        lista = Lista()
        assert lista.menor() is None, 'Menor item deve ser None'
        print("ACERTO test_04_menor")
    except AssertionError as erro:
        print("ERRO test_04_menor: ", erro)


def test_05_menor():
    try:
        lista = Lista()
        lista.insere_no_final(10)
        assert lista.menor() == 10, 'Menor item deve ser 10'
        print("ACERTO test_05_menor")
    except AssertionError as erro:
        print("ERRO test_05_menor: ", erro)


def test_06_menor():
    try:
        lista = Lista()
        lista.insere_no_final(10)
        lista.insere_no_final(20)
        lista.insere_no_final(5)
        lista.insere_no_final(30)
        lista.insere_no_final(5)
        assert lista.menor() == 5, 'Menor item deve ser 5'
        print("ACERTO test_06_menor")
    except AssertionError as erro:
        print("ERRO test_06_menor: ", erro)


def test_07_menor():
    try:
        lista = Lista()
        lista.insere_no_final(30)
        lista.insere_no_final(20)
        lista.insere_no_final(30)
        lista.insere_no_final(40)
        lista.insere_no_final(7)
        assert lista.menor() == 7, 'Menor item deve ser 7'
        print("ACERTO test_07_menor")
    except AssertionError as erro:
        print("ERRO test_07_menor: ", erro)


def test_08_remover_valor():
    try:
        lista = Lista()
        lista.remover_valor(10)
        assert lista.imprimir() == '', 'Lista deve continuar vazia'
        assert lista.cabeca is None, 'Cabeça da lista deve ser None'
        print("ACERTO test_08_remover_valor")
    except AssertionError as erro:
        print("ERRO test_08_remover_valor: ", erro)


def test_09_remover_valor():
    try:
        lista = Lista()
        lista.insere_no_final(20)
        lista.remover_valor(20)
        assert lista.imprimir() == '', 'Lista deve ser vazia'
        assert lista.cabeca is None, 'Cabeça da lista deve ser None'
        print("ACERTO test_09_remover_valor")
    except AssertionError as erro:
        print("ERRO test_09_remover_valor: ", erro)


def test_10_remover_valor():
    try:
        lista = Lista()
        lista.insere_no_final(20)
        lista.insere_no_final(30)
        lista.insere_no_final(40)
        lista.insere_no_final(20)
        lista.insere_no_final(50)
        lista.remover_valor(20)
        assert lista.imprimir() == '30, 40, 20, 50', 'lista deve ser: 30, 40, 20, 50'
        assert lista.cabeca.dado == 30, 'Cabeça da lista deve ser 30'
        print("ACERTO test_10_remover_valor")
    except AssertionError as erro:
        print("ERRO test_10_remover_valor: ", erro)


def test_11_remover_valor():
    try:
        lista = Lista()
        lista.insere_no_final(20)
        lista.insere_no_final(30)
        lista.insere_no_final(40)
        lista.insere_no_final(20)
        lista.insere_no_final(50)
        lista.remover_valor(40)
        assert lista.imprimir() == '20, 30, 20, 50', 'lista deve ser: 20, 30, 20, 50'
        assert lista.cabeca.dado == 20, 'Cabeça da lista deve ser 20'
        print("ACERTO test_11_remover_valor")
    except AssertionError as erro:
        print("ERRO test_11_remover_valor: ", erro)


def test_12_remover_valor():
    try:
        lista = Lista()
        lista.insere_no_final(20)
        lista.insere_no_final(30)
        lista.insere_no_final(40)
        lista.insere_no_final(60)
        lista.insere_no_final(50)
        lista.remover_valor(50)
        assert lista.imprimir() == '20, 30, 40, 60', 'lista deve ser: 20, 30, 40, 60'
        assert lista.cabeca.dado == 20, 'Cabeça da lista deve ser 20'
        print("ACERTO test_12_remover_valor")
    except AssertionError as erro:
        print("ERRO test_12_remover_valor: ", erro)


def test_13_remover_valor():
    try:
        lista = Lista()
        lista.insere_no_final(20)
        lista.insere_no_final(30)
        lista.insere_no_final(40)
        lista.insere_no_final(20)
        lista.insere_no_final(50)
        lista.remover_valor(100)
        assert lista.imprimir() == '20, 30, 40, 20, 50', 'lista deve ser: 20, 30, 40, 20, 50'
        assert lista.cabeca.dado == 20, 'Cabeça da lista deve ser 20'
        print("ACERTO test_13_remover_valor")
    except AssertionError as erro:
        print("ERRO test_13_remover_valor: ", erro)


def test_14_lista_reversa():
    try:
        lista = Lista()
        lista.insere_no_final(20)
        lista.insere_no_final(30)
        lista.insere_no_final(40)
        lista.insere_no_final(50)
        lista.insere_no_final(60)
        assert lista.imprimir() == '20, 30, 40, 50, 60', 'lista deve ser: 20, 30, 40, 50, 60'
        assert lista.lista_reversa() == [
            60, 50, 40, 30, 20], 'lista reversa deve ser: [60, 50, 40, 30, 20]'
        print("ACERTO test_14_lista_reversa")
    except AssertionError as erro:
        print("ERRO test_14_lista_reversa: ", erro)


def test_15_lista_reversa():
    try:
        lista = Lista()
        lista.insere_no_final(20)
        assert lista.imprimir() == '20', 'lista deve ser: 20'
        assert lista.lista_reversa() == [20], 'lista reversa deve ser: [20]'
        print("ACERTO test_15_lista_reversa")
    except AssertionError as erro:
        print("ERRO test_15_lista_reversa: ", erro)


def test_16_lista_reversa():
    try:
        lista = Lista()
        assert lista.imprimir() == '', 'lista deve ser vazia'
        assert lista.lista_reversa() == [], 'lista reversa deve ser: []'
        print("ACERTO test_16_lista_reversa")
    except AssertionError as erro:
        print("ERRO test_16_lista_reversa: ", erro)


test_01_tamanho()
test_02_tamanho()
test_03_tamanho()
test_04_menor()
test_05_menor()
test_06_menor()
test_07_menor()
test_08_remover_valor()
test_09_remover_valor()
test_10_remover_valor()
test_11_remover_valor()
test_12_remover_valor()
test_13_remover_valor()
test_14_lista_reversa()
test_15_lista_reversa()
test_16_lista_reversa()
