import unittest


'''
EXERCÍCIO 1:
    implemente a função 'soma' que recebe uma lista de números e retorna a
    soma de todos eles.
    NÃO utilize a função sum do python. Implemente a lógica você mesmo!
'''


def soma(lista):
    i = 0
    for a in lista:
        i += a
    return i


'''
EXERCÍCIO 2:
    faça uma função 'media' que recebe uma lista de números e retorna a média.
    ou seja, soma todos os números e divide pela quantidade de numeros
'''


def media(lista):
    i = 0
    for a in lista:
        i += a
    return i / len(lista)


'''
EXERCÍCIO 3:
    Faça a função 'cresce' que acrescenta o proximo numero a uma lista.
    por exemplo cresce([7, 8]) deve devolver [7, 8, 9]
'''


def cresce(lista):
    valor = lista[-1]
    valor_a_ser_mudado = valor + 1
    lista.append(valor_a_ser_mudado)
    return lista


'''
EXERCÍCIO 4:
    Implemente uma funcao 'troca', que recebe uma lista e duas posicoes,
    e troca os valores das duas posicoes.
    Um exemplo:
        troca(['a','b','c'], 0, 1) deve retornar ['b','a','c']
    Um exemplo diferente:
        troca(['a','b','c'], 0, 2) deve retornar ['c','b','a']
'''


def troca(lista, pos1, pos2):
    if pos1 == pos2:
        return lista
    else:
        lista[pos1], lista[pos2] = lista[pos2], lista[pos1]
        return lista


'''
EXERCÍCIO 5:
    Implemente uma funcao 'indice_menor', que recebe uma lista e devolve
    o indice do seu menor elemento.
    Se houver mais de um menor elemento, retorna o indice menor.
    Exemplo, se a = [2, 3, 1], então indice_menor(a) retorna 2, pois a[2]==1
    NAO USE "funções prontas" do python, como lista.index nem min(lista)
'''


def indice_menor(lista):
    menor = lista[0]
    posicao = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            posicao = i
    return posicao


'''
EXERCÍCIO 6:
    Faça uma função que recebe uma lista,
    e retorna todos os valores dessa lista que estao acima da média.
    Por exemplo, considerando [1, 2, 3, 4, 5], temos média 3.
    Assim acima_da_media([1, 2, 3, 4, 5]) deve retornar a lista [4, 5]
    Voce pode usar a sua funçao de média, que implementou antes
'''


def acima_da_media(lista):
    i = 0
    for a in lista:
        i += a
    media = i / len(lista)
    nova_lista = []
    for a in range(len(lista)):
        if lista[a] > media:
            nova_lista.append(lista[a])
    return nova_lista


'''
EXERCÍCIO 7:
    Faça uma função quebra em dois, que recebe uma lista e um numero divisor.
    A função devolve duas listas:
    - uma dos numeros da lista menores que o divisor
    - e outra, dos numeros da lista maiores que o divisor
    Se a lista tiver algum números igual ao divisor, ele deve ser colocado
    na lista de maiores
'''


def quebra_em_dois(lista, divisor):
    lista_maiores = []
    lista_menores = []
    for a in range(len(lista)):
        if lista[a] == divisor:
            lista_maiores.append(lista[a])
        elif lista[a] > divisor:
            lista_maiores.append(lista[a])
        else:
            lista_menores.append(lista[a])
    return lista_menores, lista_maiores


'''
EXERCÍCIO 8:
    Uma loja está fazendo uma liquidaçao.
    A funçao 'liquidacao' receberá duas listas.
    Uma contém preços (em reais) e a outra descontos (tb em reais)
    Retorne uma terceira lista, dos preços já com desconto.
    Assim, por exemplo, liquidacao([2,4],[0,3]) é uma situação em que
    o produto de preço 2 tem 0 reais de desconto e o produto de
    preço 4 tem 3 reais de desconto
    A função deve retornar a lista [2, 1]
'''


def liquidacao(precos, descontos):
    lista_final = []
    for a in range(len(precos)):
        if len(precos) != len(descontos):
            break
        valor_lista = precos[a] - descontos[a]
        lista_final.append(valor_lista)
    return lista_final


'''
ATENÇÃO:
    O trecho de código a seguir não deve ser alterado.
    Ele irá testar a implementação das funções quando o arquivo for executado.
'''


class TestPartTwo(unittest.TestCase):

    def test_01_soma(self):
        self.assertEqual(soma([1, 2, 3]), 6)
        self.assertEqual(soma([3, 2, 1]), 6)
        self.assertEqual(soma([3, 10, 15, 30, 2, 1]), 61)

    def test_02_soma(self):
        self.assertEqual(soma([-1]), -1)
        self.assertEqual(soma([3]), 3)
        self.assertEqual(soma([]), 0)

    def test_03_media(self):
        self.assertEqual(media([1]), 1)
        self.assertEqual(media([1, 2]), 1.5)
        self.assertEqual(media([1, 2, 3]), 2)

    def test_04_cresce(self):
        self.assertEqual(cresce([1]), [1, 2])
        self.assertEqual(cresce([5]), [5, 6])
        self.assertEqual(cresce([5, 6]), [5, 6, 7])
        self.assertEqual(cresce([5, 6, 7, 8, 9]), [5, 6, 7, 8, 9, 10])

    def test_05_troca(self):
        self.assertEqual(
            troca([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48], 5, 6),
            [3, 44, 38, 5, 47, 36, 15, 26, 27, 2, 46, 4, 19, 50, 48])
        self.assertEqual(
            troca([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48], 5, 5),
            [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48])
        self.assertEqual(
            troca([3, 44], 0, 1),
            [44, 3])
        self.assertEqual(
            troca([3], 0, 0),
            [3])

    def test_06_indice_menor(self):
        self.assertEqual(
            indice_menor([3, 44, 38, 5, 47, 15, 36, 26,
                          27, 2, 46, 4, 19, 50, 48]),
            9)
        self.assertEqual(
            indice_menor([3, 44, 38, 5, 47, 15, 36,
                          26, 27, 46, 4, 19, 50, 48]),
            0)
        self.assertEqual(
            indice_menor([44, 38, 5, 47, 15, 36, 26, 27, 46, 4, 19, 50, 48]),
            9)

    def test_07_acima_da_media(self):
        self.assertEqual(acima_da_media([1, 2, 3]), [3])
        self.assertEqual(acima_da_media([2, 2, 2]), [])
        self.assertEqual(acima_da_media([-2, 0, 1]), [0, 1])

    def test_08_quebra_em_dois(self):
        self.assertEqual(
            quebra_em_dois([1, 2, 3, 4, 5, 5, 6, 7], 4),
            ([1, 2, 3], [4, 5, 5, 6, 7]))

        self.assertEqual(
            quebra_em_dois([10, 20, 30, 40, 5, 5, 6, 7], 4),
            ([], [10, 20, 30, 40, 5, 5, 6, 7]))

        self.assertEqual(
            quebra_em_dois([10, 20, 30, 40, 5, 5, 6, 7], 100),
            ([10, 20, 30, 40, 5, 5, 6, 7], []))

    def test_09_liquidacao(self):
        precos = [10, 10, 10], [0], [10, 20, 30], [1, 2, 3, 4]
        descontos = [1, 1, 1], [0], [9, 8, 7], [1, 1, 1, 1]
        final = [9, 9, 9], [0], [1, 12, 23], [0, 1, 2, 3]
        for i in range(0, len(precos)):
            self.assertEqual(liquidacao(precos[i], descontos[i]), final[i])


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPartTwo)
    unittest.TextTestRunner(verbosity=2, failfast=False).run(suite)


print("\nResultado dos Testes:\n")
runTests()
