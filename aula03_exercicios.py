# Exercicio 1: Ao final da execução da função abaixo,
# qual o número de execuções em função de n?
# Qual a complexidade usando a notação O()? O(n²)

def funcao1(n):  # O(n²) -> Quadrática
    s = 0    # 1
    for i in range(n):  # n
        for j in range(n):  # n * n
            s = s + 1  # n
    return n, s  # 1


print(f"Função 1 -> {funcao1(2)}")
print(f"Função 1 -> {funcao1(3)}")
print(f"Função 1 -> {funcao1(4)}")
print()


# Exercicio 2: Ao final da execução da função abaixo,
# qual o número de execuções em função de n?
# Qual a complexidade usando a notação O()?

def funcao2(n):  # O(n³) -> Cúbica
    s = 0  # 1
    for i in range(n):  # n
        for j in range(n):  # n * n
            for k in range(n):  # n * n * n
                s = s + 1  # n
    return n, s  # 1


print(f"Função 2 -> {funcao2(2)}")
print(f"Função 2 -> {funcao2(3)}")
print(f"Função 2 -> {funcao2(4)}")
print()


# Exercicio 3: Considerando a função abaixo e responda as questões:
# a) se a = 10 e b = 100, quantas vezes as linhas marcadas são executadas?
#    1 -> 100, 2 -> 100
# b) se a = 20 e b = 10, quantas vezes as linhas marcadas são executadas?
#    1 -> 400, 2 -> 10
# c) se a = 100 e b = 10, quantas vezes as linhas marcadas são executadas?
#    1 -> 10000, 2 -> 10
# d) Qual a complexidade usando a notação O()?

def funcao3(a, b):  # Quadrática -> O(n²)
    cont = 0
    for i in range(a):
        for j in range(a):
            cont = cont + 1     # linha 1
    for i in range(b):
        cont = cont + 1         # linha 2
    return cont


print(f"Função 3 -> {funcao3(10, 100)}")
print(f"Função 3 -> {funcao3(20, 10)}")
print(f"Função 3 -> {funcao3(100, 10)}")
print()


# Exercicio 4: Considerando a função abaixo e responda as questões:
# a) se a lista tem tamanho 1000, quantas vezes as linhas marcadas são
# executadas? 1000² vezes
# b) se a lista tem tamanho 2000, quantas vezes as linhas marcadas são
# executadas? 2000² vezes
# c) se a lista tem tamanho 4000, quantas vezes as linhas marcadas são
# executadas? 4000² vezes
# d) Qual a complexidade usando a notação O()? 

'''
def funcao4(lista):  # O(n²) -> quadrática
    i = 0
    for e1 in lista:
        for e2 in lista:
            i = i + 1         # linha 1
    return e1, e2


print(f"Função 4 -> {funcao4(list(range(1000)))}")
print(f"Função 4 -> {funcao4(list(range(2000)))}")
print(f"Função 4 -> {funcao4(list(range(4000)))}")
print()
'''

# Exercicio 5: Considerando a função abaixo e responda as questões:
# a) se a lista tem tamanho 1000, quantas vezes as linhas marcadas são
# executadas? 1000
# b) se a lista tem tamanho 2000, quantas vezes as linhas marcadas são
# executadas? 2000
# c) se a lista tem tamanho 4000, quantas vezes as linhas marcadas são
# executadas? 4000
# d) Qual a complexidade usando a notação O()?

'''
def funcao5(lista):  # O(n) -> Linear
    i = 0
    for e in lista:
        i = i + 1             # linha 1
    return e


print(f"Função 5 -> {funcao5(list(range(1000)))}")
print(f"Função 5 -> {funcao5(list(range(2000)))}")
print(f"Função 5 -> {funcao5(list(range(4000)))}")
print()
'''

# Exercicio 6: Considerando a função abaixo e responda as questões:
# a) se a lista tem tamanho 1000, quantas vezes as linhas marcadas são
# executadas? 1000
# b) se a lista tem tamanho 2000, quantas vezes as linhas marcadas são
# executadas? 2000
# c) se a lista tem tamanho 4000, quantas vezes as linhas marcadas são
# executadas? 4000
# d) Qual a complexidade usando a notação O()? 

'''
def funcao6(lista):  # O(n2) -> Cúbica
    i = 0
    for e in lista:
        i = i+1             # linha 1
    for e1 in lista:
        for e2 in lista:
            i = i+1         # linha 2
    return e, e1, e2


print(f"Função 6 -> {funcao6(list(range(1000)))}")
print(f"Função 6 -> {funcao6(list(range(2000)))}")
print(f"Função 6 -> {funcao6(list(range(4000)))}")
print()
'''

# Exercicio 7:
# Escreva uma função que recebe uma lista de tamanho n e troca de posição seu
# maior e seu menor elementos.
# Você não pode usar outro vetor como auxiliar e não deve utilizar funções
# prontas do python.
# A função deve ter complexidade O(n).


def funcao7(lista):
    lista = list(lista)
    maior = lista[0]
    menor = lista[0]
    i_maior = 0
    i_menor = 0

    for i in range(0, len(lista)):
        if i == 0:
            maior = menor = lista[i]
        else:
            if lista[i] > maior:
                i_maior = i
                maior = lista[i]

            if lista[i] < menor:
                i_menor = i
                menor = lista[i]

    lista[i_maior] = menor
    lista[i_menor] = maior

    return lista


print(f"Função 7 -> {funcao7(list([1,2,9,3,4,5,0,6,7]))}")

# Exercicio 8:
# Escreva uma função para inverter a ordem dos elementos de uma lista de
# tamanho n.
# Você não pode usar outro vetor como auxiliar e não deve utilizar funções
# prontas do python.
# A função deve ter complexidade O(n).


def funcao8(lista):
    lista = list(lista)
    for i in range(len(lista)):
        lista_inversa = lista[::-1]
    return lista_inversa


print(f"Função 8 -> {funcao8(list(range(10)))}")

