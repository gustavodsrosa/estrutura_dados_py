
from typing import ItemsView
import unittest


'''
EXEMPLO: Observe a função 'soma', implementada a seguir.
'''


def soma(a, b):
    resultado = a + b           # linha 1
    return resultado            # linha 2


print('Exemplo soma:')
print(soma(1, 2))

'''
    O que acontece na função é o seguinte: quando você executa a instrução
    soma(1, 2), a função soma é chamada. Ela guarda o valor 1 na variavel 'a'
    e o valor 2 na variavel 'b', e começa a executar os comandos da função.
    Na linha 2, a função devolve um número, que é o resultado do
    cálculo realizado.

    ERRO COMUM: algumas pessoas tem dificuldade em passar valores (parâmetros)
    para as funções e implementam elas como no exemplo abaixo.
    A forma correta de passar parâmetros para funções é chamar a função
    e colocar os números nos parênteses, como fizemos na chamada da função soma
'''


def soma_incorreta(a, b):
    # linha 0
    a = 2                   # linha 1
    b = 5                   # linha 2
    resultado = a + b
    return resultado


print('Exemplo soma_incorreta:')
print(soma_incorreta(100, 10))      # exibe 7
print(soma_incorreta(12, 1))        # exibe 7

'''
    Ao chamar soma_incorreta(100, 10), e depois soma_incorreta(12, 1),
    a função sempre retorna o mesmo número: 7.
    O que acontece é que na linha 0, 'a' vale 100 e 'b' vale 10.
    Mas nas linhas 1 e 2, nós colocamos 2 no 'a' e 5 no 'b'. Assim, teremos
    sempre 7 no resultado.
    Resumindo: os números não devem ser definidos dentro da função,
    mas depois, quando você for usar a função.

    ERRO COMUM: outro erro comum é usar input na função.
    Novamente, a forma mais adequada é que os números devem ser recebidos como
    parâmetros ao chamar a função, e não definidos dentro da função.
'''


def soma_incorreta2(a, b):
    # linha 0
    a = int(input('Primeiro Numero:'))      # linha 1
    b = int(input('Segundo Numero:'))       # linha 2
    resultado = a + b
    return resultado


'''
    Uma coisa muito util é chamar uma função dentro de outra.
    Observe o exemplo abaixo:
'''


def soma3(a, b, c):
    dois_primeiros = soma(a, b)             # chama a função soma
    resultado = soma(dois_primeiros, c)     # chama a função soma novamente
    return resultado


print('Exemplo soma3:')
print(soma3(4, 2, 1))       # exibe 7
print(soma3(9, 3, 10))      # exibe 22


'''
Utilizando o que você relembrou até agora, resolva os exercícios a seguir:
'''

'''
EXERCÍCIO 1:
    Implemente a função 'quadrado' que recebe um número e retorna o resultado
    desse número ao quadrado.
    Lembre-se que a função deve utilizar a instrução return, para devolver
    o resultado. Se você utilizar print dentro da função para mostrar o
    resultado, a sua função estará incorreta.
'''


def quadrado(a):
    numero = a ** 2
    return numero


'''
EXERCÍCIO 2:
    Implmente a função 'soma_dos_quadrados' que receba dois numeros e devolve
    a soma dos seus quadrados.
    Você pode utilizar a função 'quadrado' definida anteriormente para
    facilitar a implementação.
'''


def soma_dos_quadrados(a, b):
    return (a ** 2) + (b ** 2)


'''
EXERCÍCIO 3:
    Implemente a função 'media', que recebe três valores numéricos e retorna
    a média dos valores.
'''


def media(a, b, c):
    return (a + b + c) / 3


'''
EXERCÍCIO 4:
    Implemente a função 'calcular_salario', que recebe o salário atual de um
    funcionário e retorna o salário com um reajuste de aumento, sendo que:
    - Caso o salário atual seja maior que R$ 2.000,00, o funcionário receberá
      7% de aumento.
    - Caso contrário, o funcionário receberá 15% de aumento.
'''


def calcular_salario(salario):
    if salario > 2000:
        return salario * 1.07
    else:
        return salario * 1.15


'''
EXERCÍCIO 5
    defina uma funcao 'maximo2' que recebe dois numeros e retorna o maior deles
'''


def maximo2(a, b):
    if a > b:
        return a
    else:
        return b


'''
EXERCÍCIO 6
    defina uma funcao 'maximo3' que recebe três numeros e retorna o maior deles
'''


def maximo3(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


'''
EXERCÍCIO 7
    defina uma funcao 'maximo4' que recebe quatro numeros e retorna o maior
    deles
'''


def maximo4(a, b, c, d):
    if a > b and a > c and a > d:
        return a
    elif b > a and b > c and b > d:
        return b
    elif c > a and c > b and c > d:
        return c
    else:
        return d


'''
EXERCÍCIO 8:
    Implemente a função 'soma_divisores', que recebe como parâmetro de entrada
    um número positivo e retorna a soma de todos os divisores desse número.
    Por exemplo:
    - caso o número seja 15, o retorno deve ser 24 (1+3+5+15).
    - caso o número seja 30, o retorno deve ser 72 (1+2+3+5+6+10+15+30)
'''


def soma_divisores(n):
    lista = []
    for a in range(1, n+1):
        if n % a == 0:
            lista.append(a)
    i = 0
    for a in lista:
        i += a
    return i


# Mostrando valores na tela
print()
print("Exercício 1")
print(quadrado(3), 9)
print(quadrado(10), 100)
print()
print("Exercício 2")
print(soma_dos_quadrados(2, 3), 13)
print(soma_dos_quadrados(5, 7), 74)
print()
print("Exercício 3")
print(media(2, 6, 25), 11)
print()
print("Exercício 4")
print(calcular_salario(3000), 3210.0)
print(calcular_salario(2000), 2300.0)
print(calcular_salario(1000), 1150.0)
print()
print("Exercício 5")
print(maximo2(1, 2), 2)
print(maximo2(3, 2), 3)
print(maximo2(-1, -2), -1)
print(maximo2(-1, 2), 2)
print()
print("Exercício 6")
print(maximo3(1, 2, 3), 3)
print(maximo3(10, 2, 3), 10)
print(maximo3(1, 20, 3), 20)
print()
print("Exercício 7")
print(maximo4(1, 2, 3, 4), 4)
print(maximo4(10, 2, 3, 4), 10)
print(maximo4(1, 20, 3, 4), 20)
print(maximo4(1, 2, 30, 4), 30)
print()
print("Exercício 8")
print(soma_divisores(10), 18)
print(soma_divisores(30), 72)


'''
ATENÇÃO:
    O trecho de código a seguir não deve ser alterado.
    Ele irá testar a implementação das funções quando o arquivo for executado.
'''


class TestStringMethods(unittest.TestCase):
    
    def test_01_soma(self):
        self.assertEqual(soma(1, 5), 6)
        self.assertEqual(soma(1, 5), 6)

    def test_02_soma3(self):
        self.assertEqual(soma3(1, 2, 3), 6)
        self.assertEqual(soma3(9, 2, 1), 12)

    def test_03_quadrado(self):
        self.assertEqual(quadrado(3), 9)
        self.assertEqual(quadrado(10), 100)

    def test_04_soma_dos_quadrados(self):
        self.assertEqual(soma_dos_quadrados(2, 3), 13)
        self.assertEqual(soma_dos_quadrados(5, 7), 74)

    def test_05_media(self):
        self.assertEqual(media(2, 6, 25), 11)
        self.assertEqual(round(media(7, 7, 8), 2), 7.33)

    def test_06_calcular_salario(self):
        self.assertEqual(calcular_salario(3000), 3210.0)
        self.assertEqual(calcular_salario(2000), 2300.0)
        self.assertEqual(calcular_salario(1000), 1150.0)

    def test_07_maximo2(self):
        self.assertEqual(maximo2(1, 2), 2)
        self.assertEqual(maximo2(3, 2), 3)
        self.assertEqual(maximo2(-1, -2), -1)
        self.assertEqual(maximo2(-1, 2), 2)

    def test_08_maximo3(self):
        self.assertEqual(maximo3(1, 2, 3), 3)
        self.assertEqual(maximo3(10, 2, 3), 10)
        self.assertEqual(maximo3(1, 20, 3), 20)

    def test_09_maximo4(self):
        self.assertEqual(maximo4(1, 2, 3, 4), 4)
        self.assertEqual(maximo4(10, 2, 3, 4), 10)
        self.assertEqual(maximo4(1, 20, 3, 4), 20)
        self.assertEqual(maximo4(1, 2, 30, 4), 30)

    def test_10_soma_divisores(self):
        self.assertEqual(soma_divisores(10), 18)
        self.assertEqual(soma_divisores(30), 72)


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2, failfast=False).run(suite)


print("\nResultado dos Testes:\n")
runTests()
