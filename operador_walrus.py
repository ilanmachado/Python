"""
Operador Walrus permite fazer a atribuição e retorno de valor em uma unica expressão.

variavel := expressão


nome = 'Ilan Machado'
print(nome)

print(nome := 'Ilan Machado')

# Utilizado até o python 3.7

cesta = []
fruta = input('Informe a fruta: ')
while fruta != 'jaca':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ')

print(cesta)

"""

# A partir do python 3.8 utilizando o operador Walrus

cesta = []
while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)

print(cesta)

