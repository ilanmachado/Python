"""
Funções com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parâmtros seja opcional

# Exemplo de função onde o parâmetro seja :
print('Ilan Machado')
print()
print('Python')

# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado())

def exponencial(numero=2, potencia=2):
    return numero ** potencia

print(exponencial(2, 3)) # 2 * 2 * 2
print(exponencial(3, 3)) # 3 * 3

print(exponencial(3)) # Por padrão eleve ao quadrado
print(exponencial(3, 5)) # Eleva a potência informada pelo usuário

# Caso seja informado um argumento, será elevado ao quadrado
# Caso seja informado dois argumentos, o primeiro será elevado ao exponencial do segundo

print(exponencial())

# OBS:  Em funções Python, os valores default sempre devem estar ao final da declaração.
def teste(potencia, num=2):
    return num ** potencia

print(teste(2))

# Outros exemplos
def soma(num1=1, num2=1):
    return num1 + num2

print(soma(4, 3))
print(soma(4))
print(soma())


# Exemplo mais complexo
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ilan'))
print(mostra_informacao(nome='Rose'))

# Por que utilizar com valor default?
# Nos permite ser mais flexíveis nas funções
# Evita erros com parâmetros incorretos
# Nos permite trabalhar com exemplos mais legíveis de códigos

# Quais tiṕos de dados podemos utilzar para parâmtros?
# R: Qualquer tipo de dados: numeros, strings, floats, booleanos, listas,
# tuplas, dicionários, funções, etc

# Exemplo
def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões

# Variáveis globais
# Variáveis locais

instrutor = 'Ilan' # variável global

def diz_oi():
    instrutor = 'Python' # variável local
    return f'Oi {instrutor}'

print(diz_oi())

# OBS: A variável local se sobressai sobre a variável global, caso ambas tenham o mesmo nome

def diz_oi():
    prof = 'Geek'
    return f'Olá {prof}'

print(diz_oi())

print(prof # NameError

# ATENÇÃO com variáveis globais (Se puder evitar, evite)

total = 0

def incrementar():
    global total
    total += 1 # A variável local é usada para processamento sem ter sido inicializada
    return total

print(incrementar())
print(incrementar())
print(incrementar())



"""

# Podemos ter funções que são declaradas dentro de funções, e tem
# uma forma especial de escopo de variável

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador += 1

        return contador
    return dentro()

print(fora())
print(fora())
print(fora())
