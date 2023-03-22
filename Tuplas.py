"""
Tuplas (Tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:
1. As tuplas são representadas por ()
2. As tuplas são imutáveis, ou seja, ao se criar uma tupla, ela não muda.
    Toda operação em uma tupla, gera uma nova tupla


# CUIDADO 1: As tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)     # Cria uma tupla
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6       # Cria tupla sem parêntese
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento
tupla3 = (4)    # Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,)   # Isso é uma tupla
tupla5 = 5,     # Isso também é uma tupla
print(tupla4)
print(type(tupla4))
print(tupla5)
print(type(tupla5))

# Podemos concluir que tuplas são definidas pela vírgula e não pelo uso de parênteses
# (4)   -> Não é tupla
# (4,)  -> É tupla
# 4,    -> É tupla

# Podemos gerar uma tupla dinamicamente com range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla
# As regras são as mesmas para o numero de variáveis e elementos da tupla

tupla = ('Ilan', 'Machado')
nome, sobrenome = tupla
print(nome)
print(sobrenome)

# Métodos para adição e remoção de elementos das tuplas não existem, uma vez que tuplas são imutáveis

# Soma*, valor máximo, valor mínimo, Tamanho
# Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenção de tupla
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutáveis
print(tupla1)
print(tupla2)


# Concatenção de tupla
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutáveis
print(tupla1)
print(tupla2)
tupla3 = tupla1 + tupla2
print(tupla3)

# Verifica se determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(3 in tupla)

# Iterando sobre uma tupla
tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))
print(tupla.count('b'))
print(tupla.count('c'))

nome = tuple('Ilan Machado')
print(nome)
print(nome.count('a'))

# Dicas de utilização de tuplas

# Devemos utilizar tuplas sempre que precisamos modificar os dados contidos em uma coleção

# Exemplo 1
semana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')

# O acesso aos elementos é semelhante a de uma lista
print(semana[3])

# Iterar com while
i = 0
while i < len(semana):
    print(semana[i])
    i += 1


# Exemplo 2
semana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')

# Verificar em qual índice um elemento está na tupla
print(semana.index('Sábado'))

#OBS: Caso o elemento não exista na tupla, #ValueErro

# Exemplo 3
semana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')

# Slicing

# Tupla[início:fim:passo]
print(semana[0::])
print(semana[3::1])
print(semana[::-1])

# Por que utilizar tuplas?
- Tuplas são mais rápidas que listas
- Tuplas deixam seu código mais seguro devido a imutabilidade
- Trabalhar com elementos imutáveis deixa seu código mais seguro

# Copiando uma tupla para outra
tupla = (1, 2, 3)
print(tupla)

nova = tupla
print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra

print(tupla)
print(nova)
print(outra)

"""

