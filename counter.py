"""
Módulo Collections - Counter (Contador)
Collection -> High Performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter
que é parecido com um dicionário, contendo como chave o elemento da lista passada como
parâmetro e como valor a quantidade de ocorrências desse elemento.

# Realizando o import
from collections import Counter

# Exemplo1

# Podemos utilzar qualquer iterável. (usando uma lista)
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 7, 7, 7, 7, 45, 45, 88, 88, 34, 43]

# Utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)
# Counter({3: 5, 7: 4, 1: 3, 2: 2, 4: 2, 45: 2, 88: 2, 5: 1, 6: 1, 34: 1, 43: 1})
# Para cada elemento da lista, o Counter criou uma chave e atribuiu a qtde de ocorrências

# Exemplo 2
print(Counter('Ilan Machado'))


# Exemplo 3
texto = """ Em linguística, a noção de texto é ampla e ainda aberta a uma definição mais precisa.
Grosso modo, pode ser entendido como manifestação linguística das ideias de um autor, que
serão interpretadas pelo leitor de é é acordo com seus conhecimentos linguísticos e culturais.
Seu tamanho é variável."""

palavras = texto.split()
# print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrências no texto
print(res.most_common(5))

"""


