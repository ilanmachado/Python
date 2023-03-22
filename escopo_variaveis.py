"""
Escopo Variáveis

"""

numero = 46 # numero -> Variável Global

if numero > 10:
    novo = numero + 10 # novo -> Variável Local

print(numero)
print(novo) # O erro acontece porque a variável é local
