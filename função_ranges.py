"""
Ranges
- Precisamos conhecer o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com o loop for

Ranges são utilizadas para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especifica.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

#Exemplo
for cont in range(11):
    print(cont)


# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)

#Exemplo
for cont in range(1, 11):
    print(cont)


# Forma 3
range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)
#Exemplo 3
for cont in range(5, 50, 5):
    print(cont)

# Forma 4 (inverso)
range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)
#Exemplo 3
for cont in range(10, 1, -1):
    print(cont)
"""


