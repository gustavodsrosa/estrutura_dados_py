import hashlib
import unittest

'''
EXPLICACAO

    Uma fila é um tipo abstrato de dados que suporta 2 operações
    basicas (e mais duas que vamos falar mais pra frente, mas
    sao bem mais simples).

    As duas operações basicas são "insere" e "retira"

    A idéia é que novos elementos são inseridos "no fim"
    da fila, e, se retiramos alguém, é o elemento do início da fila.

    Basicamente é uma fila de supermercado. Quem entra, entra
    "no fim", quando vai sair alguém, sai o que está "na frente".

    Ou seja: quem entrou primeiro sai primeiro. Em inglês,
    diriamos First In First Out, ou FIFO.
'''

'''
EXEMPLO

   Comecemos com uma fila vazia: []
   insere(2)
   fila: [2]
   insere(5)
   fila: [2, 5]
   insere(1)
   fila: [2, 5, 1]
   retira()
   sai o 2
   fila: [5, 1]
'''

'''
EXERCÍCIO

Inicie com uma fila vazia.
considere as seguintes operações:
    insere(3)
    insere(4)
    insere(1)
    insere(2)

Qual o estado da fila?
Responda, em forma de lista, na variavel fila1
'''

fila1 = [3, 4, 1, 2]


'''
EXERCÍCIO

Inicie com uma fila vazia.
Execute:
    insere(3)
    insere(4)
    remove()
    insere(1)
    insere(2)
    remove()

Qual o estado da fila?
Responda, em forma de lista, na variavel fila2
'''

fila2 = [1, 2]

'''
EXERCÍCIO

Inicie com uma fila vazia.
Execute:
    insere(3)
    insere(4)
    remove()
    insere(1)
    remove()
    insere(2)
    remove()
    insere(7)

Qual o estado da fila?
Responda, em forma de lista, na variavel fila3
'''

fila3 = [2, 7]

'''
   Para implementar a idéia de filas em python, usamos uma lista.
   Para criar uma lista vazia, fazemos lista = []
   Para a operação "retira", fazemos lista.pop(0)
   Para adicionar um elemento, fazemos lista.append(elemento)

   Veja o exemplo a seguir

    fila = []
    fila.append(1)      # fila = [1]
    fila.append(2)      # fila = [1, 2]
    fila.append(3)      # fila = [1, 2, 3]
    fila.pop(0)         # fila = [2, 3]
    fila.append(4)      # fila = [2, 3, 4]
    fila.pop(0)         # fila = [3, 4]


EXERCICIO

    Definindo uma fila como acima, com listas,
    faca uma funcao enfileirar(fila, elemento)
    que adiciona o elemento ao final da fila
'''


def enfileirar(fila, elemento):
    fila.append(elemento)
    return fila


'''
EXERCICIO

    Faca a funcao 'desenfileirar(fila)' que tira o elemento do inicio
    da fila e o retorna.

    Ou seja:
    fila = [10, 2, 3]
    desenfileirar(fila)    # retorna 10, e a fila fica com os elementos [2, 3]
'''


def desenfileirar(fila):
    valor_inicial = fila[0]
    fila.pop(0)
    return valor_inicial


'''
EXPLICACAO

    Para verificar quantos elementos tem na fila, é só fazer len(fila).
    Veja o exemplo

    fila = []
    fila.append(2)          # fila = [2]
    fila.append(3)          # fila = [2, 3]
    len(fila)               # 2
    fila.append(4)          # fila = [2, 3, 4]
    len(fila)               # 3
    fila.pop(0)             # fila = [3, 4]
    len(fila)               # 2


EXERCICIO

    Implemente a função 'tamanho(fila)', que recebe uma fila e retorna a
    quantidade de elementos contidos nessa fila.
'''


def tamanho(fila):
    return len(fila)


'''
EXERCICIO

    Usando o tamanho, podemos definir uma funcao 'fila_vazia'
    que diz se a fila está vazia ou não.
    Ela retorna True se a fila estiver vazia, False caso contrário
'''


def fila_vazia(fila):
    if len(fila) == 0:
        resp = True
    else:
        resp = False
    return resp


'''
EXPLICACAO
    Para ver qual é o primeiro elemento da fila, sem retirar
    ninguém, é só usar o indice 0. Veja o exemplo:

    fila = [10, 11, 100, 1]
    # retornar o primeiro elemento, sem retirá-lo da fila
    primeiro = fila[0]
    print(primeiro)     # 10
    # fila = [10, 11, 100, 1]

    # retornar o primeiro elemento e retirá-lo da fila
    primeiro = fila.pop(0)
    print(primeiro)     # 10
    # fila = [11, 100, 1]


EXERCICIO

    Implemente a função 'primeiro(fila)', que retorna o primeiro elemento
    da fila sem retirá-lo da fila.
'''


def primeiro(fila):
    return fila[0]


'''
EXERCICIO

    faça uma funcao vira_1(fila) que recebe uma fila, retira o primeiro
    elemento do começo da fila e coloca ele de volta, no fim da fila

    Ex:
    fila = [1, 2, 3, 4, 5]
    se fizermos vira_1(fila), a fila passa a ser [2, 3, 4, 5, 1]

    Utilize as funçoes enfileirar e desenfileirar implementadas anteriormente
'''


def vira_1(fila):
    valor_inicial = fila[0]
    fila.pop(0)
    fila.append(valor_inicial)
    return fila


'''
EXERCICIO

    faça uma funcao vira_5(fila) que recebe uma fila, retira o primeiro
    elemento do começo da fila e coloca ele de volta, no fim da fila.
    Depois faz isso de novo, pegando o novo primeiro elemento da fila
    e colocando no final...
    Fazendo 5 vezes no total.

    Ex:
    fila = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    depois de vira_5(fila), a fila será [6, 7, 8, 9, 1, 2, 3, 4, 5]

    Utilize as funçoes enfileirar e desenfileirar implementadas anteriormente
'''


def vira_5(fila):
    for i in range(5):
        valor_inicial = fila[0]
        fila.pop(0)
        fila.append(valor_inicial)
    return fila


'''
EXERCICIO
    Faça uma funçao vira_n(fila, n), parecida com a vira_5.
    A idéia agora é que você pode especificar quantas
    vezes a operacao "pega do começo e poe no fim" acontece.

    Exemplo:
    fila = [1, 2, 3, 4, 5, 6]
    depois de vira_n(fila, 3), a fila será [4, 5, 6, 1, 2, 3]
    se fizermos vira_n(fila, 3) novamente, a fila será [1, 2, 3, 4, 5, 6]
    se fizermos vira_n(fila, 1), a fila agora será [2, 3, 4, 5, 6, 1]

    Utilize as funçoes enfileirar e desenfileirar implementadas anteriormente
'''


def vira_n(fila, n):
    for i in range(n):
        valor_inicial = fila[0]
        fila.pop(0)
        fila.append(valor_inicial)
    return fila


'''
EXERCICIO

    Faça uma funçao vira_4_mata_1(fila),
    que faz o mesmo que vira_5 para os primeiros 4 elementos,
    mas depois tira o primeiro elemento da fila e não coloca ele de volta

    Ex:
    fila = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Tira o 1 e coloca no fim, depois o 2, depois o 3, depois o 4.
    # Tira o 5 e nao coloca na fila.
    depois de vira_4_mata_1(fila), a fila será [6, 7, 8, 9, 1, 2, 3, 4]
    se fizemos vira_4_mata_1(fila) de novo, a fila será [2, 3, 4, 6, 7, 8, 9]

    Utilize as funçoes enfileirar e desenfileirar implementadas anteriormente
'''


def vira_4_mata_1(fila):
    for i in range(4):
        valor_inicial = fila[0]
        fila.pop(0)
        fila.append(valor_inicial)
    fila.pop(0)
    return fila


'''
EXERCÍCIO

    Faça uma funcao fila_inicial(n) que recebe um numero n
    e retorna uma lista [1, 2, 3, ..., n] (ou seja, uma lista
    dos numeros de 1 até n.
'''


def fila_inicial(n):
    lista = []
    for i in range(1, n+1):
        lista.append(i)
    return lista


# ----------------------------------------------------------------------
'''
O trecho de código abaixo irá testar a implementação das funções.
Ele não deve ser alterado.
'''


class TestStringMethods(unittest.TestCase):

    def test_01_fila1(self):
        self.verifica_fila(
            fila1, 'a6e09ce0ee14436cb70020b2fdbf640e79f88bfbc1d3b81276657a2d')

    def test_02_fila2(self):
        self.verifica_fila(
            fila2, '009f4fe1b80c470dec51da24864145a53a702b5263d09165e58475e1')

    def test_03_fila3(self):
        self.verifica_fila(
            fila3, '716dba572ee747af70f2fe863b1206c87244726185bb42a30fb5025c')

    def test_04_enfileirar(self):
        fila = [1, 2]
        enfileirar(fila, 5)
        self.assertEqual(fila, [1, 2, 5])
        enfileirar(fila, 10)
        self.assertEqual(fila, [1, 2, 5, 10])
        fila = [1, 2]
        enfileirar(fila, 10)
        self.assertEqual(fila, [1, 2, 10])

    def test_05_desenfileirar_fila(self):
        fila = [10, 4, 5]
        primeiro = desenfileirar(fila)
        self.assertEqual(primeiro, 10)
        self.assertEqual(fila, [4, 5])
        primeiro = desenfileirar(fila)
        self.assertEqual(primeiro, 4)
        self.assertEqual(fila, [5])
        primeiro = desenfileirar(fila)
        self.assertEqual(primeiro, 5)
        self.assertEqual(fila, [])
        fila = [11, 12, 13]
        primeiro = desenfileirar(fila)
        self.assertEqual(primeiro, 11)
        self.assertEqual(fila, [12, 13])

    def test_06_tamanho_fila(self):
        fila = [10, 4, 5]
        self.assertEqual(tamanho(fila), 3)
        desenfileirar(fila)
        self.assertEqual(tamanho(fila), 2)
        desenfileirar(fila)
        self.assertEqual(tamanho(fila), 1)
        desenfileirar(fila)
        self.assertEqual(tamanho(fila), 0)

    def test_07_fila_vazia(self):
        fila = [4, 50, 2]
        self.assertFalse(fila_vazia(fila))
        desenfileirar(fila)
        self.assertFalse(fila_vazia(fila))
        desenfileirar(fila)
        self.assertFalse(fila_vazia(fila))
        desenfileirar(fila)
        self.assertTrue(fila_vazia(fila))
        enfileirar(fila, 12)
        self.assertFalse(fila_vazia(fila))

    def test_08_primeiro(self):
        fila = [4, 3, 2]
        prim_num = primeiro(fila)
        self.assertEqual(prim_num, 4)
        if fila != [4, 3, 2]:
            self.fail('nao era pra voce ter retirado nada da fila')

    def test_09_vira_1(self):
        soldados = [1, 2, 3, 4]
        vira_1(soldados)
        self.assertEqual(soldados, [2, 3, 4, 1])
        vira_1(soldados)
        self.assertEqual(soldados, [3, 4, 1, 2])

    def test_10_vira_5(self):
        soldados = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        vira_5(soldados)
        self.assertEqual(soldados, [6, 7, 8, 9, 1, 2, 3, 4, 5])
        vira_5(soldados)
        self.assertEqual(soldados, [2, 3, 4, 5, 6, 7, 8, 9, 1])

    def test_11_vira_n(self):
        soldados = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        vira_n(soldados, 5)
        self.assertEqual(soldados, [6, 7, 8, 9, 1, 2, 3, 4, 5])
        vira_n(soldados, 5)
        self.assertEqual(soldados, [2, 3, 4, 5, 6, 7, 8, 9, 1])
        soldados = [1, 2, 3, 4, 5, 6]
        vira_n(soldados, 3)
        self.assertEqual(soldados, [4, 5, 6, 1, 2, 3])
        vira_n(soldados, 3)
        self.assertEqual(soldados, [1, 2, 3, 4, 5, 6])
        vira_n(soldados, 1)
        self.assertEqual(soldados, [2, 3, 4, 5, 6, 1])

    def test_12_vira_4_mata_1(self):
        soldados = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        vira_4_mata_1(soldados)
        self.assertEqual(soldados, [6, 7, 8, 9, 1, 2, 3, 4])
        vira_4_mata_1(soldados)
        self.assertEqual(soldados, [2, 3, 4, 6, 7, 8, 9])
        vira_4_mata_1(soldados)
        self.assertEqual(soldados, [8, 9, 2, 3, 4, 6])
        vira_4_mata_1(soldados)
        self.assertEqual(soldados, [6, 8, 9, 2, 3])

    def test_13_fila_inicial(self):
        self.assertEqual(fila_inicial(4), [1, 2, 3, 4])
        self.assertEqual(fila_inicial(8), [1, 2, 3, 4, 5, 6, 7, 8])

    def verifica_fila(self, fila, codigo_correto):
        codigo_resp_aluno = hashlib.sha224(
            str(fila).encode('utf-8')).hexdigest()
        self.assertEqual(codigo_resp_aluno, codigo_correto)


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


runTests()
