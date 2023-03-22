# Utilize Camel Case antes de Classes


class Calculadora:
    pass

class CalculadoraCientifica:
    pass


# utilize nomes em minúsculos, separados por enderline para funções ou variáveis

def soma_par():
    pass

numero_par = 4
numero_impar = 5

# Utilize 4 espaços para identação! (NÃO USE TAB!)
if 'a' in 'banana':
    print('Tem')

# Linhas em branco


class Classe:
    pass


# Imports devem ser separados
# Import de forma errada
import sys, os

#import de forma certa
import sys
import os

# Não há problema em utilizar
from types import StringType, ListType

# Quando há necessidade de muitos imports, fazer:
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo
