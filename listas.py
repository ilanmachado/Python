"""
Listas em Pyhton funcionam como vetores/matrizes (arrays) em outras linguagens, com
a diferença de serem DINÂMICO e também podermos colocar qualquer tipo dedado.

Linguagens C/Java: Arrays
    - Possuem e tipo de dado fixo;
    Ou seja, nessas linguagens se você cria um array do tipo INT e com tamanho 5, este
    array será SEMPRE do tipo inteiro e poderá ter SEMPRE o máximo de 5 valores.

Em linguagem Python;
    - Dinâmico: Não possui tamanho fixo, ou seja, podemos criar listas e simplesmente ir
    adicionando elementos;
    - Qualquer tipo de dado: não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo
    de dado;

As listas em Python são representadas por colchetes: []

type([])

lista1 =[1, 99, 4, 27, 1, 65, 2, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista
num = 17
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de uma valor de uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementor em uma lista, utilizamos a função append
print(lista1)
lista1.append(42)
print(lista1)

# Com append, conseguimos colocar apenas 1 elemento por vez
# lista1.apprend(12, 34, 56) # Erro

lista1.append([8, 3, 1]) # coloca a lista como elemento único (sublista
print(lista1)
if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67]) # coloca cada elemento na lista como valor adicional.

# Podemos inserir um novo elemento na lista informando a posição no índice
# Não substitui o valor inicial, sendo o mesmo deslocado para cima
lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos facilmente juntar duas listas
lista1 = lista1 + lista2
lista1.extend(lista2)
print(lista1)

# Copiar uma lista
lista6 = lista1.copy()

# Podemos contar quantos elementos existem dentro de uma lista
print(len(lista5))

# Podemos facilmente remover um elemento de uma lista
# Remove apenas o último elemento e também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover o elemento pelo índice
# Os elementos a direita deste índice serão deslocados para direita
# Se não houver algum elemento no índice especificado, ocorrerá IndexError
lista5.pop(2)
print(lista5)

# Podemos zerar a lista, eliminando todos os elementos
print(lista5)
lista5.clear()
print(lista5)

# Podemos converter uma string em lista
# Exemplo 1
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split() # O comando split separa os elementos pelo espaço entre eles.
print(curso)

# Exemplo 2
curso = 'Programação,em,Python,Essencial'
print(curso)
curso = curso.split(',') # Define qual caractere será feita a separação
print(curso)

# Convertendo lista em string
lista6 = ['Programação', 'em', 'Python']
print(lista6)

# Peda a lista e coloca espaço em cada elemento
curso = ' '.join(lista6)
print(curso)

# Peda a lista e coloca sifrão em cada elemento
curso = '$'.join(lista6)
print(curso)


# Podemos colocar qualquer tipo de elemento na lista
lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 46523165]




# Iterando sobre uma lista
# Exemplo 1 - Utilizando for
soma = 0
for elemento in lista4:
    print(elemento)
    soma += elemento
print(soma)

# Exemplo 2 - Utilizando While
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto a lista ou digite 'sair' para encerrar: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)


# Utilizando variáveis em listas
numeros = [1, 2, 3]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
numeros = [num1, num2, num3]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

#           0        1          2       3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o indice negativo, pense na lista como un circulo, onde
# o final de un elemento esta ligado ao inicio da listd

print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde

# print(cores[-5]) # Erro, pois ndo existe indice -5

cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)


# Encontrar o valor do índice em uma lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Para o valor 7
print(numeros.index(7))

# Para o valor 9
print(numeros.index(9))

# Para o valor 5, onde existe 2x na lista, ele retorna apenas o primeiro
print(numeros.index(5))

# Podemos fazer busca dentro de um range:
print(numeros.index(5, 1)) # buscando a partir do índice 1
print(numeros.index(5, 2)) # buscando a partir do índice 2
print(numeros.index(5, 3)) # buscando a partir do índice 3

print(numeros.index(8, 3, 6)) # buscando o valor 8 entre os índices 3 a 6

# Listas com slicing
lista = [1, 2, 3, 4]
print(lista[1:]) #Iniciando a lista a partir do indice 1 até o fim da lista, ignorando o primeiro
print(lista[:2]) #Iniciando a lista a partir do indice 0 até o índice 2, -1
print(lista[:4]) #Iniciando a lista a partir do indice 0 até o índice 4, -1
print(lista[1:3]) #Iniciando a lista a partir do indice 1 até o índice 3, -1

print(lista[1::2]) #Iniciando a lista a partir do indice 1 até o final, de dois em dois
print(lista[::2]) #Iniciando a lista do início até o final, de dois em dois
print(lista[::-1]) #Iniciando a lista do fim até o início , de trás pra frente

# Invertendo valores da lista
nomes = ['Ilan', 'Machado']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['Ilan', 'Machado']
nomes.reverse()
print(nomes)


# Realizar soma, valor max, valor min
# *Lista deve ter valores inteiros reais

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))   # soma
print(max(lista))   # valor máximo
print(min(lista))   # valor mínimo
print(len(lista))   # tamanho da lista

# Converter lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de lista
# O número de elementos variáveis deve ser igual ao número de índice da lista
lista = [1, 2, 3]
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra
# Forma 1 : Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy() # Ao utilizar a copy, a lista independe da cópia, uma alteração não afeta a outra
print(nova)
nova.append(4)

print(lista)
print(nova)

# Forma 2: Shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista # Uma alteração depende da outra, afetando tanto a lista quanto a cópia
print(nova)
nova.append(4)

print(lista)
print(nova)
"""

