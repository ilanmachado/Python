"""
Módulo Collection - Named Tuple

# Recap Tupla
tupla = (1, 2, 3)
print(tupla[1])

Named Tuple -> São tuplas diferenciadas, onde, especificamos um nome para a mesma
e também parâmetros.
"""

# Importando
from collections import namedtuple

# Precisamos defini o nome e parâmetro
# Forma 1
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Utilizando
rex = cachorro(idade=2, raca='vira-lata', nome='Rex')

# Acessando

# Forma 1
print(rex)
print(rex[0])   # idade
print(rex[1])   # raça
print(rex[2])   # nome

# Forma 2
print(rex.idade)    # idade
print(rex.raca)     # raça
print(rex.nome)     # nome

print(rex.index('vira-lata'))
print(rex.count('vira-lata'))