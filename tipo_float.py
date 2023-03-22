"""
Tipo Float

Tipo Real, Decimal

Casas Decimais

Obs: O separador de casas decimais é o ponto e não a vírgula.
"""

# Errado do ponto de vista Float, e gera uma Tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para int
"""
Ao se converter, perdemos precisão
"""
res=int(valor)
print(res)
print(type(res))

# Podemos trabalhar com número
variavel = 5j
print(type(variavel))
