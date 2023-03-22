"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma:

Se a gente pensar em um programa qualquer, geralmente temos:

Input -> Process -> Output

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada, mas não possuem saída;
- Não possuem entrada, mas possuem saída;
- Possuem entrada e saída;


# Refatorando uma função

def quadrado(numero):
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

# Exemplo de outra refatoração

def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!')

cantar_parabens('Samuel')

# Funções podem ter n parâmetros de entrada, ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessários. Eles são separadods por vírgula.

# Exemplo
def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(5, 2))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))

# Caso informado número errado de parâmetro ou argumentos, teremos TypeError
print(soma(2, 3, 4)) # TypeError: argumentos a maior
print(soma(2)) # TypeError: argumentos a menor


# Nomeando parâmetros

def nome_completo(nome, sobrenome):
    return f'Seu nome é completo é {nome} {sobrenome}'

print(nome_completo('Samuel', 'Machado'))

# A diferença entre parâmetros e argumentos
# Parâmtros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parâmtros importa!

nome = 'Ilan'
sobrenome = 'Machado'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (KeyWord Arguments)
# Caso utilezemos nomes dos parâmetros dos argumentos para informá-los, podemos
# utilizar qql ordem.

print(nome_completo(nome='Rose', sobrenome='Machado'))
print(nome_completo(sobrenome=sobrenome, nome=nome))


"""


# Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))

