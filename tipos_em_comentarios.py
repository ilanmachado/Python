import math

def circunferencia(raio):
    # type: (float) -> float
    return 2*math.pi * raio

print(circunferencia(8))

# print(circunferencia('teste'))


def cabecalho1(texto, alinhamento= True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

# cabecalho1(texto=43 ,alinhamento='outros')

def cabecalho2(
        texto, # type: str
        alinhamento=True # type: bool
): # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return

cabecalho2(texto='42', alinhamento=False)



