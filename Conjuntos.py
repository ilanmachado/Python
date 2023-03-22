"""
Conjuntos

- Conjuntos em qualquer linguagem de programaçao estamos fazendo referência à Teoria dos Conjuntos
da Matemática

- Em Python, os conjuntos são chamados de Sets

Dito isto, da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, não são indexados;

Conjuntos são úteis para se utilizar quando precisamos armazenar elementos, não se importando com
a ordenação deles. Quando não precisamos se preocupar com cahves, valores, itens duplicados.

Os conjuntos (sets) são referencias com Chaves {}

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:
    - Um dicionario tem chave/valor
    - Um conjunto tem apenas valor


# Definindo um Conjunto

# Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) # Temos valores repetidos
print(s)
print(type(s))

# OBS: Caso exista no conjunto, valores duplicados, o mesmo será
# ignorado sem gerar erro e não fará parte do conjunto

# Forma 2 (mais comum)
s = {1, 2, 3, 4, 5, 6, 7, 2, 3}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')


# Não existem valores duplicados e não existe ordem
dados = '99, 2, 34, 23, 12, 1, 44, 5, 2, 34'

# Listas aceitam valores, então retorna 10 elementos
lista = [99, 2, 34, 23, 12, 1, 44, 5, 2, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores, então retorna 10 elementos
tupla = (99, 2, 34, 23, 12, 1, 44, 5, 2, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionários NÂO aceitam valores duplicados, retornando 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 12,  1, 44, 5, 2, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos NÂO aceitam valores duplicados, retornando 8 elementos
conjunto = {99, 2, 34, 23, 12, 1, 44, 5}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como todo conjuntos em Python podemos colocar tipos de dados misturados em Sets
s = {1, 'b', True, 1.44, 44}
print(s)
print(type(s))

# Podemos iterar em um Set normalmente
for valor in s:
    print(valor)


# Casos interessantes de Conjuntos (Sets)

# Imagine um cadastro de visitante em um museu.
# Os visitantes informam de qual cidade vieram.
# Nós adicionamos cada cidade em uma lista Python, pois podem acontecer repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# Quantas cidades únicas temos? Utilizamos Set para isso...
print(len(set(cidades)))

s = {1, 2, 3}

# Adicionando elementos em um conjunto
s.add(4)
s.add(5)
s.add(5) # Duplicidade não gera erro. É ignorado e não é adicionado
print(s)

# Removendo elementos de um conjunto
# Forma 1
s.remove(3) # Não é índice, mas sim o valor a ser removido
print(s)

# Forma 2
s.discard(2) # Caso não exista o valor, nenhum erro é gerado
print(s)

s = {1, 2, 3}
print(s)

#Copiando um conjunto para outro

# Forma 1 (deep copy - elementos distintos e independentes)
novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 (Shalow Copy)
novo = s
novo.add(4)

print(novo)
print(s)

# Podemos remover todos os elementos
s.clear()
print(s)


# Métodos matemáticos de Conjuntos

# Imagine dois conjuntos de estudantes: Curso de Python e Curso de Java
# Alguns alunos que estudam Java, também estudam Python

estudantes_python = {'Mark', 'Pat', 'Zé', 'Cauê', 'Gui','Ed'}
estudantes_java = {'Ana', 'Pat', 'Frã', 'Ju', 'Gui'}

# Precisamos gerar uma lista de nomes únicos de estudantes

# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
# {'Ana', 'Cauê', 'Ed', 'Mark', 'Gui', 'Zé', 'Frã', 'Pat', 'Ju'}
print(unicos1)

# Forma 2 - Utilizando o pipe '|'
unicos2 = estudantes_python | estudantes_java
print(unicos2)


# Gera um conjunto que estudo tanto em Java quanto em Python

# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar uma lista de estudantes de curso que não estão no outro
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""

# Soma*, Valor Max*, Valor Min*, Tamanho
# Se os valores forem inteiros ou reais

s = {1 ,2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
