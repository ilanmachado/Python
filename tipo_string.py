"""
Tipo String

Em Python, um dado é considerado string sempre que:
- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas dupla -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
- Estiver entre aspas duplas triplas

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Loko's Bar"
print(nome)
print(type(nome))

nome = 'Geek \nUniversity'
print(nome)
print(type(nome))

nome = "Geek University"
print(nome)
print(type(nome))

print(nome.upper()) # Deixa dos caracteres em caixa alta

print(nome.lower()) # Deixa os caracteres em minúsculo

print(nome.split()) #Transforma em uma lista de strings
"""

nome = 'Geek University'
print(nome)
print(nome[::-1]) # Inversão de String

texto = 'socorram me subino onibus em marrocos' # Palíndromo
print(texto)
print(texto[::-1])

