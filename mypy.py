def cabecalho(texto: str, alinhamento: bool = True):
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')

print(cabecalho('ilan machado'))

print(cabecalho('ilan machado', alinhamento=False))

print(cabecalho('ilan machado', alinhamento=True)

"""
MyPy e Type Hinting trabalham em conjunto, pois não adianta utilizar 
sozinho que o MyPy não irá funcionanar
"""
