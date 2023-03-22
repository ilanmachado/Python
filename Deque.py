"""
Módulo Colection - Deque
Podemos dizer que um Deque é uma lista de alta performance.
"""

# Importando
from collections import deque

# Criando deque
deq = deque('ilan')
print(deq)

# Adicionando elementos no deque ao final
deq.append('o')
print(deq)

# Adicionando elementos no deque ao começo
deq.appendleft('k')
print(deq)

# Remover elementos
print(deq.pop())    # Remove e retorna o último elemento
print(deq)

print(deq.popleft())    # Remove e retorna o primeiro elemento
print(deq)
