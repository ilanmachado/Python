"""
Tipo Booleano

Álgebra Booleana criada por Gearge Boole

2 Constantes: Verdadeiro ou Falso
True => Verdadeiro
False => Falso

OBS.: Sempre com a inicial maiúscula

Errado:
true, false

Certo
True, False

"""

ativo = False
print(ativo)

"""
Operação Básica. Fazendo a negação de um booleano, ele retorna sempre o valor contrário
"""
# Negação (not)
print(not ativo)

"""
Ou (or)
Depende de duas ou mais variáveis, bastando que uma delas seja verdadeira para 
que a saída seja verdadeira

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
logado = False
print(ativo or logado)

"""
E (and)
Depende de duas ou mais variáveis, bastando que uma delas seja falsa para 
que a saída seja falsa

True AND True -> True
True AND False -> False
False AND True -> False
False AND False -> False
"""
