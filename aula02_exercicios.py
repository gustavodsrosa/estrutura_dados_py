'''
Analise a função abaixo, que encontra o maior valor contido em uma lista

Considerando o pior caso e a notação O grande,
responda as seguintes questões:

1 - Quantas vezes a linha marcada é executada, para uma lista de tamanho 1000?
    # A linha marcada é executada 1000 vezes.

2 - Quantas vezes a linha marcada é executada, para uma lista de tamanho 2000?
    # A linha marcada é executada 2000 vezes.

3 - Quantas vezes a linha marcada é executada, para uma lista de tamanho 4000?
    # A linha marcada é executada 4000 vezes.

4 - Qual a ordem de magnitude da função?
    # Conforme a notação O, a ordem de magnitude é linear -> O(n)
'''


def valor_maximo(lista):
    cont = 0                        # Inserido para testes
    maximo = lista[0]
    for valor in lista:
        cont += 1                   # Inserido para testes
        if (valor > maximo):        # linha marcada
            maximo = valor
    return maximo, cont


lista = list(range(1000))
print(valor_maximo(lista))

lista = list(range(2000))
print(valor_maximo(lista))

lista = list(range(4000))
print(valor_maximo(lista))
