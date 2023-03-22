"""
Módulo Collection - Default Dict
Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido
Caso tentemos, acessar uma chave que não existe, essa chave será criada e atribuída
o valor default

dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) # Gera KeyError

OBS: lambda são funções sem nome, que podem ou não receber parâmetros de entradae
e retornar valores
"""

# Fazendo import Default Dict
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python'

print(dicionario)

print(dicionario['outro']) # KeyError no dicionário comum, mas aqui não

print(dicionario)


