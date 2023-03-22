"""
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None (nada)

# Exemplo Função

def quadrado_de_7():
    print(7 * 7)

ret = quadrado_de_7()
print(f'Retorno de ret: {ret}') # Não retorna nada

OBS: Funções Python que retornam valores, devem retornar com a palavra reservada return.
OBS: Não é necessário criar variável para receber um retorno de uma função. Podemos passar a
execução da função para outras funções.


# Exemplo Função refatorada (reescrever o código)

def quadrado_de_7():
    return 7 * 7

# Foi criada uma variável para receber o retorno da função
ret = quadrado_de_7()

print(f'Retorno: {ret}')


# Refatorando a primeira função

def diz_oi():
    return ('Oi ')

alguem = 'Pedro!'

print(diz_oi() + alguem)

Observações sobre o return
1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter na função, diferentes returns;
3 - Podemos, em uma função, retornar qql tipo de dado, até mesmo múltiplos valores

# Exemplo 1
def diz_oi():
    print('Estou sendo executado!')
    return 'Oi! '
    print('Estou sendo executado!')

print(diz_oi())

# Exemplo 2
def nova_funcao():
    variavel = False #True #None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())


# Exemplo 3
def outra_funcao():
    return 2, 3, 4, 5

# n1, n2, n3, n4 = outra_funcao()
# print(n1, n2, n3, n4)

print(outra_funcao())
print(type(outra_funcao()))

# Vamos criar uma função para jogar cara ou coroa
from random import random

def joga_moeda():
    # Gera um numero randomico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

"""

# Erros comuns na utilização de retun e codificações necessárias
def eh_impar():
    numero = 60
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())
