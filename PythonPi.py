"""
Nome: pi.py
Objetivo: obter o valor de Pi para n número de casas decimais
Autor: Pradipta (geekpradd)
Algoritmo: Algoritmo Chudnovsky
Licença: MIT
Dependências do módulo:
Matemática fornece enraizamento quadrado rápido
Decimal fornece o tipo de dados Decimal que é muito melhor do que Float
sys é necessário para definir a profundidade da recursão.
"""

from __future__ import print_function
import math, sys 
from decimal import *
getcontext().rounding =  ROUND_FLOOR
sys.setrecursionlimit(100000)

python2 = sys.version_info[0] == 2 


def factorial(n):

    """
    Retorna o fatorial de um número usando recursão.
    Parâmetros:
    n - Número para obter o fatorial
    """

    if not n:
        return 1

    return n*factorial(n-1)


def getIteratedVAlue(k):

    """
    Retorna as Iterações conforme fornecido no Algoritmo de Chudnovsky.
    k iterações dá k-1 casas decimais .. Uma vez que precisamos de k casas decimais
    faça iterações iguais a k + 1

    Parâmetros:
    k - Número de dígitos decimais para obter
    """

    k = k+1
    getcontext().prec = k
    sum = 0
    for k in range(k):
        first = factorial(6*k)*(13591409+545140134*k)
        down = factorial(3*k)*(factorial(k))**3*(640320**(3*k))
        sum += first/down 
    return Decimal(sum)

def getValueOfPi(k):

    """
    Retorna o valor calculado de Pi usando o valor iterado do loop
    e alguma divisão dada no Algoritmo Chudnovsky
    Parâmetros:
    k - Número de dígitos decimais até o qual o valor de Pi deve ser calculado
    """

    iter = getIteratedVAlue(k)
    up = 426880*math.sqrt(10005)
    pi = Decimal(up)/iter

    return pi 

def shell():
    """
    Função de console para criar o Shell interativo.
    É executado apenas quando __name__ == __main__ ou seja, quando o script está sendo chamado diretamente
    Sem valor de retorno e parâmetros
    """
    print("Bem vindo a calculadora Pi, digite o número de dígitos que Pi deve ser calculado ou digite 'quit' para sair." )

    while True:
        print(">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        if not entry.isdigit():
            print("Você não digitou um número. Tente novamente.")
        else:
            print(getValueOfPi(int(entry)))


if __name__ == '__main__':
    shell()