"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela,
verificar para que a função seja simplificada.

Já utilizamos várias funções desde que iníciamos este curso
print()
max()
min()
len()
e muitas outras
"""

# # Exemplo de utilização de funções
# cores = ['verde', 'amarelo', 'azul', 'branco']
#
# # Utilizando uma função Built In (integrada) no Python:
# print(cores)
#
# curso = 'Programação em Python'
# print(curso)
#
# cores.append('roxo')
# print(cores)
#
# cores.clear()
# print(cores)
#
# # DRY - Don't Repeat Yourself - Não repita a você mesmo - Não repita seu código

"""
# Como definir funções?
Em Python, a forma geral de definir funções é:

def nome_do_funcao(paramtros_de_entrada):
    bloco_da_funcao

nome_da_funcao -> SEMPRE com letras minúsculas, caso nome composto, separado com underline(_)
parametros_de_entrada -> Opcionais, caso haja mais de um, separar por vírgula.
bloco_da_funcao -> Também chamado de corpo da função, ou implementação. É onde o processamento 
acontece. Pode haver ou não retorno da função

OBS: Para definir uma função, usar a palavra reservada 'def', informando ao Python que estamos
definindo uma função. Também abrir o bloco com dois pontos(:) que é utilizado 

"""
# Definição
# def diz_oi():
#     print('oi!')

"""
1. Veja que dentro das nossas funções, podemos utilizar outras funções;
2. Veja que nossa função, só executa uma tarefa;
3. Veja que está função não recebe nenhum parâmtro de entrada;
4. Veja que está função, não retorna nada;
5. SEMPRE utilizar o parênteses ao utilizar uma função.
"""

# Utilizando funções (chamada de execução)
# diz_oi()

def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print()

# for n in range(5):
#     cantar_parabens()

# Podemos criar uma função, e executá-la através de uma variável
canta = cantar_parabens
canta()
