"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são conhecidos por Chaves {}

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Iterar sobre dicionário
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R${receita[chave]}')
    # Acessando chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando valores
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionário

print(receita.items())

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

# Soma*, Valor Máx*, Valor Min*, Tamanho
# Se os valores forem inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)


