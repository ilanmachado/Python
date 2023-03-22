"""
def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}!'

print(cumprimentar('Ilan'))

"""

def cabecalho(texto: str, alinhamento: bool = True):
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')

print(cabecalho('ilan machado'))
print(cabecalho('ilan machado', alinhamento=False))
